```markdown
# 🤖 Autonomous Business Agent

An intelligent, multi-step reasoning and task planning agentic workflow built with **Python** and **Streamlit**. This project satisfies the Advanced internship requirement for designing and implementing an autonomous agent loop with structured task planning and execution logging.

## 🚀 Overview

This application demonstrates an **Agentic Loop** capable of broken-down multi-step reasoning. Instead of executing a user prompt linearly, the agent analyzes the prompt, evaluates business requirements, generates a sequential task plan, dynamically selects appropriate internal business tools, and streams operational execution logs back to a real-time monitoring interface.

---

## 🌟 Key Features

* 🧠 **Multi-Step Reasoning:** Evaluates user instructions to build context-aware internal logic before executing tasks.
* 📋 **Dynamic Task Planning:** Formulates a structured JSON plan breaking down the primary directive into smaller, dependency-aware operations.
* ⚡ **Autonomous Execution Loop:** Dynamically invokes target methods/tools based on the generated plan, accumulating context between steps.
* ⚙️ **Real-Time Execution Logs:** Features standard Python logging (`logging`) streaming into a live Streamlit UI dashboard and writing to an audit file (`agent_execution.log`).

---

## 🛠️ Built With

* **Frontend UI:** Streamlit (v1.35.0+)
* **Core Logic:** Native Python OOP (Object-Oriented Programming)
* **Logging Engine:** Python Standard `logging` Library

---

## 📁 Project Structure

```text
├── agent_backend.py      # Core Agent Engine (LLM client simulation, reasoning, tools, and iteration)
├── app.py                # Streamlit UI Dashboard (State handling and real-time log rendering)
├── requirements.txt      # Project library dependencies
└── agent_execution.log   # Automatically generated execution trail for audit tracking
🔧 Installation & Local Setup
1. Prerequisites
Ensure you have Python 3.9 or higher installed on your machine.

2. Clone or Copy the Repository
Create a directory on your local machine and paste the project files: app.py, agent_backend.py, and requirements.txt.

3. Install Dependencies
Open your terminal or command prompt inside the project folder and run:

Bash
pip install -r requirements.txt
4. Run the Application
Launch the Streamlit web server locally using:

Bash
streamlit run app.py