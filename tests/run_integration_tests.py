import csv
import os
import sys

sys.path.append(
    os.path.abspath(
        os.path.join(
            os.path.dirname(__file__),
            ".."
        )
    )
)

from src.sensor import PositionSensor
from src.actuator import Actuator
from src.controller import RestraintController


results = []


def record_result(test_id, category, passed, notes):
    result = "PASS" if passed else "FAIL"

    results.append({
        "Test_ID": test_id,
        "Category": category,
        "Result": result,
        "Notes": notes
    })

    print(
        f"{test_id} | {category} | {result} | {notes}"
    )


# --------------------------------------------------
# NOMINAL TESTS
# --------------------------------------------------

# TC-001
sensor = PositionSensor()
actuator = Actuator()
controller = RestraintController(sensor, actuator)

sensor.set_position("RETRACTED")

accepted = controller.deploy()

passed = (
    accepted is True
    and actuator.get_command() == "EXTEND"
)

record_result(
    "TC-001",
    "Nominal",
    passed,
    "Deploy from RETRACTED"
)


# TC-002
sensor = PositionSensor()
actuator = Actuator()
controller = RestraintController(sensor, actuator)

sensor.set_position("DEPLOYED")

accepted = controller.retract()

passed = (
    accepted is True
    and actuator.get_command() == "RETRACT"
)

record_result(
    "TC-002",
    "Nominal",
    passed,
    "Retract from DEPLOYED"
)


# TC-003
sensor = PositionSensor()
actuator = Actuator()
controller = RestraintController(sensor, actuator)

sensor.set_position("RETRACTED")
controller.deploy()

sensor.set_position("DEPLOYED")
actuator.stop()

passed = (
    sensor.get_position() == "DEPLOYED"
    and actuator.get_command() == "STOP"
)

record_result(
    "TC-003",
    "Nominal",
    passed,
    "Deploy sequence reaches DEPLOYED"
)


# --------------------------------------------------
# BOUNDARY TESTS
# --------------------------------------------------

# TC-004
sensor = PositionSensor()
actuator = Actuator()
controller = RestraintController(sensor, actuator)

sensor.set_position("DEPLOYED")

accepted = controller.deploy()

passed = (
    accepted is False
    and actuator.get_command() == "STOP"
)

record_result(
    "TC-004",
    "Boundary",
    passed,
    "Deploy requested while already DEPLOYED"
)


# TC-005
sensor = PositionSensor()
actuator = Actuator()
controller = RestraintController(sensor, actuator)

sensor.set_position("RETRACTED")

accepted = controller.retract()

passed = (
    accepted is False
    and actuator.get_command() == "STOP"
)

record_result(
    "TC-005",
    "Boundary",
    passed,
    "Retract requested while already RETRACTED"
)


# TC-006
sensor = PositionSensor()
actuator = Actuator()
controller = RestraintController(sensor, actuator)

sensor.set_position("MOVING")

accepted = controller.deploy()

passed = (
    accepted is False
    and actuator.get_command() == "STOP"
)

record_result(
    "TC-006",
    "Boundary",
    passed,
    "Deploy requested while restraint MOVING"
)


# TC-007
sensor = PositionSensor()
actuator = Actuator()
controller = RestraintController(sensor, actuator)

sensor.set_position("MOVING")

accepted = controller.retract()

passed = (
    accepted is False
    and actuator.get_command() == "STOP"
)

record_result(
    "TC-007",
    "Boundary",
    passed,
    "Retract requested while restraint MOVING"
)


# --------------------------------------------------
# FAULT TESTS
# --------------------------------------------------

# TC-008
sensor = PositionSensor()
actuator = Actuator()
controller = RestraintController(sensor, actuator)

sensor.set_fault()

accepted = controller.deploy()

passed = (
    accepted is False
    and actuator.get_command() == "STOP"
    and controller.last_message
    == "DEPLOY REJECTED: SENSOR FAULT"
)

record_result(
    "TC-008",
    "Fault",
    passed,
    "Sensor fault prevents DEPLOY"
)


# TC-009
sensor = PositionSensor()
actuator = Actuator()
controller = RestraintController(sensor, actuator)

sensor.set_position("RETRACTED")
actuator.set_fault()

accepted = controller.deploy()

passed = (
    accepted is False
    and actuator.get_command() == "STOP"
    and controller.last_message
    == "DEPLOY REJECTED: ACTUATOR FAULT"
)

record_result(
    "TC-009",
    "Fault",
    passed,
    "Actuator fault prevents DEPLOY"
)


# TC-010
sensor = PositionSensor()
actuator = Actuator()
controller = RestraintController(sensor, actuator)

sensor.set_position("RETRACTED")
controller.set_power(False)

accepted = controller.deploy()

passed = (
    accepted is False
    and actuator.get_command() == "STOP"
    and controller.last_message
    == "DEPLOY REJECTED: NO POWER"
)

record_result(
    "TC-010",
    "Fault",
    passed,
    "Loss of power prevents DEPLOY"
)


# TC-011
sensor = PositionSensor()
actuator = Actuator()
controller = RestraintController(sensor, actuator)

sensor.set_position("UNKNOWN")

accepted = controller.deploy()

passed = (
    accepted is False
    and actuator.get_command() == "STOP"
    and controller.last_message
    == "DEPLOY REJECTED: UNKNOWN POSITION"
)

record_result(
    "TC-011",
    "Fault",
    passed,
    "Unknown sensor position prevents movement"
)


# TC-012
sensor = PositionSensor()
actuator = Actuator()
controller = RestraintController(sensor, actuator)

sensor.set_position("DEPLOYED")
controller.set_power(False)

accepted = controller.retract()

passed = (
    accepted is False
    and actuator.get_command() == "STOP"
    and controller.last_message
    == "RETRACT REJECTED: NO POWER"
)

record_result(
    "TC-012",
    "Fault",
    passed,
    "Loss of power prevents RETRACT"
)


# --------------------------------------------------
# SAVE RESULTS
# --------------------------------------------------

output_path = os.path.join(
    os.path.dirname(__file__),
    "..",
    "reports",
    "test_results.csv"
)

with open(
    output_path,
    "w",
    newline=""
) as file:

    fieldnames = [
        "Test_ID",
        "Category",
        "Result",
        "Notes"
    ]

    writer = csv.DictWriter(
        file,
        fieldnames=fieldnames
    )

    writer.writeheader()
    writer.writerows(results)


print()
print("Integration test execution complete.")
print(
    f"Results saved to: "
    f"{os.path.abspath(output_path)}"
)