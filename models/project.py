from datetime import datetime

class Project:
    def __init__(self, name, description, start_date, end_date, status="active"):
        self.name = name
        self.description = description
        self.start_date = start_date
        self.end_date = end_date
        self.status = status
        self.id = None

    def update_status(self, new_status) -> bool:
        valid_statuses = {"active", "completed", "on_hold"}
        if new_status in valid_statuses:
            self.status = new_status
            return True
        return False

    def get_progress(self) -> float:
        return 100.0 if self.status == "completed" else 50.0 if self.status == "on_hold" else 0.0

    def to_dict(self) -> dict:
        return {
            "id": self.id,
            "name": self.name,
            "description": self.description,
            "start_date": self.start_date,
            "end_date": self.end_date,
            "status": self.status
        }
