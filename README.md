# README
---
# Historical Battles & Generals Database
---

## Table of Contents

1. [Project Brief](#project-brief)
    + [Proposal](#proposal)
2. [Trello Board](#trello-board)
    + [Start Point](#start-board)
    + [Rolling Changes](#rolling-changes)
    + [End Point](#end-point)
3. [Risk Assessment](#risk-assessment)
4. [Project Architecture](#project-architecture)
    + [Entity Relationship Diagram](#entity-relationship-diagram)
    + [Architecture Diagram](#architecture-diagram)
    + [Issues Encountered](#issues-encountered)
5. Design Considerations
    + Front End
    + Back End
    + UI
6. Testing
    + Pytest Testing
    + Postman Testing
    + Final Report
7. Deployment
    + Toolset
    + CI Server Implementation
    + Branch and Merge Log
8. Front End Implementation
9. Improvements for Future Versions
+ Authors
+ Acknowledgements

## Project Brief
"Create a CRUD application with utilisation of supporting tools, methodologies and technologies that encapsulate all core modules covered during training."

### Proposal
A database of historical battles and generals. Users would be able to read, edit, delete and add to the database with generals and battles of their interest.
## Trello Board
---

My Kanban board on Trello was used to track progress and manage the needed tasks.

### Start Point

[picture of the board](https://github.com/Finn969/Project-SFIA-1/blob/master/Trello%20Board.png)

I followed the set of tasks laid out in the 'Milestones' posted on slack.
### Rolling Changes


### End Point

## Risk Assessment, to be edited
---

|Risk No.|Risk|Description|Hazard|Likelihood|Impact|Solution|
|---|---|---|---|---|---|---|
|1.0.1|Overrun on time.|Due to poor time management, the project is not completed.|Worst case scenario, marks are lost due to lack of coverage of brief.|2|5|Make good use of Kanban to manage workflow, and efficient time use of office resources.|
|1.0.2|Data breach on workstation.|Due to accident or malicious action, workstation is compromised.|Worst case scenario, severe progress loss.|1|5|Change passwords on workstation, keep e-services logged off when not in use.|
|1.1.1|Overrunning on GCP free data limits.|An instance is left running, or an account breach enables the resources on the account to be drained.|Worst case scenario, databases are unaccessable.|1|5|Continue monitoring GCP usage. Copy databases offline as final backup.|
|1.1.2.1|Database security: SQL|The GCP server is breached in some way, compromising data integrity.|Worst case scenario, data is lost, or user data is compromised.|3|5|Ensure user and personal data is encrypted, and passwords hashed, before being moved to the database.|
|1.1.2.2|Database security: SSH|Unmanaged connections cause data leak or damage, keys are lost or stolen.| Worst case scenario, GDPR noncompliance or total data compromisation.|2|5|Learn and make use of GCP's SSH key management role system, and implement it correctly.|
|1.1.2.3|Database security: SQL-I|Unsanitised user input allows SQL injection into the database.|Worst case scenario, database is maliciously destroyed.|2|5|Ensure any user accessible inputs are sanitised, and implement permission roles.|

## Project Architecture
---

### Entity Relationships

### Overall Architecture

### Issues Encountered
