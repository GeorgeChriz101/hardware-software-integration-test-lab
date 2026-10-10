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

---

## Phase 2 Integration Check

The initial hardware/software component integration was manually verified.

### Nominal Check

Starting Position:

RETRACTED

Command:

DEPLOY

Expected Actuator Command:

EXTEND

Observed:

EXTEND

Result:

PASS

### Return Check

Starting Position:

DEPLOYED

Command:

RETRACT

Expected Actuator Command:

RETRACT

Observed:

RETRACT

Result:

PASS

### Sensor Fault Check

Condition:

Position Sensor FAULT

Command:

DEPLOY

Expected Actuator Command:

STOP

Observed:

STOP

Result:

PASS