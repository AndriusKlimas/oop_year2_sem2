import json
from users import User

with open("user.json") as json_file:
    data = json.load(json_file)


    users = {}
    for info in data:
        user = User.from_dict(info)
        users[user.name] = user

    print(users)
