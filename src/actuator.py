class Actuator:
    def __init__(self):
        self.command = "STOP"
        self.status = "READY"
        self.health = "HEALTHY"

    def extend(self):
        if self.health == "FAULT":
            self.command = "STOP"
            self.status = "FAULT"
            return False

        self.command = "EXTEND"
        self.status = "MOVING"
        return True

    def retract(self):
        if self.health == "FAULT":
            self.command = "STOP"
            self.status = "FAULT"
            return False

        self.command = "RETRACT"
        self.status = "MOVING"
        return True

    def stop(self):
        self.command = "STOP"

        if self.health == "FAULT":
            self.status = "FAULT"
        else:
            self.status = "READY"

        return True

    def set_fault(self):
        self.health = "FAULT"
        self.command = "STOP"
        self.status = "FAULT"

    def reset_fault(self):
        self.health = "HEALTHY"
        self.command = "STOP"
        self.status = "READY"

    def get_command(self):
        return self.command

    def get_status(self):
        return self.status