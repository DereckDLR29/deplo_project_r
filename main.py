from datetime import datetime as dt
import random
import re
users= {}
orders= {}
products= {}
see= ("Name:", "Unit price:")
option= True
def register_client(f_users, f_id, f_fullname, f_email):
    while True:
        try:
            if f_id in users and f_fullname in users and f_email in users:
                print("Any user information already registered in another one.")
            if f_fullname.isalpha() and "@" in f_email and "." in f_email:
                print("Name and email registered succesfully.")
                data= (f_fullname, f_email)
                users[f_id]= data
                break
            else:
                raise ValueError
        except:
            print("Please enter a valid email")
    print("\nCurrent users by ID")
    for user in users:
        print(user)

def register_product(f_products, fp_name, f_price, f_see, f_idproduct):
    while True:
        if f_idproduct not in f_products:
            break
        else:
            print("Validating the system, we found this number already exists. Generating another one, please wait a moment...")

    new_product = (fp_name, f_price)
    f_products[f_idproduct] = new_product
    print(f"Product saved!\nCurrent products")
    for product, properties in f_products.items():
        print("ID:", product)
        for property, show in zip(properties, f_see):
            print(show, property)
        print("-"*40)
    
def create_order(f_users, f_products, f_orders):
    pass

def check_orders(f_users, f_products, f_orders):
    pass

def calculate_revenues(f_products, f_orders):
    pass

def final_report(f_products, f_orders):
    pass

while option != 7:
    try:
        option = int(input("Select any function\n 1) Client register\n 2) Product register \n 3) Create order\n 4) Check orders\n 5) Calculate revenues\n 6) Generate report\n 7) Exit\n>> "))
        if option not in range(1, 8):
            raise ValueError
    except ValueError:
        print("Invalid option, please select a valid one.")
        continue
    if option== 1:
        id= random.randint(10000, 50000)
        fullname= input("Please enter your full name: ").upper()
        email= input("Please enter your email: ").lower()
        register_client(users, id, fullname, email)
    elif option== 2:
        id_product = random.randint(1000, 2000) 
        name= input("Product name: ")
        try:
            price= float(input("Price: "))
            register_product(products, name, price, see, id_product)
        except:
            print("Invalid price")
    elif option== 3:
        create_order(users, products, orders)
    elif option== 4:
        check_orders(users, products, orders, see)
    elif option== 5:
        calculate_revenues(products, orders)
    elif option== 6:
        final_report(products, orders)
    elif option== 7:
        print("Thanks for use our services!")
        
