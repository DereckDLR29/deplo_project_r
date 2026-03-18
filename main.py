MENU_OPTIONS = (
    (1, "Register Client"),
    (2, "Register Product"),
    (3, "Create Order"),
    (4, "View Registered Orders"),
    (5, "Calculate Daily Revenue"),
    (6, "Generate Final Report"),
    (0, "Exit"),
)
def display_menu(menu_options: tuple) -> None:
    
    print("\n" + "=" * 45)
    print("   CUSTOMER ORDER MANAGEMENT SYSTEM")
    print("=" * 45)

    for option in menu_options:
        option_number = option[0]
        option_label  = option[1]

        if option_number == 0:
            print("-" * 45)

        print(f"  [{option_number}]  {option_label}")

    print("=" * 45)

def get_menu_choice(menu_options: tuple) -> int:
    
    # Build a tuple of valid option numbers for validation
    valid_options = tuple(option[0] for option in menu_options)

    while True:
        try:
            choice = int(input("\n  Enter an option: "))

            if choice in valid_options:
                return choice
            else:
                print(f"  ⚠  Invalid option. Please choose from: {valid_options}")

        except ValueError:
            print("  ⚠  Please enter a valid number.")

def route_menu_choice(choice: int, clients: dict, products: dict, orders: dict) -> dict:
   
    if choice == 1:
        # ── Call register_client from clients module ──────────────────
        print("\n  ── Register Client ──")
        # register_client(clients)

    elif choice == 2:
        # ── Call register_product from products module ─────────────────
        print("\n  ── Register Product ──")
        # register_product(products)

    elif choice == 3:
        # ── Call create_order from orders module ──────────────────────
        print("\n  ── Create Order ──")
        # create_order(orders, clients, products)

    elif choice == 4:
        # ── Call display_orders from queries module ────────────────────
        print("\n  ── View Registered Orders ──")
        # display_orders(orders, clients, products)

    elif choice == 5:
        # ── Call calculate_daily_revenue from revenue module ───────────
        print("\n  ── Calculate Daily Revenue ──")
        # calculate_daily_revenue(orders)

    elif choice == 6:
        # ── Call generate_final_report from reports module ─────────────
        print("\n  ── Generate Final Report ──")
        # generate_final_report(orders, clients, products)

    return {"success": True}


def run_menu() -> None:

    clients : dict = {}
    products: dict = {}
    orders  : dict = {}

    print("\n  Welcome to the Customer Order Management System")

    while True:
        display_menu(MENU_OPTIONS)
        choice = get_menu_choice(MENU_OPTIONS)

        if choice == 0:
            print("\n  Goodbye! Session ended.\n")
            break

        # Dicts are passed by reference — changes inside modules persist
        route_menu_choice(choice, clients, products, orders)

if __name__ == "__main__":
    run_menu()
