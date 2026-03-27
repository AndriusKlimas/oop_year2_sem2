import json
from users import User

with open("info.json") as json_file:
    data = json.load(json_file)

    u = User.from_dict(data)

    print(f"Username is {u.username}")
