import streamlit as st
import time
from agent_backend import AutonomousBusinessAgent

st.set_page_config(page_title="Autonomous Business Agent", page_icon="🤖", layout="wide")

st.title("🤖 Autonomous Business Agent")
st.caption("Internship Assignment: Multi-step Reasoning, Task Planning & Execution Logs")

# User Input
user_task = st.text_input("Enter Business Task / Prompt:", value="Plan a market research strategy for our upcoming project.")

if st.button("Launch Agent 🚀", type="primary"):
    if user_task:
        agent = AutonomousBusinessAgent()
        
        # Layout Columns
        col1, col2 = st.columns([1, 1])
        
        with col1:
            st.subheader("🧠 Agent Thought Process & Plan")
            reasoning_box = st.empty()
            plan_box = st.empty()
            
        with col2:
            st.subheader("⚙️ Real-time Execution Logs")
            log_box = st.empty()
            
        st.subheader("📋 Step Execution Breakdown")
        steps_container = st.container()
        
        # Streaming the agent updates
        log_history = []
        for update in agent.run_agent_step_by_step(user_task):
            time.sleep(0.5)  # Visual effect delay
            
            if update["type"] == "log":
                log_history.append(update["message"])
                # FIX: Removed key="logs_area" to prevent the duplicate key error
                log_box.text_area("Logs", value="\n".join(log_history), height=300)
                
            elif update["type"] == "reasoning":
                reasoning_box.info(f"**Reasoning:** {update['message']}")
                
            elif update["type"] == "plan":
                plan_box.json(update["data"])
                
            elif update["type"] == "step_result":
                with steps_container:
                    st.success(f"**Step {update['step']} ({update['tool']}):** {update['output']}")
                    
    else:
        st.warning("Please enter a task first!")