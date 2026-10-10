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


sensor = PositionSensor()
actuator = Actuator()
controller = RestraintController(sensor, actuator)


def show_status(title):
    print()
    print(title)
    print("-" * len(title))

    status = controller.get_status()

    for key, value in status.items():
        print(f"{key}: {value}")


show_status("Initial System State")


print()
print("Sending DEPLOY command...")

controller.deploy()

show_status("After DEPLOY Command")


print()
print("Simulating mechanical movement...")

sensor.set_position("MOVING")

show_status("While Moving")


print()
print("Simulating fully deployed position...")

sensor.set_position("DEPLOYED")
actuator.stop()

show_status("Fully Deployed")


print()
print("Sending RETRACT command...")

controller.retract()

show_status("After RETRACT Command")


print()
print("Simulating fully retracted position...")

sensor.set_position("RETRACTED")
actuator.stop()

show_status("Final System State")