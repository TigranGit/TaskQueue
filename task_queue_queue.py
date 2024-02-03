from dataclasses import dataclass
from typing import List, Optional
import queue

from task import Task
from resources import Resources


@dataclass(order=True)
class PrioritizedTask:
    priority: int
    task: Task


class TaskQueueQueue:
    """
    Implementation of TaskQueue
    using 'PriorityQueue' from standard module 'queue'
    """
    def __init__(self):
        self.tasks = queue.PriorityQueue()

    def add_task(self, task: Task):
        # negate the priority to have higher priority for higher value
        pq_task = PrioritizedTask(priority=-task.priority, task=task)
        self.tasks.put(pq_task)

    def get_task(self, available_resources: Resources) -> Optional[Task]:
        temp_tasks: List[Task] = []

        while not self.tasks.empty():
            pq_task = self.tasks.get()
            task = pq_task.task

            if (
                task.resources.ram <= available_resources.ram
                and task.resources.cpu_cores <= available_resources.cpu_cores
                and task.resources.gpu_count <= available_resources.gpu_count
            ):
                # Requeue the tasks that couldn't be processed due to resource constraints
                for temp_task in temp_tasks:
                    self.tasks.put(temp_task)
                return task
            else:
                temp_tasks.append(pq_task)

        # If no suitable task was found, requeue all tasks
        for temp_task in temp_tasks:
            self.tasks.put(temp_task)

        return None
