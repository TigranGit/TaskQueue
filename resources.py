from dataclasses import dataclass


@dataclass(order=True)
class Resources:
    ram: int
    cpu_cores: int
    gpu_count: int
