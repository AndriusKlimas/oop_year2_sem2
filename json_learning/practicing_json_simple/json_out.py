import json



with open("info.json") as f:
    ticket_dict = json.load(f)

    print(f"Name = {ticket_dict['name']}")
    print(f"Age = {ticket_dict['age']}")
    skill_list = ticket_dict['skills']
    print(f"Second skill = {skill_list[1]}")

