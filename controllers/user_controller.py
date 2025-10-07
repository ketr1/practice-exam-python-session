from models.user import User

class UserController:
    def __init__(self, db_manager) -> None:
        pass

    def add_user(self, username, email, role) -> int:
        pass

    def get_user(self, user_id) -> User | None:
        pass

    def get_all_users(self) -> list[User]:
        pass

    def update_user(self, user_id, **kwargs) -> bool:
        pass

    def delete_user(self, user_id) -> bool:
        pass

    def get_user_tasks(self, user_id) -> list:
        pass