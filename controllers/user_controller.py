from models.user import User

class UserController:
    def __init__(self, db_manager):
        self.db_manager = db_manager

    def add_user(self, username, email, role):
        user = User(username, email, role)
        return self.db_manager.add_user(user)

    def get_user(self, user_id):
        return self.db_manager.get_user_by_id(user_id)

    def get_all_users(self):
        return self.db_manager.get_all_users()

    def update_user(self, user_id, **kwargs):
        return self.db_manager.update_user(user_id, **kwargs)

    def delete_user(self, user_id):
        return self.db_manager.delete_user(user_id)

    def get_user_tasks(self, user_id):
        return self.db_manager.get_tasks_by_user(user_id)
