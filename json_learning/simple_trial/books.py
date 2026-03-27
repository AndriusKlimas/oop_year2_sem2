class Author:
    def __init__(self, f_name, l_name):
        self.f_name = f_name
        self.l_name = l_name

    def __str__(self):
        return f'{self.f_name} {self.l_name}'


    @classmethod
    def from_dict(cls, data):
        return cls(data["f_name"], data["l_name"])








class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author


    def __str__(self):
        return self.title + " " + self.author


