import json
import logging
from typing import List, Dict, Any

# Configure Execution Logs
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - [%(levelname)s] - %(message)s",
    handlers=[logging.FileHandler("agent_execution.log"), logging.StreamHandler()]
)
logger = logging.getLogger(__name__)

class MockLLMClient:
    def generate_response(self, prompt: str) -> str:
        if "market research" in prompt.lower():
            return json.dumps({
                "reasoning": "The user wants a market research strategy. I need to analyze competitors, gather sentiment, and synthesize a report.",
                "plan": [
                    {"step": 1, "tool": "competitor_analysis", "input": "TechCorp AI products"},
                    {"step": 2, "tool": "sentiment_analysis", "input": "Social media feedback on TechCorp"},
                    {"step": 3, "tool": "generate_report", "input": "Synthesize steps 1 and 2"}
                ]
            })
        return json.dumps({
            "reasoning": "Generic business task detected. Creating a standard execution path.",
            "plan": [
                {"step": 1, "tool": "competitor_analysis", "input": "General Market"},
                {"step": 2, "tool": "generate_report", "input": "Standard summary"}
            ]
        })

class BusinessTools:
    @staticmethod
    def competitor_analysis(target: str) -> str:
        return f"Competitor Analysis Result: Found 3 main feature gaps in {target}."

    @staticmethod
    def sentiment_analysis(topic: str) -> str:
        return f"Sentiment Analysis Result: 78% positive sentiment regarding {topic}."

    @staticmethod
    def generate_report(data_summary: str) -> str:
        return f"Final Business Report: Strategy formulated successfully based on ({data_summary})."

class AutonomousBusinessAgent:
    def __init__(self):
        self.llm = MockLLMClient()
        self.tools = BusinessTools()

    def run_agent_step_by_step(self, task_description: str):
        """Yields progress updates to the frontend in real-time"""
        yield {"type": "log", "message": f"🚀 Initializing Agent for Task: '{task_description}'"}
        
        # Planning Phase
        yield {"type": "log", "message": "🧠 Phase 1: Generating reasoning and task plan..."}
        planning_prompt = f"Given the task: '{task_description}', generate a step-by-step plan."
        llm_response = self.llm.generate_response(planning_prompt)
        
        parsed_response = json.loads(llm_response)
        reasoning = parsed_response.get("reasoning", "")
        plan = parsed_response.get("plan", [])
        
        yield {"type": "reasoning", "message": reasoning}
        yield {"type": "plan", "data": plan}

        # Execution Phase
        yield {"type": "log", "message": "⚡ Phase 2: Entering Execution Loop..."}
        context_accumulator = ""

        for step in plan:
            tool_name = step.get("tool")
            tool_input = step.get("input")
            
            yield {"type": "log", "message": f"🔄 Executing Step {step['step']}: Using {tool_name}"}
            
            if hasattr(self.tools, tool_name):
                tool_method = getattr(self.tools, tool_name)
                if tool_name == "generate_report":
                    tool_input = context_accumulator
                
                result = tool_method(tool_input)
                context_accumulator += f" [{result}] "
                
                yield {"type": "step_result", "step": step['step'], "tool": tool_name, "output": result}
            else:
                yield {"type": "log", "message": f"❌ Tool {tool_name} not found."}
                break
        
        yield {"type": "log", "message": "🏁 Task Execution Completed successfully."}