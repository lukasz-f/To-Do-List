from dataclasses import dataclass


@dataclass
class User:
    username: str
    email: str
    password: str
    id: int = 0  # We will automatically generate the new id


class UserManager:
    last_id = 0

    def __init__(self):
        self.users = {}

    def insert_user(self, user):
        self.__class__ .last_id += 1
        user.id = self.__class__.last_id
        self.users[user.id] = user

    def get_by_username(self, username):
        for user in self.users.values():
            if user.username == username:
                return user

    def get_by_email(self, email):
        for user in self.users.values():
            if user.email == email:
                return user


user_manager = UserManager()
user_manager.insert_user(User('user 0', 'user0@gmail.com', '0000'))
user_manager.insert_user(User('user 1', 'user1@gmail.com', '1111'))
