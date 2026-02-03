class Products:
    def __init__(self, prod_id, name, unit_price, stock):

        if not Products.validate_prod_id(prod_id):
            print("Product ID provided is incorrect")
        self.prod_id = prod_id

        if not Products.validate_name(name):
            print("Product name provided is incorrect")
        self.name = name

        if not Products.validate_unit_price(unit_price):
            print("Unit price provided is incorrect")
        self.unit_price = unit_price

        if not Products.validate_stock(stock):
            print("Stock provided is incorrect")
        self.stock = stock


    def __str__(self):
        print(f"Product ID: {self.prod_id}, Name: {self.name}, Unit Price: {self.unit_price}, Stock: {self.stock}")

    def display(self):
        print(f"Product ID: {self.prod_id}, Name: {self.name}, Unit Price: {self.unit_price}, Stock: {self.stock}")

    def __repr__(self):
        print(f"Product ID: {self.prod_id}, Name: {self.name}, Unit Price: {self.unit_price}, Stock: {self.stock}")


    @staticmethod
    def validate_unit_price(unit_price):
        if unit_price is None:
            return False
        if unit_price < 0:
            return False
        return True

    @staticmethod
    def validate_stock(stock):
        if stock is None:
            return False
        if stock < 0:
            return False
        return True

    @staticmethod
    def validate_name(name):
        if name is None:
            return False
        if len(name.strip()) == 0:
            return False
        return True

    @staticmethod
    def validate_prod_id(prod_id):
        if prod_id is None:
            return False
        if len(str(prod_id).strip()) == 0:
            return False
        return True