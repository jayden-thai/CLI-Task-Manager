from dataclasses import dataclass, field
from typing import ClassVar


@dataclass
class Task:
    title: str
    priority: str = "Normal"
    category: ClassVar[str] = "General"
    completed: bool = False
    tags: list[str] = field(default_factory=list[str])

    def complete(self) -> None:
        self.completed = True

    def rename(self, title: str) -> None:
        self.title = title

    def add_tag(self, tag: str) -> None:
        self.tags.append(tag)

    def describe(self) -> str:
        return f'[Completed: {str(self.completed).upper()}]\n\t{self.category}, "{self.priority}" priority task to "{self.title}".\n\tTags: {self.tags}'


class TaskManager:
    def __init__(self) -> None:
        self.tasks: list[Task] = []

    def add_task(self, task: Task) -> None:
        self.tasks.append(task)

    def get_all_tasks(self) -> list[Task]:
        return self.tasks.copy()

    def get_pending_tasks(self) -> list[Task]:
        return [task for task in self.tasks if not task.completed]

    def search_tasks(self, keyword: str) -> list[Task]:
        normalizedKey = keyword.casefold()
        return [
            task
            for task in self.tasks
            if normalizedKey in task.title.casefold()
            or any(normalizedKey == tag.casefold() for tag in task.tags)
        ]

    def complete_task(self, index: int) -> None:
        self.tasks[index].complete()


if __name__ == "__main__":
    manager = TaskManager()

    manager.add_task(Task("Study Python", "High"))
    manager.add_task(Task("Finish Java assignment"))
    manager.add_task(Task("Practice Python OOP"))

    manager.complete_task(0)

    print(len(manager.get_all_tasks()))  # 3
    print(len(manager.get_pending_tasks()))  # 2
    print(len(manager.search_tasks("PYTHON")))  # 2

    task = Task("Buy groceries")
    task.add_tag("Important")
    manager.add_task(task)

    results = manager.search_tasks("IMPORTANT")

    print(len(results))  # 1
    print(results[0].title)  # Buy groceries
