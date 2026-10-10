# Hardware / Software Integration Architecture

```mermaid
flowchart LR

A[Operator Command]
B[Software Controller]
C[Position Sensor]
D[Actuator]
E[Mechanical Position]
F[Power Status]
G[Fault Status]

A -->|DEPLOY / RETRACT| B
C -->|Position Feedback| B
F -->|Available / Unavailable| B
G -->|Health Status| B

B -->|EXTEND / RETRACT / STOP| D
D --> E
E --> C