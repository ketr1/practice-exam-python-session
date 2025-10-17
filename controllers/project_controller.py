from models.project import Project

class ProjectController:
    def __init__(self, db_manager):
        self.db_manager = db_manager

    def add_project(self, name, description, start_date, end_date):
        project = Project(name, description, start_date, end_date)
        return self.db_manager.add_project(project)

    def get_project(self, project_id):
        return self.db_manager.get_project_by_id(project_id)

    def get_all_projects(self):
        return self.db_manager.get_all_projects()

    def update_project(self, project_id, **kwargs):
        return self.db_manager.update_project(project_id, **kwargs)

    def delete_project(self, project_id):
        return self.db_manager.delete_project(project_id)

    def update_project_status(self, project_id, new_status):
        project = self.db_manager.get_project_by_id(project_id)
        if project:
            project.update_status(new_status)
            self.db_manager.update_project(project_id, status=project.status)
            return True
        return False

    def get_project_progress(self, project_id):
        project = self.db_manager.get_project_by_id(project_id)
        if not project:
            return 0.0
        return project.get_progress()
