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


print("Before sensor fault:")
print(controller.get_status())


sensor.set_fault()


print()
print("After sensor fault:")
print(controller.get_status())


print()
print("Sending DEPLOY command...")

controller.deploy()


print()
print("Controller response:")
print(controller.get_status())