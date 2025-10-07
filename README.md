## **Задание для доп сессии**
**Описание проекта**
Вам необходимо реализовать **Систему управления задачами** с использованием архитектуры MVC, SQL базы данных и автотестов.

**Технологии**
- Python 3.8+
- SQLite (встроенная база данных)
- pytest (для автотестов)
- tkinter (для GUI)

**Структура проекта**
```
task_system/
├── models/
│   ├── __init__.py
│   ├── task.py
│   ├── project.py
│   └── user.py
├── views/
│   ├── __init__.py
│   ├── main_window.py
│   ├── task_view.py
│   ├── project_view.py
│   └── user_view.py
├── controllers/
│   ├── __init__.py
│   ├── task_controller.py
│   ├── project_controller.py
│   └── user_controller.py
├── database/
│   ├── __init__.py
│   ├── database_manager.py
│   └── tasks.db
├── tests/
│   ├── __init__.py
│   ├── test_models.py
│   ├── test_controllers.py
│   └── test_database.py
├── main.py
├── requirements.txt
└── README.md
```

---

### **Задание 1: Модели (Models)**

#### **1.1 Класс Task (models/task.py)**
Создайте класс Task со следующими атрибутами и методами:

**Атрибуты:**
- `id` (int) - уникальный идентификатор
- `title` (str) - название задачи
- `description` (str) - описание задачи
- `priority` (int) - приоритет (1-высокий, 2-средний, 3-низкий)
- `status` (str) - статус ('pending', 'in_progress', 'completed')
- `due_date` (datetime) - срок выполнения
- `project_id` (int) - ID проекта
- `assignee_id` (int) - ID исполнителя

**Методы:**
- `__init__(self, title, description, priority, due_date, project_id, assignee_id)`
- `update_status(self, new_status)` - обновить статус задачи
- `is_overdue(self)` - проверить просрочку
- `to_dict(self)` - вернуть словарь с данными задачи

#### **1.2 Класс Project (models/project.py)**
Создайте класс Project со следующими атрибутами и методами:

**Атрибуты:**
- `id` (int) - уникальный идентификатор
- `name` (str) - название проекта
- `description` (str) - описание проекта
- `start_date` (datetime) - дата начала
- `end_date` (datetime) - дата окончания
- `status` (str) - статус ('active', 'completed', 'on_hold')

**Методы:**
- `__init__(self, name, description, start_date, end_date)`
- `update_status(self, new_status)` - обновить статус проекта
- `get_progress(self)` - рассчитать прогресс выполнения
- `to_dict(self)` - вернуть словарь с данными проекта

#### **1.3 Класс User (models/user.py)**
Создайте класс User со следующими атрибутами и методами:

**Атрибуты:**
- `id` (int) - уникальный идентификатор
- `username` (str) - имя пользователя
- `email` (str) - email
- `role` (str) - роль ('admin', 'manager', 'developer')
- `registration_date` (datetime) - дата регистрации

**Методы:**
- `__init__(self, username, email, role)`
- `update_info(self, username=None, email=None, role=None)`
- `to_dict(self)` - вернуть словарь с данными пользователя

---

### **Задание 2: База данных (SQL CRUD операции)**

#### **2.1 DatabaseManager (database/database_manager.py)**
Создайте класс DatabaseManager для работы с SQLite базой данных:

**Методы для работы с задачами:**
- `create_task_table(self)` - создать таблицу задач
- `add_task(self, task)` - добавить задачу
- `get_task_by_id(self, task_id)` - получить задачу по ID
- `get_all_tasks(self)` - получить все задачи
- `update_task(self, task_id, **kwargs)` - обновить задачу
- `delete_task(self, task_id)` - удалить задачу
- `search_tasks(self, query)` - поиск задач по названию/описанию
- `get_tasks_by_project(self, project_id)` - получить задачи проекта
- `get_tasks_by_user(self, user_id)` - получить задачи пользователя

**Методы для работы с проектами:**
- `create_project_table(self)` - создать таблицу проектов
- `add_project(self, project)` - добавить проект
- `get_project_by_id(self, project_id)` - получить проект по ID
- `get_all_projects(self)` - получить все проекты
- `update_project(self, project_id, **kwargs)` - обновить проект
- `delete_project(self, project_id)` - удалить проект

**Методы для работы с пользователями:**
- `create_user_table(self)` - создать таблицу пользователей
- `add_user(self, user)` - добавить пользователя
- `get_user_by_id(self, user_id)` - получить пользователя по ID
- `get_all_users(self)` - получить всех пользователей
- `update_user(self, user_id, **kwargs)` - обновить пользователя
- `delete_user(self, user_id)` - удалить пользователя

---

### **Задание 3: Контроллеры (Controllers)**

#### **3.1 TaskController (controllers/task_controller.py)**
Создайте класс TaskController:

**Методы:**
- `add_task(self, title, description, priority, due_date, project_id, assignee_id)` - добавить задачу
- `get_task(self, task_id)` - получить задачу
- `get_all_tasks(self)` - получить все задачи
- `update_task(self, task_id, **kwargs)` - обновить задачу
- `delete_task(self, task_id)` - удалить задачу
- `search_tasks(self, query)` - поиск задач
- `update_task_status(self, task_id, new_status)` - обновить статус задачи
- `get_overdue_tasks(self)` - получить просроченные задачи
- `get_tasks_by_project(self, project_id)` - получить задачи проекта
- `get_tasks_by_user(self, user_id)` - получить задачи пользователя

#### **3.2 ProjectController (controllers/project_controller.py)**
Создайте класс ProjectController:

**Методы:**
- `add_project(self, name, description, start_date, end_date)` - добавить проект
- `get_project(self, project_id)` - получить проект
- `get_all_projects(self)` - получить все проекты
- `update_project(self, project_id, **kwargs)` - обновить проект
- `delete_project(self, project_id)` - удалить проект
- `update_project_status(self, project_id, new_status)` - обновить статус проекта
- `get_project_progress(self, project_id)` - получить прогресс проекта

#### **3.3 UserController (controllers/user_controller.py)**
Создайте класс UserController:

**Методы:**
- `add_user(self, username, email, role)` - добавить пользователя
- `get_user(self, user_id)` - получить пользователя
- `get_all_users(self)` - получить всех пользователей
- `update_user(self, user_id, **kwargs)` - обновить пользователя
- `delete_user(self, user_id)` - удалить пользователя
- `get_user_tasks(self, user_id)` - получить задачи пользователя

---

### **Задание 4: Представления (Views) - GUI**

#### **4.1 MainWindow (views/main_window.py)**
Создайте главное окно приложения с меню и вкладками для:
- Управления задачами
- Управления проектами
- Управления пользователями

#### **4.2 TaskView (views/task_view.py)**
Создайте интерфейс для управления задачами:
- Форма добавления/редактирования задачи
- Таблица со списком задач
- Поиск по задачам
- Фильтрация по статусу/приоритету

#### **4.3 ProjectView (views/project_view.py)**
Создайте интерфейс для управления проектами:
- Форма добавления/редактирования проекта
- Таблица со списком проектов
- Просмотр задач проекта
- Прогресс выполнения

#### **4.4 UserView (views/user_view.py)**
Создайте интерфейс для управления пользователями:
- Форма добавления/редактирования пользователя
- Таблица со списком пользователей
- Просмотр задач пользователя

---

### **Задание 5: Автотесты**

#### **5.1 Тесты моделей (tests/test_models.py)**
Напишите тесты для всех классов моделей:
- Тестирование создания объектов
- Тестирование методов классов
- Тестирование валидации данных
- Тестирование граничных случаев

#### **5.2 Тесты контроллеров (tests/test_controllers.py)**
Напишите тесты для всех контроллеров:
- Тестирование CRUD операций
- Тестирование бизнес-логики
- Тестирование обработки ошибок

#### **5.3 Тесты базы данных (tests/test_database.py)**
Напишите тесты для работы с базой данных:
- Тестирование создания таблиц
- Тестирование SQL операций
- Тестирование целостности данных

---

### **Важно для тестирования и архитектуры**

- Все контроллеры должны принимать объект DatabaseManager в конструктор
- Для тестирования используйте временную базу данных
- После каждого теста закрывайте соединение с базой

**Пример инициализации для теста:**
```python
import tempfile
import os
from database.database_manager import DatabaseManager
from controllers.task_controller import TaskController

class TestTaskController:
    def setup_method(self):
        self.temp_db = tempfile.NamedTemporaryFile(delete=False, suffix='.db')
        self.db_manager = DatabaseManager(self.temp_db.name)
        self.controller = TaskController(self.db_manager)

    def teardown_method(self):
        self.db_manager.close()
        os.unlink(self.temp_db.name)
```

---

### **Требования к реализации**
- **Архитектура MVC**: Строгое разделение на Model, View, Controller
- **SQL операции**: Использование SQLite с правильными SQL запросами
- **Обработка ошибок**: Корректная обработка исключений
- **Валидация данных**: Проверка входных данных
- **Документация**: Комментарии к коду и docstrings
- **Автотесты**: Покрытие тестами не менее 80% кода

### **Критерии оценки**
- **MVC архитектура (30%)**: Правильное разделение ответственности
- **SQL операции (30%)**: Корректная работа с базой данных
- **Работа с ORM (30%)**: Функциональный и удобный интерфейс
- **Код (10%)**: Чистота кода

**ВАЖНО: УКАЗАННАЯ СТРУКТУРА (КЛАССЫ, ФУНКЦИИ, ИХ МЕТОДЫ И АРГУМЕНТЫ) ДОЛЖНЫ БЫТЬ НЕИЗМЕННЫ, ВЫ ДОПИСЫВАЕТЕ ТОЛЬКО ТЕЛО МЕТОДОВ И КЛАССОВ**