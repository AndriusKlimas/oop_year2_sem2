from types import NotImplementedType

class Customers:
    def __init__(self, username, password, email):
        if not Customers.validate_username(username):
            raise ValueError("Username provided is incorrect")
        self._username = username

        if not Customers.validate_password(password):
            raise ValueError("Password provided is incorrect")
        self.__password = password

        if not Customers.validate_email(email):
            raise ValueError("Email provided is incorrect")
        self._email = email


    def __str__(self):
        print(f"get_username(), get_email()")

    def display(self):
        print(f"get_username(), get_email()")


    def __repr__(self):
        print(f"get_username(), get_email(), get_password()")

    def __lt__(self, other: object) -> bool | NotImplementedType:
        if not isinstance(other, Customers):
            return NotImplemented

        return self._username < other._username

    def __gt__ (self, other: object) -> bool | NotImplementedType:
        if not isinstance(other, Customers):
            return NotImplemented

        return self._username > other._username

    def __le__(self, other: object) -> bool | NotImplementedType:
        if not isinstance(other, Customers):
            return NotImplemented

        return self._username <= other._username

    def __ge__(self, other: object) -> bool | NotImplementedType:
        if not isinstance(other, Customers):
            return NotImplemented

        return self._username >= other._username

    def __eq__(self, other: object) -> bool | NotImplementedType:
        if not isinstance(other, Customers):
            return NotImplemented

        return self._username == other._username

    def __ne__(self, other: object) -> bool | NotImplementedType:
        if not isinstance(other, Customers):
            return NotImplemented
        return self._username != other._username

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

        number_check = any(char.isdigit() for char in password)
        if not number_check:
            print("Password must contain at least one number.")
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

if __name__ == '__main__':

    # print("Creating cust 1 (bad password)")
    # cust1 = Customers("michelle", "password", "michelle@password")
    # print(f"cust1: {cust1}")
    # print(f"repr for cust1: {repr(cust1)}")
    # print(f"hash for cust1: {hash(cust1)}")
    # print("")
    #
    # print("Creating cust2 (bad email)")
    # cust2 = Customers("hermione", "Wing4rdium", "hermione_email")
    # print(f"cust2: {cust2}")
    # print(f"repr for cust2: {repr(cust2)}")
    # print(f"hash for cust2: {hash(cust2)}")
    # print("")
    #
    # print("Creating cust3 (bad username)")
    # cust3 = Customers("shorty", "SuperS3cur3", "short@accepted.com")
    # print(f"cust3: {cust3}")
    # print(f"repr for cust3: {repr(cust3)}")
    # print(f"hash for cust3: {hash(cust3)}")
    # print("")
    #
    # print("Creating cust4 (All good!)")
    # cust4 = Customers("valid_username", "Valid passw0rd", "valid_email@emaildomain.com")
    # print(f"cust4: {cust4}")
    # print(f"repr for cust4: {repr(cust4)}")
    # print(f"hash for cust4: {hash(cust4)}")
    # print("")
    #
    # print("Creating cust5 (Values are valid, same username as cust1)")
    # cust5 = Customers("michelle", "Valid passw0rd", "valid_email@emaildomain.com")
    # print(f"cust5: {cust5}")
    # print(f"repr for cust5: {repr(cust5)}")
    # print(f"hash for cust5: {hash(cust5)}")
    # print("")
    #
    # if cust1 != cust2:
    #     print(f"cust1 and cust2 have different usernames (cust1: {cust1.get_username()}, cust2: {cust2.get_username()}), "
    #           f"therefore can't be the same user")
    # else:
    #     print("cust1 and cust2 have the same username - this shouldn't have happened!")
    #
    # if cust1 == cust5:
    #     print(f"cust1 and cust5 have the same username (cust1: {cust1.get_username()}, cust5: {cust5.get_username()}), "
    #           f"therefore are considered the same entity")
    # else:
    #     print("cust1 and cust5 have different usernames - this shouldn't have happened!")
    #
    # # Check where customer is not less than
    # if cust1 < cust2:
    #     print(f"{cust1.get_username()} is less than {cust2.get_username()}")
    # else:
    #     print(f"{cust1.get_username()} is not less than {cust2.get_username()}")
    #
    # # Check where customer is less than
    # if cust1 < cust4:
    #     print(f"{cust1.get_username()} is less than {cust4.get_username()}")
    # else:
    #     print(f"{cust1.get_username()} is not less than {cust2.get_username()}")
    #
    # # Check where customer is not less than because they are equal
    # if cust1 < cust5:
    #     print(f"{cust1.get_username()} is less than {cust5.get_username()}")
    # else:
    #     print(f"{cust1.get_username()} is not less than {cust5.get_username()}")


    try:
        cust10 = Customers("michelle", "Password1", "michelle@password")

    except ValueError as e:
        print(e)

    try:
        customers = Customers("michelle", "password", "")

    except ValueError as e:
        print(e)
