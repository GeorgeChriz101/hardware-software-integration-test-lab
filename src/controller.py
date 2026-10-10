class RestraintController:
    def __init__(self, sensor, actuator):
        self.sensor = sensor
        self.actuator = actuator
        self.power_available = True
        self.last_message = "SYSTEM READY"

    def set_power(self, available):
        self.power_available = available

        if not available:
            self.actuator.stop()
            self.last_message = "POWER UNAVAILABLE"

    def deploy(self):
        if not self.power_available:
            self.actuator.stop()
            self.last_message = "DEPLOY REJECTED: NO POWER"
            return False

        if self.sensor.get_health() == "FAULT":
            self.actuator.stop()
            self.last_message = "DEPLOY REJECTED: SENSOR FAULT"
            return False

        if self.actuator.health == "FAULT":
            self.actuator.stop()
            self.last_message = "DEPLOY REJECTED: ACTUATOR FAULT"
            return False

        position = self.sensor.get_position()

        if position == "UNKNOWN":
            self.actuator.stop()
            self.last_message = "DEPLOY REJECTED: UNKNOWN POSITION"
            return False

        if position == "DEPLOYED":
            self.actuator.stop()
            self.last_message = "ALREADY DEPLOYED"
            return False

        if position == "MOVING":
            self.actuator.stop()
            self.last_message = "DEPLOY REJECTED: RESTRAINT MOVING"
            return False

        if position == "RETRACTED":
            self.actuator.extend()
            self.last_message = "DEPLOY COMMAND ACCEPTED"
            return True

        self.actuator.stop()
        self.last_message = "DEPLOY REJECTED"
        return False

    def retract(self):
        if not self.power_available:
            self.actuator.stop()
            self.last_message = "RETRACT REJECTED: NO POWER"
            return False

        if self.sensor.get_health() == "FAULT":
            self.actuator.stop()
            self.last_message = "RETRACT REJECTED: SENSOR FAULT"
            return False

        if self.actuator.health == "FAULT":
            self.actuator.stop()
            self.last_message = "RETRACT REJECTED: ACTUATOR FAULT"
            return False

        position = self.sensor.get_position()

        if position == "UNKNOWN":
            self.actuator.stop()
            self.last_message = "RETRACT REJECTED: UNKNOWN POSITION"
            return False

        if position == "RETRACTED":
            self.actuator.stop()
            self.last_message = "ALREADY RETRACTED"
            return False

        if position == "MOVING":
            self.actuator.stop()
            self.last_message = "RETRACT REJECTED: RESTRAINT MOVING"
            return False

        if position == "DEPLOYED":
            self.actuator.retract()
            self.last_message = "RETRACT COMMAND ACCEPTED"
            return True

        self.actuator.stop()
        self.last_message = "RETRACT REJECTED"
        return False

    def get_status(self):
        return {
            "power": self.power_available,
            "sensor_position": self.sensor.get_position(),
            "sensor_health": self.sensor.get_health(),
            "actuator_command": self.actuator.get_command(),
            "actuator_status": self.actuator.get_status(),
            "message": self.last_message
        }