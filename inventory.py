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
    product_id = input("Enter Product ID: ")
    name = input("Enter Product Name: ")
    quantity = int(input("Enter Product Quantity: ")) 
    price = float(input("Enter Product Price: "))

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
        print("\nNo Products Available.\n")
        return
    print("\nPRODUCTS LIST")
    for product in products:
        print(
            f"ID: {product['id']} | "
            f"Name: {product['name']} | "
            f"Quantity: {product['quantity']} | "
            f"Price: Rs.{product['price']}"
        )
# Search products
def search_products(products):
    Search_id = input("Enter Product ID: ")
    for product in products:
        if product["id"] == Search_id:
            print("\nProduct Found")
            print(product)
            return
        print("Product not Found!")

#update products
def update_products(products):
    product_id = input("Enter Product ID: ")
    for product in products:
        if product["id"] == product_id:
               new_quantity = (
                   input("Enter New Quantity: ")
               )
               product["quantity"] = new_quantity
               save_products(products)
               print("Stock Updated Successfully!")
               return
        print("Product Not Found!")

# delate products
def delete_products(products):
    product_id = input("Enter Product ID; ")
    for product in products:
        if product["id"] == product_id:
            products.remove(product)
            save_products(products)
            print("Product Remove Successfully!")
            return
        print("Product Not Found!")

#login function
def login():
    username = "Admin"
    password = "admin1234"
    print("\nLOGIN TO INVENTORY MANAGEEMENT SYSTEM")
    entered_username = input("Enter Username: ")
    entered_password = input("Enter Password: ")

    if entered_username  == username and entered_password == password:
        print("login Successful!")
        return True
    print ("Invalid Username or Password!")
    return False         

#main menu
def main():
    products = load_products()
    while True:
        print("""
        iNVENTORY MANAGEMENT SYSTEM
              1. Add Product
              2. View Products
              3. Search Products
              4. Update Product
              5. Delete Product
              6. Exit
        """)
        choice = input("Enter Your Choice: ")
        if choice == "1":
            add_product(products)
        elif choice == "2":
            view_products(products)
        elif choice == "3":
            search_products(products)
        elif choice == "4":
            update_products(products)
        elif choice == "5":
            delete_products(products)
        elif choice == "6":
            print("Thank you for using the Inventory Management System!")
            break
        else:
            print("Invalid Choice please Try Again!")    

if __name__ == "__main__":
    if login():
        main()