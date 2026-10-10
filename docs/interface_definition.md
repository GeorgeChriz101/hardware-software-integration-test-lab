# Hardware / Software Interface Definition

This document defines the simplified interfaces used by the Hardware/Software Integration & Test Lab.

---

## Interface 1 — Operator to Controller

Source:

Operator

Destination:

Software Controller

Commands:

- DEPLOY
- RETRACT

---

## Interface 2 — Position Sensor to Controller

Source:

Position Sensor

Destination:

Software Controller

Possible Values:

- RETRACTED
- MOVING
- DEPLOYED
- UNKNOWN

Health Status:

- HEALTHY
- FAULT

---

## Interface 3 — Controller to Actuator

Source:

Software Controller

Destination:

Actuator

Commands:

- EXTEND
- RETRACT
- STOP

---

## Interface 4 — Actuator Status to Controller

Source:

Actuator

Destination:

Software Controller

Status:

- READY
- MOVING
- FAULT

---

## Interface 5 — System Power

Source:

Aircraft Power Simulation

Destination:

Controller

States:

- AVAILABLE
- UNAVAILABLE