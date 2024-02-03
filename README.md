# TaskQueue
Implementations of the task queue with priorities and resource limits

* Each task has a priority and the required amount of resources to process it.
* Publishers create tasks with specified resource limits, and put them in a task queue.
* Consumer receives the highest priority task that satisfies available resources.
* The queue is expected to contain thousands of tasks.
* Write a unit test to demonstrate the operation of the queue.


## Requirements

* Python 3.6+

## Run tests

```sh
python3 test_queue.py
```
