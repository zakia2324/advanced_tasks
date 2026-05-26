# main.py
import time
from coordinator import CoordinatorAgent

def main():
    print("=== STARTING MULTI-AGENT SYSTEM ===")
    
    # 1. Initialize Coordinator
    coordinator = CoordinatorAgent()
    
    # 2. Mock Data payload
    mock_dataset = [102.4, 98.7, 120.1, 150.3, 88.4]
    
    # 3. Delegate the job asynchronously
    job = coordinator.delegate_workflow(mock_dataset)
    
    # 4. Monitor tracking (Non-blocking check)
    print("[Main] Doing other system tasks while agents work in the background...")
    
    # Block and wait just to show the final output in the console
    final_output = job.get(timeout=10)
    
    print("\n=== WORKFLOW COMPLETE ===")
    print(f"Final System Output: {final_output}")

if __name__ == "__main__":
    main()