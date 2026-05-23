import time
import random
from datetime import datetime, timedelta

class Task:
    """Represents a single task for the agent to perform."""
    def __init__(self, name, estimated_duration_minutes, difficulty_level):
        self.name = name
        self.estimated_duration_minutes = estimated_duration_minutes
        self.difficulty_level = difficulty_level # Higher difficulty increases chance of "unexpected results"
        self.status = "pending"
        self.result_message = None

    def __str__(self):
        return f"Task('{self.name}', est_duration={self.estimated_duration_minutes}min, status='{self.status}')"

class HermesAgent:
    """Simulates an AI agent managing a workload."""
    def __init__(self, name="Hermes"):
        self.name = name
        self.completed_tasks = []
        self.failed_tasks = []
        self.operational_log = [] # To capture agent's actions and outcomes

    def _simulate_task_execution(self, task):
        """Simulates the agent working on a task, introducing random failures."""
        # Simulate work being done. Scale down actual sleep time for a quick demo.
        # The article mentions a 24-hour experiment; this scales down the real-time wait.
        time.sleep(task.estimated_duration_minutes * 0.05) # 5% of actual duration for demo speed

        # --- Illustrates "Beklenmedik Sonuçlar" (Unexpected Results) ---
        # Simulate unexpected issues based on task difficulty.
        failure_chance = task.difficulty_level * 0.15 # Higher difficulty, higher chance of failure
        if random.random() < failure_chance:
            task.status = "failed"
            task.result_message = f"Encountered an unexpected issue during '{task.name}' (Difficulty: {task.difficulty_level}). Requires human review."
            self.operational_log.append(f"[{datetime.now().strftime('%H:%M:%S')}] {self.name}: Task '{task.name}' FAILED. Reason: {task.result_message}")
            return False
        else:
            task.status = "completed"
            task.result_message = f"Successfully completed '{task.name}'."
            self.operational_log.append(f"[{datetime.now().strftime('%H:%M:%S')}] {self.name}: Task '{task.name}' COMPLETED.")
            return True

    def run_for_duration(self, tasks, total_conceptual_minutes):
        """
        Simulates the agent running for a specified conceptual duration,
        processing tasks and logging outcomes.
        """
        print(f"--- {self.name} Agent Simulation Started (Conceptual duration: {total_conceptual_minutes} minutes) ---")
        
        # --- Illustrates "24 Saatte Hermes Ajanı ile Gerçek İş Yükünü Yönetmek" (Managing Real Workload in 24 Hours) ---
        # We simulate a 24-hour operational window (1440 minutes) as mentioned in the article.
        conceptual_elapsed_time = timedelta(minutes=0)

        task_queue = list(tasks)
        random.shuffle(task_queue) # Simulate dynamic task selection

        while task_queue and conceptual_elapsed_time.total_seconds() < total_conceptual_minutes * 60:
            task = task_queue.pop(0)
            print(f"\n[{datetime.now().strftime('%H:%M:%S')}] {self.name}: Picking up task: {task.name} (Est. duration: {task.estimated_duration_minutes} min)")
            self.operational_log.append(f"[{datetime.now().strftime('%H:%M:%S')}] {self.name}: Starting task '{task.name}'.")

            success = self._simulate_task_execution(task)
            conceptual_elapsed_time += timedelta(minutes=task.estimated_duration_minutes)

            if success:
                self.completed_tasks.append(task)
            else:
                self.failed_tasks.append(task)

            # A small real-time delay between tasks for readability in console
            time.sleep(0.2)

        print(f"\n--- {self.name} Agent Simulation Finished ---")
        print(f"Conceptual total time spent: {conceptual_elapsed_time.total_seconds() / 60:.1f} minutes (out of {total_conceptual_minutes} planned)")
        
        print("\n--- Summary Report ---")
        print(f"Tasks Completed: {len(self.completed_tasks)}")
        for task in self.completed_tasks:
            print(f"  - {task.name}")
        print(f"Tasks Failed: {len(self.failed_tasks)}")
        for task in self.failed_tasks:
            print(f"  - {task.name} ({task.result_message})")
        
        print("\n--- Detailed Agent Log ---")
        for entry in self.operational_log:
            print(entry)

# Main execution block
if __name__ == "__main__":
    # Define a set of typical "real workload" tasks
    daily_tasks = [
        Task("Process incoming emails", 30, 1),
        Task("Generate weekly report", 60, 2),
        Task("Schedule team meeting", 15, 1),
        Task("Develop new feature A", 120, 3),
        Task("Review pull requests", 45, 2),
        Task("Debug production issue", 90, 4), # High difficulty, more prone to failure
        Task("Update documentation", 20, 1),
        Task("Prepare presentation for client", 75, 3),
        Task("Optimize database query", 50, 4), # High difficulty
        Task("Research new technology X", 40, 2),
        Task("Refactor legacy code", 100, 5), # Very high difficulty
    ]

    # Initialize the Hermes agent
    hermes = HermesAgent()

    # --- Simulate the agent's operation over a 24-hour period (1440 minutes) ---
    # The actual script execution time is much shorter due to scaled down `time.sleep`.
    hermes.run_for_duration(daily_tasks, total_conceptual_minutes=1440)
