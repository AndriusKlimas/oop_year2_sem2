import json
from ex_e_class import User

if __name__ == "__main__":
    with open("excercise_e.json") as f:
        user_dict = json.load(f)

        user1 = User.from_dict(user_dict)

        print(user1)
