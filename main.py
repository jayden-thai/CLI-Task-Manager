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
        normalized_key = keyword.casefold()
        return [
            task
            for task in self.tasks
            if normalized_key in task.title.casefold()
            or any(normalized_key == tag.casefold() for tag in task.tags)
        ]

    def complete_task(self, index: int) -> None:
        self.tasks[index].complete()


def main() -> None:
    manager = TaskManager()
    print("Welcome to Task Manager!")
    print("Commands: add, list, pending, search, complete, quit")

    while True:
        user_input = input("> ")
        command, _, argument = user_input.strip().partition(" ")
        command = command.casefold()
        argument = argument.strip()

        if command == "add":
            if not argument:
                print("Invalid title argument.")
            else:
                new_task = Task(argument)
                manager.add_task(new_task)
                print(f"Added task: {new_task.title}")

        elif command == "list":
            tasks = manager.get_all_tasks()
            if not tasks:
                print("No tasks stored.")
            else:
                for index, task in enumerate(tasks, start=1):
                    print(
                        f"{index}. {task.tags} {task.title}\n\tpriority: {task.priority}\n\tcompleted: {task.completed}"
                    )

        elif command == "pending":
            pending_tasks = [
                (index, task)
                for index, task in enumerate(manager.get_all_tasks(), start=1)
                if not task.completed
            ]
            if not pending_tasks:
                print("No unfinished tasks remaining.")
            else:
                for index, task in pending_tasks:
                    print(
                        f"{index}. {task.tags} {task.title}\n\tpriority: {task.priority}\n\tcompleted: {task.completed}"
                    )

        elif command == "search":
            results = manager.search_tasks(argument)

            if not argument:
                print("Please enter a search keyword.")
            elif results:
                print("\nResults:\n")
                for index, task in enumerate(manager.get_all_tasks(), start=1):
                    if task in results:
                        print(
                            f"{index}. {task.tags} {task.title}\n\tpriority: {task.priority}\n\tcompleted: {task.completed}"
                        )
            else:
                print("No results.")

        elif command == "complete":
            tasks = manager.get_all_tasks()
            try:
                index = int(argument) - 1
                if not tasks:
                    print("No tasks stored.")
                elif not 0 <= index < len(tasks):
                    print(f"Task {argument} does not exist in {len(tasks)} task(s).")
                elif tasks[index].completed:
                    print(
                        f"Task {argument}: {tasks[index].title} is already marked completed."
                    )
                else:
                    manager.complete_task(index)
                    print(f"Completed task {argument}: {tasks[index].title}")
            except ValueError:
                print("Please enter a valid integer.")

        elif command == "quit":
            return

        else:
            print(f'Command "{command}" unrecognized.')
            print("Commands: add, list, pending, search, complete, quit")


if __name__ == "__main__":
    main()
