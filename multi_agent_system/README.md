# 🤖 Enterprise Multi-Agent System (Advanced Level)

An asynchronous, decoupled Multi-Agent System built using an industrial-grade communication layer and dynamic task delegation. This project demonstrates high-performance parallel task execution across separate specialized agents without blocking the main system orchestration loop.

---

## 👥 Developer Information
* **Email:** nexeagent@gmail.com
* **Phone:** 03222100121
* **LinkedIn:** [Nexe-Agent](https://linkedin.com/in/Nexe-Agent) (Update with your actual link profile URL)

---

## 🏗️ Architectural Overview

The system consists of three distinct pillars:
1. **Separate Agents:** Specialized, isolated processes (`Data Analysis Agent` & `Report Generation Agent`) that operate independently.
2. **Communication Layer:** A centralized message broker network bus driven by **Celery** and backed by **Redis** inside a Docker container.
3. **Task Delegation (Coordinator):** A smart `CoordinatorAgent` that non-blockingly breaks down user requests, builds an execution chain, and dispatches them across the network layer.



---

## 📂 Project Directory Structure

```text
multi_agent_system/
│
├── config.py          # Centralized configuration for Redis and Celery serialization
├── communication.py   # Communication Layer backbone (App initialization & task discovery)
├── agents.py          # Separate business logic definitions for specific Agents
├── coordinator.py     # Task Delegation logic & pipeline orchestration (Chaining)
└── main.py            # User entry point to trigger and monitor workflows

🚀 Technical Stack
Language: Python 3.11+

Task Queue: Celery 5.6.3+

Message Broker: Redis (Running inside Docker)

Concurrency Engine: Gevent (Optimized for Windows platform execution)

🛠️ Setup & Installation Instructions
Follow these steps to run the Multi-Agent environment locally:

1. Clone & Navigate to Project Directory
Bash
cd "C:\Users\AK Technology\Desktop\advancedpro\Multi_Agent_System"

2. Install Project Dependencies
Bash
pip install celery redis gevent

3. Spin up the Communication Broker (Redis via Docker)
Make sure Docker Desktop is open and running, then start the containerized Redis broker:

Bash
docker run -d --name my-redis -p 6379:6379 redis

4. Activate the Background Agents (Terminal 1)
Start the Celery application to bring the separate worker agents online on the communication bus:

Bash
celery -A communication.communication_bus worker --loglevel=info -P gevent

5. Trigger the Orchestration Workflow (Terminal 2)
In a separate terminal window, run the main orchestration script to delegate jobs:

Bash
python main.py

📊 Sample Execution Logs & Output
Agent Worker Node Logs (Terminal 1)
Plaintext
[Data Agent] Received task with data: [102.4, 98.7, 120.1, 150.3, 88.4]
[Data Agent] Analyzing patterns...
Task agents.data_analysis_agent[...] succeeded in 3.155s
[Report Agent] Received task for summary: {'status': 'Success', 'summary': 'Analyzed 5 data points.'}
[Report Agent] Generating PDF/Markdown structure...
Task agents.report_generation_agent[...] succeeded in 2.188s


System Coordinator Output (Terminal 2)
Plaintext
=== STARTING MULTI-AGENT SYSTEM ===
[Coordinator Agent] Online and ready to manage workflows.
[Coordinator] New request received. Initiating delegation workflow...
[Coordinator] Workflow dispatched to Communication Layer. Task ID: 193a3706-...
[Main] Doing other system tasks while agents work in the background...

=== WORKFLOW COMPLETE ===
Final System Output: {'report_id': 'REP-1779755471', 'path': '/reports/REP-1779755471.pdf'}