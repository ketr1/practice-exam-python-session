import sys
import os
import tempfile
from datetime import datetime, timedelta

# Добавляем корень проекта в sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))


from controllers.user_controller import UserController
from controllers.user_controller import UserController
from database.database_manager import DatabaseManager
from models.project import Project
from models.user import User
from controllers.project_controller import ProjectController
from controllers.task_controller import TaskController



class TestUserController:
    """Тесты для UserController"""

    def setup_method(self):
        """Настройка перед каждым тестом"""
        import tempfile
        import os
        from datetime import datetime, timedelta
        from models.project import Project
        from models.user import User
        from database.database_manager import DatabaseManager
        from controllers.task_controller import TaskController

        temp_dir = tempfile.gettempdir()
        self.temp_db_path = os.path.join(temp_dir, "test_temp.db")
        self.db_manager = DatabaseManager(self.temp_db_path)
        self.db_manager.create_tables()
        self.controller = UserController(self.db_manager)

        # Создаем тестовые проекты и пользователей
        self.project_id = self.db_manager.add_project(
            Project("Тестовый проект", "Описание проекта", datetime.now(), datetime.now() + timedelta(days=30))
        )
        self.user_id = self.db_manager.add_user(
            User("test_user", "test@example.com", "developer")
        )

    def teardown_method(self):
        self.db_manager.close()
        import os
        if os.path.exists(self.temp_db_path):
            os.unlink(self.temp_db_path)

    def test_add_user(self):
        """Тест добавления пользователя"""
        user_id = self.controller.add_user(
            "new_user",
            "new_user@example.com",
            "developer"
        )

        assert user_id is not None
        assert isinstance(user_id, int)

        # Проверяем, что пользователь действительно добавлен
        user = self.controller.get_user(user_id)
        assert user.username == "new_user"
        assert user.email == "new_user@example.com"
        assert user.role == "developer"

    def test_get_user(self):
        """Тест получения пользователя по ID"""
        user_id = self.controller.add_user(
            "user_for_get",
            "user@example.com",
            "manager"
        )

        user = self.controller.get_user(user_id)
        assert user is not None
        assert user.username == "user_for_get"
        assert user.role == "manager"

    def test_get_all_users(self):
        """Тест получения всех пользователей"""
        # Добавляем несколько пользователей
        self.controller.add_user("user1", "user1@example.com", "developer")
        self.controller.add_user("user2", "user2@example.com", "manager")

        users = self.controller.get_all_users()
        assert len(users) >= 2

        # Проверяем, что все пользователи имеют необходимые атрибуты
        for user in users:
            assert hasattr(user, "id")
            assert hasattr(user, "username")
            assert hasattr(user, "role")

    def test_update_user(self):
        """Тест обновления пользователя"""
        user_id = self.controller.add_user(
            "old_username",
            "old@example.com",
            "developer"
        )

        # Обновляем пользователя
        self.controller.update_user(
            user_id,
            username="new_username",
            email="new@example.com",
            role="manager"
        )

        # Проверяем изменения
        user = self.controller.get_user(user_id)
        assert user.username == "new_username"
        assert user.email == "new@example.com"
        assert user.role == "manager"

    def test_delete_user(self):
        """Тест удаления пользователя"""
        user_id = self.controller.add_user(
            "user_for_delete",
            "delete@example.com",
            "developer"
        )

        # Удаляем пользователя
        self.controller.delete_user(user_id)

        # Проверяем, что пользователь удален
        user = self.controller.get_user(user_id)
        assert user is None

    def test_get_user_tasks(self):
        """Тест получения задач пользователя"""
        user_id = self.controller.add_user("task_user", "task@example.com", "developer")

        # Создаем проект и задачи
        project_controller = ProjectController(self.db_manager)
        project_id = project_controller.add_project(
            "Проект для задач", "Описание", datetime.now(), datetime.now() + timedelta(days=10)
        )

        task_controller = TaskController(self.db_manager)
        task_controller.add_task("Задача 1", "Описание", 1, datetime.now() + timedelta(days=1), project_id, user_id)
        task_controller.add_task("Задача 2", "Описание", 1, datetime.now() + timedelta(days=1), project_id, user_id)

        tasks = self.controller.get_user_tasks(user_id)
        assert isinstance(tasks, list)
        assert len(tasks) >= 2

        for task in tasks:
            assert task.assignee_id == user_id
