class Customers:
    def __init__(self, username, password, email):
        self._username = username
        self.__password = password
        self._email = email


    def __str__(self):
        print(f"get_username(), get_email()")

    def display(self):
        print(f"get_username(), get_email()")

    def __repr__(self):
        print(f"get_username(), get_email(), get_password()")


#better practices for encapsulation
    def get_password(self):
        return self.__password

    def get_email(self):
        return self._email

    def get_username(self):
        return self._username