import sqlite3
from models.task import Task
from models.project import Project
from models.user import User
from datetime import datetime


class DatabaseManager:
    def __init__(self, db_path):
        self.conn = sqlite3.connect(db_path)
        self.conn.row_factory = sqlite3.Row
        self.cursor = self.conn.cursor()


    def close(self) -> None:
        try:
            if hasattr(self, "cursor") and self.cursor:
                try:
                    self.cursor.close()
                except Exception:
                    pass
            if hasattr(self, "conn") and self.conn:
                try:
                    self.conn.commit()
                    self.conn.close()
                except Exception:
                    pass
            time.sleep(0.05)
        except Exception:
            pass

    # ---------- CREATE TABLES ----------
    def create_tables(self) -> None:
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT NOT NULL,
                email TEXT NOT NULL,
                role TEXT NOT NULL,
                registration_date TEXT NOT NULL
            )
        """)

        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS projects (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                description TEXT,
                start_date TEXT,
                end_date TEXT,
                status TEXT
            )
        """)

        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS tasks (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT NOT NULL,
                description TEXT,
                priority INTEGER,
                status TEXT,
                due_date TEXT,
                project_id INTEGER,
                assignee_id INTEGER
            )
        """)

        self.conn.commit()

    # ---------- TASKS ----------
    def add_task(self, task: Task) -> int:
        self.cursor.execute("""
            INSERT INTO tasks (title, description, priority, status, due_date, project_id, assignee_id)
            VALUES (?, ?, ?, ?, ?, ?, ?)
        """, (task.title, task.description, task.priority, task.status,
              task.due_date.isoformat() if isinstance(task.due_date, datetime) else task.due_date,
              task.project_id, task.assignee_id))
        self.conn.commit()
        return self.cursor.lastrowid

    def get_task_by_id(self, task_id) -> Task | None:
        self.cursor.execute("SELECT * FROM tasks WHERE id = ?", (task_id,))
        row = self.cursor.fetchone()
        if not row:
            return None
        task = Task(row["title"], row["description"], row["priority"],
                    datetime.fromisoformat(row["due_date"]) if row["due_date"] else None,
                    row["project_id"], row["assignee_id"])
        task.id = row["id"]
        task.status = row["status"]
        return task

    def get_all_tasks(self) -> list[Task]:
        self.cursor.execute("SELECT * FROM tasks")
        rows = self.cursor.fetchall()
        return [self.get_task_by_id(row["id"]) for row in rows]

    def update_task(self, task_id, **kwargs) -> bool:
        if not kwargs:
            return False
        fields = ", ".join(f"{key} = ?" for key in kwargs)
        values = list(kwargs.values()) + [task_id]
        self.cursor.execute(f"UPDATE tasks SET {fields} WHERE id = ?", values)
        self.conn.commit()
        return self.cursor.rowcount > 0

    def delete_task(self, task_id) -> bool:
        self.cursor.execute("DELETE FROM tasks WHERE id = ?", (task_id,))
        self.conn.commit()
        return self.cursor.rowcount > 0

    def search_tasks(self, query) -> list[Task]:
        like_query = f"%{query}%"
        self.cursor.execute("""
            SELECT * FROM tasks WHERE title LIKE ? OR description LIKE ?
        """, (like_query, like_query))
        rows = self.cursor.fetchall()
        return [self.get_task_by_id(row["id"]) for row in rows]

    def get_tasks_by_project(self, project_id) -> list[Task]:
        self.cursor.execute("SELECT * FROM tasks WHERE project_id = ?", (project_id,))
        rows = self.cursor.fetchall()
        return [self.get_task_by_id(row["id"]) for row in rows]

    def get_tasks_by_user(self, user_id) -> list[Task]:
        self.cursor.execute("SELECT * FROM tasks WHERE assignee_id = ?", (user_id,))
        rows = self.cursor.fetchall()
        return [self.get_task_by_id(row["id"]) for row in rows]
    
    def get_overdue_tasks(self) -> list[Task]:
        """Возвращает список просроченных задач (у которых due_date < текущей даты и статус != 'completed')"""
        now = datetime.now().isoformat()
        self.cursor.execute(
            "SELECT * FROM tasks WHERE due_date < ? AND status != 'completed'", (now,)
        )
        rows = self.cursor.fetchall()
        return [self.get_task_by_id(row["id"]) for row in rows]

    # ---------- PROJECTS ----------
    def add_project(self, project: Project) -> int:
        self.cursor.execute("""
            INSERT INTO projects (name, description, start_date, end_date, status)
            VALUES (?, ?, ?, ?, ?)
        """, (project.name, project.description,
              project.start_date.isoformat() if isinstance(project.start_date, datetime) else project.start_date,
              project.end_date.isoformat() if isinstance(project.end_date, datetime) else project.end_date,
              project.status))
        self.conn.commit()
        return self.cursor.lastrowid

    def get_project_by_id(self, project_id) -> Project | None:
        self.cursor.execute("SELECT * FROM projects WHERE id = ?", (project_id,))
        row = self.cursor.fetchone()
        if not row:
            return None
        project = Project(row["name"], row["description"],
                          datetime.fromisoformat(row["start_date"]) if row["start_date"] else None,
                          datetime.fromisoformat(row["end_date"]) if row["end_date"] else None)
        project.id = row["id"]
        project.status = row["status"]
        return project

    def get_all_projects(self) -> list[Project]:
        self.cursor.execute("SELECT * FROM projects")
        rows = self.cursor.fetchall()
        return [self.get_project_by_id(row["id"]) for row in rows]

    def update_project(self, project_id, **kwargs) -> bool:
        if not kwargs:
            return False
        fields = ", ".join(f"{key} = ?" for key in kwargs)
        values = list(kwargs.values()) + [project_id]
        self.cursor.execute(f"UPDATE projects SET {fields} WHERE id = ?", values)
        self.conn.commit()
        return self.cursor.rowcount > 0

    def delete_project(self, project_id) -> bool:
        self.cursor.execute("DELETE FROM projects WHERE id = ?", (project_id,))
        self.conn.commit()
        return self.cursor.rowcount > 0

    # ---------- USERS ----------
    def add_user(self, user: User) -> int:
        self.cursor.execute("""
            INSERT INTO users (username, email, role, registration_date)
            VALUES (?, ?, ?, ?)
        """, (user.username, user.email, user.role,
              user.registration_date.isoformat() if hasattr(user, "registration_date") else datetime.now().isoformat()))
        self.conn.commit()
        return self.cursor.lastrowid

    def get_user_by_id(self, user_id) -> User | None:
        self.cursor.execute("SELECT * FROM users WHERE id = ?", (user_id,))
        row = self.cursor.fetchone()
        if not row:
            return None
        user = User(row["username"], row["email"], row["role"])
        user.id = row["id"]
        return user

    def get_all_users(self) -> list[User]:
        self.cursor.execute("SELECT * FROM users")
        rows = self.cursor.fetchall()
        return [self.get_user_by_id(row["id"]) for row in rows]

    def update_user(self, user_id, **kwargs) -> bool:
        if not kwargs:
            return False
        fields = ", ".join(f"{key} = ?" for key in kwargs)
        values = list(kwargs.values()) + [user_id]
        self.cursor.execute(f"UPDATE users SET {fields} WHERE id = ?", values)
        self.conn.commit()
        return self.cursor.rowcount > 0

    def delete_user(self, user_id) -> bool:
        self.cursor.execute("DELETE FROM users WHERE id = ?", (user_id,))
        self.conn.commit()
        return self.cursor.rowcount > 0

