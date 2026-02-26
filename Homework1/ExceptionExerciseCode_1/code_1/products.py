class Product:
    def __init__(self, id, name, cost_price, retail_price, quantity):

        if Product.id_validation(id):
            self.id = id
        else:
            raise ValueError("Invalid product id")

        if Product.name_validation(name):
            self.name = name
        else:
            raise ValueError("Invalid product name")


        self.name = name
        self.cost_price = cost_price
        self.retail_price = retail_price
        self.quantity = quantity

    def __str__(self):
        print(f"id = {self.id}, name = {self.name}, cost_price = {self.cost_price}, retail_price = {self.retail_price}, quantity = {self.quantity}")

    def __repr__(self):
        print(f"id = {self.id}, name = {self.name}, cost_price = {self.cost_price}, retail_price = {self.retail_price}, quantity = {self.quantity}")


    @staticmethod
    def id_validation(id):
        if id < 0:
            return False

        if id is None:
            return False

        else:
            return True

    @staticmethod
    def name_validation(name):
        if name is None:
            return False
        else:
            return True

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
    print("Testing ID as -1, should come with error")
    try:
        product1 = Product(-1,"wheel",1,1,1)
    except ValueError as e:
        print(e)
