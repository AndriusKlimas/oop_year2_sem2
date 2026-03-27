import json
from ex_e_class import User

if __name__ == "__main__":
    with open("ex_f_list.json") as f:
        data = json.load(f)

        info = []
        for user in data:
            info.append(User.from_dict(user))
            print(user)
            

