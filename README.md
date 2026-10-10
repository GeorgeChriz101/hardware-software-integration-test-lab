# Hardware / Software Integration & Test Lab

A systems-engineering project demonstrating hardware/software integration, nominal testing, boundary testing, fault injection, problem reporting, root cause analysis, corrective action, and regression testing.

The project models a simplified Aircraft Cargo Restraint Control System.

---

## Project Objective

The goal of this project was to practice how software interacts with simulated hardware components and how integrated systems are tested under normal and abnormal conditions.

The project demonstrates:

- Sensor/controller/actuator integration
- Hardware/software interface definition
- Nominal testing
- Boundary-condition testing
- Fault-condition testing
- Automated PASS/FAIL reporting
- Problem reporting
- Root cause analysis
- Corrective action
- Regression testing
- Technical documentation

---

## System Overview

The simulated Aircraft Cargo Restraint Control System contains three main components.

### Position Sensor

Reports the mechanical state of the restraint.

Possible states:

- RETRACTED
- MOVING
- DEPLOYED
- UNKNOWN

### Software Controller

Processes:

- Operator commands
- Position feedback
- Sensor health
- Actuator health
- Power availability

The controller determines whether movement is allowed.

### Actuator

Receives commands from the controller.

Possible commands:

- EXTEND
- RETRACT
- STOP

---

## Integration Workflow

```mermaid
flowchart LR

A[Operator]
B[Software Controller]
C[Position Sensor]
D[Actuator]
E[Mechanical Position]

A -->|DEPLOY / RETRACT| B
C -->|Position Feedback| B
B -->|EXTEND / RETRACT / STOP| D
D --> E
E --> C