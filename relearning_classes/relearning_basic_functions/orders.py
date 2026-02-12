class Orders:
    def __init__(self, order_num, username, prod_id, quantity, price):

        if not Orders.validate_order_num(order_num):
            print("Order number provided is incorrect")
        self.order_num = order_num

        if not Orders.validate_username(username):
            print("Username provided is incorrect")
        self.username = username

        if not Orders.validate_prod_id(prod_id):
            print("Product ID provided is incorrect")
        self.prod_id = prod_id

        if not Orders.validate_quantity(quantity):
            print("Quantity provided is incorrect")
        self.quantity = quantity

        if not Orders.validate_price(price):
            print("Price provided is incorrect")
        self.price = price


    def __str__(self):
        print(f"Order Number: {self.order_num}, Username: {self.username}, Product ID: {self.prod_id}, Quantity: {self.quantity}, Price: {self.price}")

    def display(self):
        print(f"Order Number: {self.order_num}, Username: {self.username}, Product ID: {self.prod_id}, Quantity: {self.quantity}, Price: {self.price}")

    def __repr__(self):
        print(f"Order Number: {self.order_num}, Username: {self.username}, Product ID: {self.prod_id}, Quantity: {self.quantity}, Price: {self.price}")


    def __lt__(self, other:object) -> bool | NotImplementedType:
        if not isinstance(other, Orders):
            return NotImplemented
        return self.quantity < other.quantity

    def __gt__(self, other:object) -> bool | NotImplementedType:
        if not isinstance(other, Orders):
            return NotImplemented
        return self.quantity > other.quantity

    def __eq__(self, other) -> bool | NotImplementedType:
        if not isinstance(other, Orders):
            return NotImplemented
        return self.quantity == other.quantity

    def __le__(self, other:object) -> bool | NotImplementedType:
        if not isinstance(other, Orders):
            return NotImplemented
        return self.quantity <= other.quantity

    def __ge__(self, other:object) -> bool | NotImplementedType:
        if not isinstance(other, Orders):
            return NotImplemented
        return self.quantity >= other.quantity


    @staticmethod
    def validate_order_num(order_num):
        if order_num is None:
            return False
        if len(str(order_num).strip()) <= 0:
            return False
        return True

    @staticmethod
    def validate_quantity(quantity):
        if quantity is None:
            return False
        if quantity <= 0:
            return False
        return True

    @staticmethod
    def validate_price(price):
        if price is None:
            return False

        if price < 0:
            return False
        return True

    @staticmethod
    def validate_username(username):
        if username is None:
            return False

        if len(username.strip()) < 8:
            return False
        return True

    @staticmethod
    def validate_prod_id(prod_id):
        if prod_id is None:
            return False

        if len(str(prod_id).strip()) <= 0:
            return False
        return True

