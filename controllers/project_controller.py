from models.project import Project

class ProjectController:
    def __init__(self, db_manager) -> None:
        pass

    def add_project(self, name, description, start_date, end_date) -> int:
        pass

    def get_project(self, project_id) -> Project | None:
        pass

    def get_all_projects(self) -> list[Project]:
        pass

    def update_project(self, project_id, **kwargs) -> bool:
        pass

    def delete_project(self, project_id) -> bool:
        pass

    def update_project_status(self, project_id, new_status) -> bool:
        pass

    def get_project_progress(self, project_id) -> float:
        pass