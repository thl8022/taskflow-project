from dataclasses import dataclass


@dataclass
class Task:
    id: int = None
    title: str = ""
    description: str = ""
    priority: str = "Média"
    status: str = "Pendente"