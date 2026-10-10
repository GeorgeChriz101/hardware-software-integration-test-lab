# Integration Test Plan

## Objective

Verify that the simulated sensor, controller, and actuator interact correctly under normal, boundary, and fault conditions.

---

# Test Categories

## 1. Nominal Testing

Tests expected system behavior during normal operation.

Planned examples:

- DEPLOY command from RETRACTED position
- RETRACT command from DEPLOYED position
- Correct actuator command generation
- Correct position feedback handling

---

## 2. Boundary Testing

Tests behavior at operational limits.

Planned examples:

- DEPLOY requested while already DEPLOYED
- RETRACT requested while already RETRACTED
- Command issued while position is MOVING

---

## 3. Fault Testing

Tests controller behavior when hardware or system faults occur.

Planned examples:

- Sensor fault
- Invalid sensor value
- Actuator fault
- Power unavailable
- Lost or unknown position

---

## Expected Safety Principle

When the controller cannot confidently determine that movement is safe, the expected actuator command should be:

STOP