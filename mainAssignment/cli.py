from inventory import Inventory
from cart import CartItem
import csv

  # Create  instance of the Inventory class
inventory = Inventory()

# Create an empty list to represent the shopping cart
cart = []


while True:
    # Display  menu with options for the user
    print("1. Browse Products")
    print("2. Add Item to Cart")
    print("3. View Cart")
    print("4. Proceed to Checkout")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        # Implement the logic for browsing products
        products = inventory.get_products()
        for product in products:
            print(f"{product.get_name()} - Price: ₹ {product.get_price()}")

    elif choice == "2":
        # Implement the logic for adding items to the cart
        product_name = input("Enter the name of the product: ")
        quantity = int(input("Enter the quantity: "))

        # Find the product in the inventory
        selected_product = None
        for product in inventory.get_products():
            if product.get_name() == product_name:
                selected_product = product
                break

        if selected_product is None:
            print("Product not found.")
        elif selected_product.get_quantity() < quantity:
            print("Insufficient quantity.")
        else:
            # Add the item to the cart
            cart_item = CartItem(selected_product, quantity)
            cart.append(cart_item)
            print("Item added to the cart.")

    elif choice == "3":
        # Implement the logic for viewing the cart
        print("Cart Contents:")
        for item in cart:
            product = item.get_product()
            print(f"{product.get_name()} - Quantity: {item.get_quantity()} - Price: ₹ {item.get_price()}")

    elif choice == "4":
        # Implement the logic for proceeding to checkout
        # Calculate the total price of the items in the cart
        total_price = sum(item.get_price() for item in cart)
        print("Total Price:", total_price)
        f = open("products.csv", "w", newline='')
        wo = csv.writer(f)
        wo.writerow(["Product name", "quantity", "price", "total price"])
        name1 = ""
        quantity2 = ""
        price3 = ""
        for item in cart:
            product = item.get_product()
            name = product.get_name()
            quantity = item.get_quantity()
            price = item.get_price()
            data = [name, quantity, price]
            wo.writerow(data)
        data2= [name1, quantity2, price3, total_price]
        wo.writerow(data2)


    elif choice == "5":
        # Exit the program
        break

    else:
        print("Invalid choice. Please try again.")
1