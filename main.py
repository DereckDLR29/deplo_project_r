from datetime import datetime as dt  # dt is just an alias to avoid writing "datetime" repeatedly
import random  # Used for generating random IDs

users= {}  # Stores users as {id: (fullname, email)}
orders= {}  # Stores orders as {order_id: (client, product, unit_price, quantity, total, date)}
products= {}  # Stores products as {id: (name, price)}
see= ("Name:", "Unit price:")  # Used with zip() to label tuple values when printing
option= True  # Initially boolean, later replaced by integer input (type changes dynamically)

def register_client(f_users, f_id, f_name, f_lastname, f_email):
    """
    Creates a user within an ID and email, using both name and lastname to create username.
    A username and email validation that allow registration if there's any @ and a dot in the last one.
    Plus, show registered users list printing current users by ID.
    """

    if f_id in users and fullname in users and f_email in users:  # fullname is referenced before assignment → potential crash
        print("Any user information already registered in another one.")

    if f_name.isalpha() and f_lastname.isalpha() and "@" in f_email and "." in f_email:  # Only checks structure, not real email validity
        fullname= f_name + " " + f_lastname  # Concatenation to create display name
        print("Name and email registered succesfully.")
        data= (fullname, f_email)          
        users[f_id]= data  # Tuple is immutable → prevents accidental modification
    else:
        print("Theres invalid values, please try it again")
        
    print("\nCurrent users by ID")
    for user in f_users:  # Iterating a dict directly returns keys
        print(user)

    if fullname and f_email is True:  # Logical issue: f_email is a string, not a boolean
        return f_id, data


def register_product(f_products, fp_name, f_price, f_see, f_idproduct):
    """
    This option request product name and unit price, generating a random ID for this product and adding it in available products dictionary.
    There's a option to see current product list, showing IDs, name and unit price previously defined.
    """

    if f_idproduct in f_products:
        print("Validating the system, we found this number already exists, Generating another one, please wait a moment...")  # No actual regeneration happens

    new_product= (fp_name, f_price)  # Product stored as tuple (fixed structure)
    f_products[f_idproduct]= new_product

    print(f"Product saved!\nCurrent products")
    for product, properties in f_products.items():
        print("ID:", product)
        for property, show in zip(properties, f_see):  # zip pairs ("name", price) with labels ("Name:", "Unit price:")
            print(show, property)
        print("-"*40)

    if f_idproduct and new_product is True:  # Tuple will never equal True → unreachable return
        return f_idproduct, new_product
    

def validate_things(dictionary, message):
    """
    Specific function to validate the ID user/product.
    ID of the product to be purchased and the user who will purchase it.
    """

    while True:  # Loop guarantees valid input before continuing program flow
        try:
            variable_id = int(input(f"Enter {message} ID: "))  # Explicit casting to int
            if variable_id in dictionary:
                return variable_id  # Only returns if ID exists
            else:
                print(f"{message} not found. Try again.")
        except ValueError:
            print("Please enter a valid number.")  # Handles invalid conversion


def create_order(f_users, f_products, f_orders, client_id, product_id):
    """
    Creates a new order associating one client, one product and quantity.
    Returns the new order ID if successful.
    """

    if client_id not in f_users:
        print("There are no registered customers yet. Try at least registering someone")
        return 
    if product_id not in f_products:
        print("There are no products registered yet. Try at least registering one product")
        return
    
    print("Registered customers: ")
    for fid, (name, email) in f_users.items():  # Tuple unpacking directly in loop
        print(f" ID: {fid} | Name: {name.title()} | Email: {email}")
    
    print("\n", "-"*40)
    
    print("Available products: ")
    for fid, (name, price) in f_products.items():
        print(f" ID: {fid} | Name: {name} | Price: ${price:.2f}")
    
    print("\n", "-"*40)
    
    while True:
        try:
            quantity = int(input("Enter quantity: "))  # Input must be numeric
            if quantity > 0:
                break
            print("Quantity must be greater than 0.")
        except ValueError:
            print("Please enter a valid number.")
    
    print("\n", "-"*40)
      
    product_name = f_products[product_id][0]  # Access by index → relies on fixed tuple structure
    unit_price = f_products[product_id][1]
    total = unit_price * quantity  # Basic calculation
    
    if f_orders:
        order_id = max(f_orders.keys())  # ⚠️ This will overwrite last order (no +1)
    else:
        order_id = random.randint(100000, 200000)

    order_tuple = (
        f_users[client_id][0],   
        product_name,            
        unit_price,              
        quantity,                
        total,                   
        dt.now().strftime("%Y-%m-%d %H:%M")  # Converts datetime to formatted string
    )
    
    f_orders[order_id] = order_tuple  # Stores full order snapshot
    
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
    print("ORDERS REVIEW".center(50))  # center() aligns text within width
    print("="*50)
    
    orders_quantity= 0
    
    for order_id, data in f_orders.items():
        orders_quantity+= 1

        cliente, prod, unit_price, cant, total, fecha = data  # Must match tuple structure exactly

        print(f"ID: {order_id} | Fecha: {fecha} \nCliente: {cliente}\nProducto: {prod} \nQuantity: {cant}\nTotal order: ${total:.2f}")
        print("-" * 50)

        print(f"\nA total of {orders_quantity} orders have been reviewed.")  # Printed every loop iteration

    return orders_quantity


def calculate_revenues(f_orders):
    """
    Calculates the total daily income by summing all registered orders.
    """

    if not f_orders:
        return 0.0
    
    total_income = 0.0
    for order_data in f_orders.values():
        total_income += order_data[4]  # Relies on position → index 4 = total
    
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

        product_summary = {}  # Aggregation dictionary → groups by product name

        for order_id, properties in f_orders.items():
            overall+= 1
            client, product, unit_price, quantity, total, date = properties

            if product not in product_summary:
                product_summary[product] = [0, 0]  # [total_quantity, total_revenue]

            product_summary[product][0] += quantity  # Accumulates quantity instead of overwriting
            product_summary[product][1] += total     # Accumulates revenue per product

            final_revenue += total  # Global accumulation

        print("Product summary","\n","-"*40, "ID", order_id)  # order_id here is last loop value

        for product, values in product_summary.items():
            total_quantity, total_product_revenue = values
            print(f"Product: {product} \nTotal quantity sold: {total_quantity} \nTotal revenue: ${total_product_revenue:.2f}")
            print("-"*56)

        print(f"\nTotal orders: {overall} \nFinal revenue: ${final_revenue:.2f}")
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
            name= input("Please enter your name: ").capitalize()  # Only capitalizes first letter
            lastname= input("Please enter your lastname: ").capitalize()
            email= input("Please enter your email: ").lower()
            register_client(users, id, name, lastname, email)
        except:
            print("Uh")  # Bare except hides specific error

    elif option== 2:
        id_product = random.randint(1000, 2000) 
        name= input("Product name: ")
        try:
            price= float(input("Price: "))  # Conversion required for numeric operations
            register_product(products, name, price, see, id_product)
        except:
            print("Invalid price.")

    elif option== 3:
        client_id= validate_things(users, "Client")  # Variables become available after execution
        product_id= validate_things(products, "Product")

    elif option== 4:
        new_id = create_order(users, products, orders, client_id, product_id)  # Depends on previous step
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
        current_date = dt.now().strftime("%A, %B %d")  # Example: Friday, March 20
        final_report(orders, current_date)

    elif option== 8:
        print("Thanks for use our services!")