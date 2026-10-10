---

## PR-001 — DEPLOY Request Does Not Correctly Handle Position Sensor Fault

**Status:** Resolved

**Severity:** High

**Environment:**

Hardware/Software Integration Test Simulation

Python controller implementation

**Related Test Case:**

TC-008 — Sensor Fault

**Description:**

During fault-condition integration testing, TC-008 failed when a DEPLOY command was issued while the position sensor was in the FAULT state.

The controller did not execute the intended sensor-fault rejection path.

**Preconditions:**

- System power available
- Position sensor initialized
- Actuator initialized
- Position sensor health set to FAULT

**Steps to Reproduce:**

1. Create a PositionSensor instance.
2. Create an Actuator instance.
3. Create a RestraintController using the sensor and actuator.
4. Set the position sensor to FAULT.
5. Send a DEPLOY command.
6. Observe the controller response.

**Expected Result:**

The controller should reject the DEPLOY command.

The actuator command should remain STOP.

The controller status message should indicate:

DEPLOY REJECTED: SENSOR FAULT

**Actual Result:**

TC-008 failed because the controller did not execute the intended sensor-fault handling path.

**Root Cause:**

The DEPLOY control path was missing the position sensor health validation.

Because the controller did not explicitly reject the command when sensor health was FAULT, the expected fault-handling behavior was not executed.

**Corrective Action:**

Restore the position sensor health check before evaluating movement conditions.

If sensor health is FAULT, the controller shall:

- Command STOP
- Reject the DEPLOY request
- Report DEPLOY REJECTED: SENSOR FAULT

**Regression Result:**

PASS

TC-008 passed after restoring the sensor-health validation.

The full 12-test integration suite was also re-executed.

Final regression result:

- 12 PASS
- 0 FAIL