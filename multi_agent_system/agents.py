# agents.py
import time
from communication import communication_bus

@communication_bus.task(name="agents.data_analysis_agent")
def data_analysis_agent(data):
    """Agent specialized in processing and analyzing raw data."""
    print(f"\n[Data Agent] Received task with data: {data}")
    print("[Data Agent] Analyzing patterns...")
    time.sleep(3)  # Simulating heavy analytical work
    result = {"status": "Success", "summary": f"Analyzed {len(data)} data points."}
    print(f"[Data Agent] Task Complete. Result: {result}")
    return result

@communication_bus.task(name="agents.report_generation_agent")
def report_generation_agent(analysis_summary):
    """Agent specialized in formatting results into a readable report."""
    print(f"\n[Report Agent] Received task for summary: {analysis_summary}")
    print("[Report Agent] Generating PDF/Markdown structure...")
    time.sleep(2)  # Simulating file generation
    report_id = f"REP-{int(time.time())}"
    result = {"report_id": report_id, "path": f"/reports/{report_id}.pdf"}
    print(f"[Report Agent] Task Complete. Generated: {report_id}")
    return result