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