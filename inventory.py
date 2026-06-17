import json
import os

FILENAME = "products.json"
#load porducts
def load_products():    #creating a function called Load_products
    if os.path.exists(FILENAME):
        with open(FILENAME, "r") as file:
            return json.load(file)
    return []
