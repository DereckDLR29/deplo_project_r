from datetime import datetime as dt
import random
import re
users= {}
orders= {}
products= {}
see= ("Name:", "Unit price:")
option= True
def register_client(f_users, f_id, f_name, f_lastname, f_email):
    """
    Creates a user within an ID and email, using both name and lastname to create username.
    A username and email validation that allow registration if there's any @ and a dot in the last one.
    Plus, show registered users list printing current users by ID.
    """
    if f_id in users and fullname in users and f_email in users:
        print("Any user information already registered in another one.")
    if f_name.isalpha() and f_lastname.isalpha() and "@" in f_email and "." in f_email:
        fullname= f_name + " " + f_lastname
        print("Name and email registered succesfully.")
        data= (fullname, f_email)          
        users[f_id]= data
    else:
        print("Theres invalid values, please try it again")
        
    print("\nCurrent users by ID")
    for user in f_users:
        print(user)
    if fullname and f_email is True:
        return f_id, data

def register_product(f_products, fp_name, f_price, f_see, f_idproduct):
    """
    This option request product name and unit price, generating a random ID for this product and adding it in available products dictionary.
    There's a option to see current product list, showing IDs, name and unit price previously defined.
    """
    if f_idproduct in f_products:
        print("Validating the system, we found this number already exists, Generating another one, please wait a moment...")
    new_product= (fp_name, f_price)
    f_products[f_idproduct]= new_product
    print(f"Product saved!\nCurrent products")
    for product, properties in f_products.items():
        print("ID:", product)
        for property, show in zip(properties, f_see):
            print(show, property)
        print("-"*40)
    if f_idproduct and new_product is True:
        return f_idproduct, new_product
    
def validate_things(dictionary, message):
    while True:
        try:
            variable_id = int(input(f"Enter {message} ID: "))
            if variable_id in dictionary:
                return variable_id
            else:
                print(f"{message} not found. Try again.")
        except ValueError:
            print("Please enter a valid number.")

def create_order(f_users, f_products, f_orders, client_id, product_id):
    """
    Creates a new order associating one client, one product and quantity.
    Returns the new order ID if successful, otherwise returns None.
    """
    if client_id not in f_users:
        print("There are no registered customers yet. Try at least registering someone")
        return 
    if product_id not in f_products:
        print("There are no products registered yet. Try at least registering one product")
        return
    
    print("Registered customers: ")
    for fid, (name, email) in f_users.items():
        print(f" ID: {fid} | Name: {name.title()} | Email: {email}")

    print("Available products: ")

    for fid, (name, price) in f_products.items():
        print(f" ID: {fid} | Name: {name} | Price: ${price:.2f}")

    while True:
        try:
            quantity = int(input("Enter quantity: "))
            if quantity > 0:
                break
            print("Quantity must be greater than 0.")
        except ValueError:
            print("Please enter a valid number.")
      
    product_name = f_products[product_id][0]
    unit_price = f_products[product_id][1]
    total = unit_price * quantity
    
    if f_orders:
        order_id = max(f_orders.keys()) + 1
    else:
        order_id = random.randint(100000, 200000)
    order_tuple = (
        f_users[client_id][0],   
        product_name,            
        unit_price,              
        quantity,                
        total,                   
        dt.now().strftime("%Y-%m-%d %H:%M")  
    )
    
    f_orders[order_id] = order_tuple
    
    print(f"Order created successfully!\nOrder ID: {order_id}\nClient: {f_users[client_id][0]}\nProduct: {product_name}\nQuantity: {quantity}\nTotal: ${total:.2f}")
    
    return order_id

def check_orders(f_orders):
    """
    Iterates in orders dictionary to print orders recorded in system.
    Plus, returns the number of finished orders.
    """
    if not f_orders:
        print("\nNo orders registered yet.")
        return

    print("\n" + "="*50)
    print("ORDERS REVIEW".center(50))
    print("="*50)
    
    orders_quantity= 0
    
    for order_id, data in f_orders.items():
        orders_quantity+= 1
        cliente, prod, precio, cant, total, fecha = data
        print(f"ID: {order_id} | Fecha: {fecha} \nCliente: {cliente}\nProducto: {prod} \nQuantity: {cant})\nTotal order: ${total:.2f}")
        print("-" * 50)
        print(f"\nA total of {orders_quantity} orders have been reviewed.")
    return orders_quantity

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

def final_report(f_orders, report_date):
    """
    This function uses datetime module to print day of weekend in report.
    Defines properties in all orders values to iterate these dictionary and
    show final revenue adding total per order to this value.
    """
    final_revenue= 0
    if not f_orders:
        print("There's no any orders registered!")
    else:
        print("Report for", report_date)
        overall= 0
        for order_id, properties in f_orders.items():
            overall+= 1
            client, product, price, quantity, total, date= properties
            print("-" * 56, "ID:", order_id, "\nClient:", client, "/ Product", product, "/ Quantity:", quantity)
            print(f"Total order: ${total:.2f}")
            print("-" *56, "\nTotal orders:", overall)
            final_revenue+= total
        print("\nFinal revenue:", final_revenue)
        return overall

while option != 8:
    try:
        option = int(input("Select any function\n 1) Client register\n 2) Product register\n 3) Validate inputs\n 4) Create order\n 5) Check orders\n 6) Calculate revenues\n 7) Generate report\n 8) Exit\n>> "))
        if option not in range(1, 9):
            raise ValueError
    except ValueError:
        print("Invalid option, please select a valid one.")
        continue
    if option== 1:
        id= random.randint(10000, 50000)
        try:
            name= input("Please enter your name: ").capitalize()
            lastname= input("Please enter your lastname: ").capitalize()
            email= input("Please enter your email: ").lower()
            register_client(users, id, name, lastname, email)
        except:
            print("Uh")
    elif option== 2:
        id_product = random.randint(1000, 2000) 
        name= input("Product name: ")
        try:
            price= float(input("Price: "))
            register_product(products, name, price, see, id_product)
        except:
            print("Invalid price.")
    elif option== 3:
        client_id= validate_things(users, "Client")
        product_id= validate_things(products, "Product")
    elif option== 4:
        new_id = create_order(users, products, orders, client_id, product_id)
        if new_id:
            print(f"Order #{new_id} was created.")
    elif option== 5:
        check_orders(orders)
    elif option== 6:
        total = calculate_revenues(orders)
        print("\n" + "=" * 50)
        print("     DAILY INCOME CALCULATION")
        print("=" * 50)
        if total == 0.0:
            print("No orders registered yet.")
        else:
            print(f"Total income generated today: ${total:.2f}")
        print("=" * 50)
    elif option== 7:
        current_date = dt.now().strftime("%A, %B %m")
        final_report(orders, current_date)
    elif option== 8:
        print("Thanks for use our services!")
