class Customers:
    def __init__(self, username, password, email):
        self._username = username
        self.__password = password
        self._email = email


    def __str__(self):
        print(f"self.username, self.email")

    def display(self):
        print(f"self.username, self.email")

    def __repr__(self):
        print(f"self.username, self.email, self.__password")

    def get_password(self):
        return self.__password

    def get_email(self):
        return self._email

    def get_username(self):
        return self._username