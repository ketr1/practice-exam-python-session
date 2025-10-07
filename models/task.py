from datetime import datetime

class Task:
    def __init__(self, title, description, priority, due_date, project_id, assignee_id) -> None:
        pass

    def update_status(self, new_status) -> bool:
        pass

    def is_overdue(self) -> bool:
        pass

    def to_dict(self) -> dict:
        pass