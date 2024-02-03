from typing import List, Optional

from task import Task
from resources import Resources


class TaskQueueScratch:
    """
    Implementation of TaskQueue from scratch
    without using additional modules
    """
    def __init__(self):
        self.tasks: List[Task] = []

    def add_task(self, task: Task):
        index = self._find_position_to_insert(task)
        self.tasks.insert(index, task)

    def _find_position_to_insert(self, new_task: Task) -> int:
        # Custom binary search algorithm to optimally insert the new task
        left, right = 0, len(self.tasks) - 1
        while left <= right:
            mid = (left + right) // 2
            if self.tasks[mid].priority > new_task.priority:
                left = mid + 1
            elif self.tasks[mid].priority < new_task.priority:
                right = mid - 1
            else:  # priorities are equal, use id for tie-break
                if self.tasks[mid].id < new_task.id:
                    left = mid + 1
                else:
                    right = mid - 1
        return left

    def get_task(self, available_resources: Resources) -> Optional[Task]:
        for i, task in enumerate(self.tasks):
            # Check available resources for each task
            if (
                task.resources.ram <= available_resources.ram
                and task.resources.cpu_cores <= available_resources.cpu_cores
                and task.resources.gpu_count <= available_resources.gpu_count
            ):
                return self.tasks.pop(
                    i
                )  # Remove and return the task if it can be executed
        # Return None if the queue is empty or no task found that can be executed with available resources
        return None
