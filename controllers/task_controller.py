from models.task import Task


class TaskController:
    def __init__(self, db_manager):
        self.db_manager = db_manager

    def add_task(self, title, description, priority, deadline, project_id, user_id):
        return self.db_manager.add_task(Task(title, description, priority, deadline, project_id, user_id))

    def get_task(self, task_id):
        return self.db_manager.get_task_by_id(task_id)

    def get_all_tasks(self):
        return self.db_manager.get_all_tasks()

    def update_task(self, task_id, **kwargs):
        return self.db_manager.update_task(task_id, **kwargs)

    def delete_task(self, task_id):
        return self.db_manager.delete_task(task_id)

    def search_tasks(self, keyword):
        return self.db_manager.search_tasks(keyword)

    def get_tasks_by_user(self, user_id):
        return self.db_manager.get_tasks_by_user(user_id)

    def get_overdue_tasks(self):
        return self.db_manager.get_overdue_tasks()

    def update_task_status(self, task_id, new_status):
        task = self.db_manager.get_task_by_id(task_id)
        if task:
            task.update_status(new_status)
            self.db_manager.update_task(task_id, status=task.status)
            return True
        return False

    def get_tasks_by_project(self, project_id):
        return self.db_manager.get_tasks_by_project(project_id)
