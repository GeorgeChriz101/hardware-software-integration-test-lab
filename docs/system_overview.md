# Hardware/Software Integration & Test Lab

## Project Purpose

This project demonstrates a simplified hardware/software integration and verification workflow.

The project models a fictional aircraft cargo restraint system containing:

- A position sensor
- A software controller
- An actuator
- Operator commands
- Fault monitoring

The purpose is to test how software responds to simulated hardware inputs under normal, boundary, and fault conditions.

---

## System Description

The Aircraft Cargo Restraint Control System controls a simplified cargo restraint mechanism.

The restraint can exist in three primary states:

- RETRACTED
- MOVING
- DEPLOYED

An operator can request:

- DEPLOY
- RETRACT

A position sensor reports the current mechanical position to the software controller.

The controller evaluates:

- Operator command
- Sensor position
- Sensor health
- Actuator health
- System power

The controller then determines whether the actuator should:

- EXTEND
- RETRACT
- STOP

---

## System Workflow

Operator Command
        |
        v
Software Controller
        |
        +----------------+
        |                |
        v                v
 Position Sensor     Fault Status
        |                |
        +-------+--------+
                |
                v
         Control Decision
                |
                v
             Actuator
                |
                v
      Mechanical Movement
                |
                v
         Position Sensor

---

## Main Components

### Position Sensor

Provides the simulated mechanical position of the cargo restraint.

Possible states:

- RETRACTED
- MOVING
- DEPLOYED
- UNKNOWN

### Software Controller

Processes sensor information and operator commands.

The controller determines whether actuator movement is allowed.

### Actuator

Receives commands from the controller.

Possible commands:

- EXTEND
- RETRACT
- STOP

---

## Safety Behavior

The simplified controller should stop actuator movement when:

- System power is unavailable
- A sensor fault is detected
- An actuator fault is detected
- An invalid position is reported
- The requested destination has already been reached

---

## Testing Scope

The integration lab will eventually test:

### Nominal Conditions

Expected normal operation.

Examples:

- Deploy from RETRACTED
- Retract from DEPLOYED

### Boundary Conditions

Conditions near operational limits.

Examples:

- Deploy command while already DEPLOYED
- Retract command while already RETRACTED

### Fault Conditions

Simulated hardware or communication problems.

Examples:

- Sensor failure
- Invalid sensor reading
- Actuator failure
- Loss of power