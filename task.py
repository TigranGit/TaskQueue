from dataclasses import dataclass

from resources import Resources


@dataclass(order=True)
class Task:
    id: int
    priority: int
    resources: Resources
    content: str
    result: str
