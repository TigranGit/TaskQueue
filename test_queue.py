import unittest

from task import Task
from resources import Resources
from task_queue_scratch import TaskQueueScratch
from task_queue_queue import TaskQueueQueue


class TaskQueueScratchTest(unittest.TestCase):
    def test_task_queue(self):
        queue = TaskQueueScratch()

        task_1 = Task(
            id=1,
            priority=10,
            resources=Resources(ram=4, cpu_cores=2, gpu_count=1),
            content="Task 1",
            result="",
        )
        task_2 = Task(
            id=2,
            priority=20,
            resources=Resources(ram=2, cpu_cores=1, gpu_count=0),
            content="Task 2",
            result="",
        )
        task_3 = Task(
            id=3,
            priority=15,
            resources=Resources(ram=6, cpu_cores=3, gpu_count=2),
            content="Task 3",
            result="",
        )

        queue.add_task(task_1)
        queue.add_task(task_2)
        queue.add_task(task_3)

        available_resources = Resources(ram=4, cpu_cores=2, gpu_count=1)
        selected_task = queue.get_task(available_resources)

        # Check if the selected_task is the highest priority task that can be executed with the given resources
        self.assertIsNotNone(selected_task)
        self.assertEqual(
            selected_task.id, 2
        )  # Since task2 has the highest priority and its resources requirements are met.

        # Attempt to get another task with the same available resources
        next_task = queue.get_task(available_resources)
        self.assertIsNotNone(next_task)
        # This time, task 1 is expected to be selected as it fits the available resources.
        self.assertEqual(next_task.id, 1)

        # Finally, verify that no task is available for very limited resources
        limited_resources = Resources(ram=1, cpu_cores=1, gpu_count=0)
        no_task = queue.get_task(limited_resources)
        self.assertIsNone(no_task)


# Unittests for TaskQueueQueue
class TestTaskQueueQueue(unittest.TestCase):
    def test_get_task_with_sufficient_resources(self):
        queue = TaskQueueQueue()
        task1 = Task(1, 10, Resources(2, 2, 0), "Task 1", "")
        task2 = Task(2, 20, Resources(1, 1, 1), "Task 2", "")
        queue.add_task(task1)
        queue.add_task(task2)

        task = queue.get_task(Resources(4, 4, 1))
        self.assertIsNotNone(task)
        self.assertEqual(task.id, 2)  # Expecting task 2 because it has higher priority

    def test_get_task_with_insufficient_resources(self):
        queue = TaskQueueQueue()
        task1 = Task(1, 10, Resources(8, 8, 2), "Task 1", "")
        queue.add_task(task1)

        task = queue.get_task(Resources(4, 4, 1))
        self.assertIsNone(
            task
        )  # None should be returned since available resources are insufficient


if __name__ == "__main__":
    unittest.main()
