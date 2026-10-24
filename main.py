class Task:
    category = "General"

    def __init__(self, title: str, priority: str = "Normal") -> None:
        self.title = title
        self.priority = priority
        self.completed = False

    def complete(self) -> None:
        self.completed = True

    def rename(self, title: str) -> None:
        self.title = title

    def describe(self) -> str:
        return f'[Completed: {str(self.completed).upper()}]\n\t{self.category}, "{self.priority}" priority task to "{self.title}".'


if __name__ == "__main__":
    task = Task("Study Python")
    print(task.describe())
    task.complete()
    print(task.describe())
    task.rename("Train an AI")
    print(task.describe())
