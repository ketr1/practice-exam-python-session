from datetime import datetime


class Task:
    def __init__(self, title, description, priority, due_date, project_id, assignee_id, status="pending"):
        self.title = title
        self.description = description
        self.priority = priority
        self.status = status
        self.due_date = due_date
        self.project_id = project_id
        self.assignee_id = assignee_id
        self.id = None


    def update_status(self, new_status) -> bool:

        valid_statuses = {"pending", "in_progress", "completed"}
        if new_status in valid_statuses:
            self.status = new_status
            return True
        return False

    def is_overdue(self) -> bool:

        if self.status != "completed" and isinstance(self.due_date, datetime):
            return datetime.now() > self.due_date
        return False

    def to_dict(self) -> dict:

        return {
            "id": self.id,
            "title": self.title,
            "description": self.description,
            "priority": self.priority,
            "status": self.status,
            "due_date": self.due_date.isoformat() if isinstance(self.due_date, datetime) else self.due_date,
            "project_id": self.project_id,
            "assignee_id": self.assignee_id
        }
