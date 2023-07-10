from product import Product

class Inventory:
    def __init__(self):
        self.products = [
            Product("Product 1", 10.99, 5),
            Product("Product 2", 5.99, 10),
            # Add more sample products here
        ]

    def get_products(self):
        return self.products
