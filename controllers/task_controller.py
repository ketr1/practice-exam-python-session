from models.task import Task

class TaskController:
    def __init__(self, db_manager) -> None:
        pass

    def add_task(self, title, description, priority, due_date, project_id, assignee_id) -> int:
        pass

    def get_task(self, task_id) -> Task | None:
        pass

    def get_all_tasks(self) -> list[Task]:
        pass

    def update_task(self, task_id, **kwargs) -> bool:
        pass

    def delete_task(self, task_id) -> bool:
        pass

    def search_tasks(self, query) -> list[Task]:
        pass

    def update_task_status(self, task_id, new_status) -> bool:
        pass

    def get_overdue_tasks(self) -> list[Task]:
        pass

    def get_tasks_by_project(self, project_id) -> list[Task]:
        pass

    def get_tasks_by_user(self, user_id) -> list[Task]:
        pass