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


if __name__ == "__main__":
    task1 = Task("Study Python")
    task2 = Task("Study Java", "High")

    task1.add_tag("programming")
    task1.add_tag("python")

    print(task1.tags)
    # ['programming', 'python']

    print(task2.tags)
    # []

    task1.complete()
    print(task1.describe())
    # Your existing formatted description
