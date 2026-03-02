class UserManager:
    def __init__(self):
        self.users = []

    def add_user(self, username: str):
        if not username:
            raise ValueError("Le nom d'utilisateur est obligatoire")
        if username in self.users:
            raise ValueError("Utilisateur déjà existant")
        self.users.append(username)

    def remove_user(self, username: str):
        if username not in self.users:
            raise ValueError("Utilisateur introuvable")
        self.users.remove(username)

    def count_users(self) -> int:
        return len(self.users)


def count_total_users(users) -> int:
    return len(users)
