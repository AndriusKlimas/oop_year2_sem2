class Customers:
    def __init__(self, username, password, email):
        if not Customers.validate_username(username):
            print("Username provided is incorrect")
        self._username = username

        if not Customers.validate_password(password):
            print("Password provided is incorrect")
        self.__password = password

        if not Customers.validate_email(email):
            print("Email provided is incorrect")
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


    #username validation method
    @staticmethod
    def validate_username(username):
        if username is None:
            return False
        if len(username.strip()) < 8:
            return False
        return True



    #password validation method
    @staticmethod
    def validate_password(password):
        #If the password is None, return False
        if password is None:
            return False
        #If the password length is less than 8, return False
        if len(password.strip()) < 8:
            return False

        # Check for at least one uppercase and one lowercase letter
        #If any character in the password is uppercase, set upper to true, do same for lower
        upper_check = any(char.isupper() for char in password)
        if not upper_check:
            print("Password must contain at least one uppercase letter.")
            return False

        lower_check = any(char.islower() for char in password)
        if not lower_check:
            print("Password must contain at least one lowercase letter.")
            return False

        return True

    #email validation method
    @staticmethod
    def validate_email(email):
        if email is None:
            return False
        if "@" not in email or "." not in email:
            return False
        return True