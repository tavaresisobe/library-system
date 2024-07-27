class UserRepo:
    def __init__(self):
        self.users = []

    def add_user(self, user):
        self.users.append(user)
        return user.ra

    def remove_user(self, user_id):
        pass