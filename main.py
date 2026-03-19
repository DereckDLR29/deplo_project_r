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
    """
    Creates a new order associating one client, one product and quantity.
    Returns the new order ID if successful, otherwise returns None.
    """
    if not f_users:
        print("There are no registered customers yet")
        print("Try at least registering one customer")
        return 
    if not f_products:
        print("There are no products registered yet")
        print("Try at least registering one product")
        return
    
    print("Registered customers: ")
    
    for fid, (name, email) in f_users.items():
        print(f" ID: {fid} | Name: {name.title()} | Email: {email}")
        
    while True:
        try:
            client_id = int(input("Enter customer ID: "))
            if client_id in f_users:
                break
            print("Customer not found. Try again.")
        except ValueError:
            print("Please enter a valid number.")
    
    print("Available products: ")
    
    for fid, (name, price) in f_products.items():
        print(f"  ID: {fid} | Name: {name} | Price: ${price:.2f}")
        
    while True:
        try:
            prod_id = int(input("Enter product ID: "))
            if prod_id in f_products:
                break
            print("Product not found. Try again.")
        except ValueError:
            print("Please enter a valid number.")
    
    while True:
        try:
            quantity = int(input("Enter quantity: "))
            if quantity > 0:
                break
            print("Quantity must be greater than 0.")
        except ValueError:
            print("Please enter a valid number.")
      
    product_name = f_products[prod_id][0]
    unit_price = f_products[prod_id][1]
    total = unit_price * quantity
    
    if f_orders:
        order_id = max(f_orders.keys()) + 1
    else:
        order_id = 10001
        order_tuple = (
        f_users[client_id][0],   
        product_name,            
        unit_price,              
        quantity,                
        total,                   
        dt.now().strftime("%Y-%m-%d %H:%M")  
    )
    
    f_orders[order_id] = order_tuple
    
    print(f"Order created successfully!")
    print(f"Order ID: {order_id}")
    print(f"Client: {f_users[client_id][0]}")
    print(f"Product: {product_name}")
    print(f"Quantity: {quantity}")
    print(f"Total: ${total:.2f}")
    
    return order_id

def check_orders(f_users, f_products, f_orders):
    pass

def calculate_revenues(f_orders):
    """
    Calculates the total daily income by summing all registered orders.
    
    This function was developed collaboratively:
    - Person 1: Basic sum logic
    - Person 2: Main function with validation and return value
    
    Args:
        f_orders (dict): Dictionary containing all orders 
                        (order_id -> (client_name, product_name, unit_price, quantity, total, date))
    
    Returns:
        float: Total daily income (sum of all order totals)
               Returns 0.0 if there are no orders.
    """
    if not f_orders:
        return 0.0
    
    total_income = 0.0
    for order_data in f_orders.values():
        total_income += order_data[4]   # index 4 = total of the order
    
    return total_income

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
            print("Invalid price.")
    elif option== 3:
        new_id = create_order(users, products, orders)
        if new_id is not None:
            print(f"Order #{new_id} was created.")
    elif option== 4:
        check_orders(users, products, orders, see)
   
    elif option == 5:
        total = calculate_revenues(orders)
        
        print("\n" + "=" * 50)
        print("     DAILY INCOME CALCULATION")
        print("=" * 50)
        if total == 0.0:
            print("No orders registered yet.")
        else:
            print(f"Total income generated today: ${total:.2f}")
        print("=" * 50)
    elif option== 6:
        final_report(products, orders)
    elif option== 7:
        print("Thanks for use our services!")
        
