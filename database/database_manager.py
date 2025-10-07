import sqlite3
from models.task import Task
from models.project import Project
from models.user import User
from datetime import datetime

class DatabaseManager:
    def __init__(self, db_path="tasks.db") -> None:
        pass

    def close(self) -> None:
        pass

    def create_tables(self) -> None:
        pass

    def add_task(self, task: Task) -> int:
        pass

    def get_task_by_id(self, task_id) -> Task | None:
        pass

    def get_all_tasks(self) -> list[Task]:
        pass

    def update_task(self, task_id, **kwargs) -> bool:
        pass

    def delete_task(self, task_id) -> bool:
        pass

    def search_tasks(self, query) -> list[Task]:
        pass

    def get_tasks_by_project(self, project_id) -> list[Task]:
        pass

    def get_tasks_by_user(self, user_id) -> list[Task]:
        pass

    def add_project(self, project: Project) -> int:
        pass

    def get_project_by_id(self, project_id) -> Project | None:
        pass

    def get_all_projects(self) -> list[Project]:
        pass

    def update_project(self, project_id, **kwargs) -> bool:
        pass

    def delete_project(self, project_id) -> bool:
        pass

    def add_user(self, user: User) -> int:
        pass

    def get_user_by_id(self, user_id) -> User | None:
        pass

    def get_all_users(self) -> list[User]:
        pass

    def update_user(self, user_id, **kwargs) -> bool:
        pass

    def delete_user(self, user_id) -> bool:
        pass