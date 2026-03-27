class Address:
    def __init__(self, city):
        self.city = city


    @classmethod
    def from_dict(cls, data):
         return cls(data["city"])


class User:
    def __init__(self, name, address):
        self.name = name
        self.address = address


    @classmethod
    def from_dict(cls, data):
        address = Address.from_dict(data["address"])
        return cls(data["name"], address)
