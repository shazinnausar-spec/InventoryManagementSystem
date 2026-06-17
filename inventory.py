import json
import os

FILENAME = "products.json"
#load porducts
def load_products():    #creating a function called Load_products
    if os.path.exists(FILENAME):
        with open(FILENAME, "r") as file:
            return json.load(file)
    return []
# save products 
def save_products(products):   #creating a function called save_products
    with open(FILENAME, "w") as file:
        json.dump(products, file, indent=4)
# add product
def add_product(products):
    porduct_id = input("enter product id: ")
    name = input("enter product name: ")
    quantity = int(input("enter product quantity: ")) 
    price = float(input("enter product price: "))

    product = {
        "id": product_id,
        "name": name,
        "quantity": quantity,
        "price":price
    }
    products.append(product)
    save_products(products)
    print("\nProduct Added Successfully!\n")

#view products
def view_products(products):
    if not products:
        print("\nNo products available.\n")
        return
    print("\nPRODUCTS LIST")
    for product in products:
        print(
            f"ID: {product['id']} | "
            f"Name: {product['name']} | "
            f"Quantity: {product['quantity']} | "
            f"price: Rs.{product['price']}"
        )