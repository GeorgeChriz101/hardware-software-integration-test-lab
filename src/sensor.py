class PositionSensor:
    def __init__(self):
        self.position = "RETRACTED"
        self.health = "HEALTHY"

    def set_position(self, position):
        valid_positions = [
            "RETRACTED",
            "MOVING",
            "DEPLOYED",
            "UNKNOWN"
        ]

        if position not in valid_positions:
            raise ValueError("Invalid sensor position")

        self.position = position

    def set_fault(self):
        self.health = "FAULT"
        self.position = "UNKNOWN"

    def reset_fault(self):
        self.health = "HEALTHY"

    def get_position(self):
        if self.health == "FAULT":
            return "UNKNOWN"

        return self.position

    def get_health(self):
        return self.health