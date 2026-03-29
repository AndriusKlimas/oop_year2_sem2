class Author:
    def __init__(self, f_name, l_name):
        self.f_name = f_name
        self.l_name = l_name

    def __str__(self):
        return f'{self.f_name} {self.l_name}'



    @classmethod
    def from_dict(cls, data):
        if data["type"] != cls.__name__:
            raise TypeError("Author's data must be of type Author")

        fname = data['f_name']
        lname = data['l_name']
        return cls(fname, lname)


    def to_dict(self):
        data = {}
        data["type"] = self.__class__.__name__

        data["f_name"] = self.f_name
        data["l_name"] = self.l_name
        return data








class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author


    def __str__(self):
        return self.title + " " + self.author


