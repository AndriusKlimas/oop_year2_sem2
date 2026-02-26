class Product:
    def __init__(self, id, name, cost_price, retail_price, quantity):


        valid, error_msg = Product.id_validation(id)
        if valid:
            self._id = id
        else:
            raise ValueError(error_msg)


        valid, error_msg = Product.name_validation(name)
        if valid:
            self._name = name
        else:
            raise ValueError(error_msg)

        if Product.cost_price_validation(cost_price):
            self.cost_price = cost_price
        else:
            raise ValueError("Invalid product cost")


        self.retail_price = retail_price
        self.quantity = quantity

    def __str__(self):
        print(f"id = {self._id}, name = {self._name}, cost_price = {self.cost_price}, retail_price = {self.retail_price}, quantity = {self.quantity}")

    def __repr__(self):
        print(f"id = {self._id}, name = {self._name}, cost_price = {self.cost_price}, retail_price = {self.retail_price}, quantity = {self.quantity}")


    @staticmethod
    def id_validation(id):
        if id < 0:
            return False, "ID cannot be negative"

        if id is None:
            return False, "No ID present"

        else:
            return True, None

    @staticmethod
    def name_validation(name):
        if name is None:
            return False, "Name cannot be None"
        else:
            return True, None

    @staticmethod
    def cost_price_validation(cost_price):
        if cost_price is None:
            return False, "cost_price cannot be None"
        if cost_price < 0:
            return False, f"cost_price cannot be negative"
        else:
            return True, None
    '''
        Code for the Product class goes here
        Product has:
        an id (unique)
        a name
        a cost price
        a retail price
        a quantity
    '''

class Book(Product):
    '''
        Code for the Book class goes here
        Book has:
        an id (unique)
        a name
        a cost price
        a retail price
        a quantity
        an author
        one or more genres (these should be stored in a list)
    '''
if __name__ == "__main__":
    print("Print, should all be good, no errors")
    try:
        product1 = Product(10,"Wheel",1,1,1)
    except ValueError as e:
        print(e)


    print("Invalid ID, should show error")
    try:
        product2 = Product(-1,"wheel",1,1,1)
    except ValueError as e:
        print(e)

    print("Invalid Name, should show error")
    try:
        product3 = Product(1,None,1,1,1)
    except ValueError as e:
        print(e)

    print("Invalid Cost Price, should show error, minus price")
    try:
        product4 = Product(1,"Wheel",-10,1,1)
    except ValueError as e:
        print(e)

    print("Invalid Retail Price, should show error, price = None")
    try:
        product5 = Product(1,"Wheel",None,1,1)
    except ValueError as e:
        print(e)
