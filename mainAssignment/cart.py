class CartItem:
    def __init__(self, product, quantity):
        self.product = product
        self.quantity = quantity
        self.price = product.get_price() * quantity

    def get_product(self):
        return self.product

    def get_quantity(self):
        return self.quantity

    def get_price(self):
        return self.price

    def adjust_quantity(self, new_quantity):
        self.quantity = new_quantity
        self.price = self.product.get_price() * new_quantity
