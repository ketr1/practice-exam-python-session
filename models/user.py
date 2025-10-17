from datetime import datetime
import re

class User:
    def __init__(self, username, email, role) -> None:
        self.username = username
        self.email = email
        self.role = role
        self.registration_date = datetime.now()

    def _is_valid_email(self, email) -> bool:
        return re.match(r"[^@]+@[^@]+\.[^@]+", email) is not None

    def update_info(self, username=None, email=None, role=None) -> None:
        if username:
            self.username = username
        if email and self._is_valid_email(email):
            self.email = email
        if role:
            self.role = role

    def to_dict(self) -> dict:
        return {
            "username": self.username,
            "email": self.email,
            "role": self.role,
            "registration_date": self.registration_date
        }
