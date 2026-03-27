from books import Author
import json


if __name__ == '__main__':
    with open("author_names.json") as f:
        user_dict = json.load(f)
        author = Author.from_dict(user_dict)
        print(author)

