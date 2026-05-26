# coordinator.py
from celery import chain
from agents import data_analysis_agent, report_generation_agent

class CoordinatorAgent:
    def __init__(self):
        print("[Coordinator Agent] Online and ready to manage workflows.")

    def delegate_workflow(self, raw_data):
        """
        Delegates tasks dynamically. 
        Uses a Celery 'chain' so the output of the Data Agent 
        is automatically piped as the input to the Report Agent.
        """
        print(f"\n[Coordinator] New request received. Initiating delegation workflow...")
        
        # Creating an asynchronous pipeline (Task Delegation)
        workflow = chain(
            data_analysis_agent.s(raw_data), 
            report_generation_agent.s()
        )
        
        # Dispatch to the communication layer
        async_result = workflow.apply_async()
        print(f"[Coordinator] Workflow dispatched to Communication Layer. Task ID: {async_result.id}")
        return async_result