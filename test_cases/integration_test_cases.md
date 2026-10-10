# Integration Test Cases

## TC-001 — Deploy From Retracted

Category: Nominal

Initial State:
RETRACTED

Command:
DEPLOY

Expected Result:
Actuator command = EXTEND

---

## TC-002 — Retract From Deployed

Category: Nominal

Initial State:
DEPLOYED

Command:
RETRACT

Expected Result:
Actuator command = RETRACT

---

## TC-003 — Complete Deploy Sequence

Category: Nominal

Initial State:
RETRACTED

Command:
DEPLOY

Simulated Final Position:
DEPLOYED

Expected Result:
Final position = DEPLOYED
Actuator command = STOP

---

## TC-004 — Deploy While Already Deployed

Category: Boundary

Initial State:
DEPLOYED

Command:
DEPLOY

Expected Result:
Command rejected
Actuator command = STOP

---

## TC-005 — Retract While Already Retracted

Category: Boundary

Initial State:
RETRACTED

Command:
RETRACT

Expected Result:
Command rejected
Actuator command = STOP

---

## TC-006 — Deploy While Moving

Category: Boundary

Initial State:
MOVING

Command:
DEPLOY

Expected Result:
Command rejected
Actuator command = STOP

---

## TC-007 — Retract While Moving

Category: Boundary

Initial State:
MOVING

Command:
RETRACT

Expected Result:
Command rejected
Actuator command = STOP

---

## TC-008 — Sensor Fault

Category: Fault

Condition:
Position sensor = FAULT

Command:
DEPLOY

Expected Result:
Command rejected
Actuator command = STOP

---

## TC-009 — Actuator Fault

Category: Fault

Condition:
Actuator = FAULT

Command:
DEPLOY

Expected Result:
Command rejected
Actuator command = STOP

---

## TC-010 — Power Loss During Deploy Request

Category: Fault

Condition:
Power unavailable

Command:
DEPLOY

Expected Result:
Command rejected
Actuator command = STOP

---

## TC-011 — Unknown Position

Category: Fault

Condition:
Sensor position = UNKNOWN

Command:
DEPLOY

Expected Result:
Command rejected
Actuator command = STOP

---

## TC-012 — Power Loss During Retract Request

Category: Fault

Condition:
Power unavailable

Command:
RETRACT

Expected Result:
Command rejected
Actuator command = STOP