
users = []     
products = []   
orders = []     
current_user = None



def main_menu():
    print("\n" + "="*40)
    print("         WELCOME TO QUICKCART")
    print("="*40)
    print("1. Login")
    print("2. Register")
    print("3. Exit")
    print("="*40)
    return input("Choose an option: ")


def admin_menu():
    print("\n" + "="*40)
    print("              ADMIN MENU")
    print("="*40)
    print("1. Add Product")
    print("2. Restock Product")
    print("3. View Orders")
    print("4. Logout")
    print("="*40)
    return input("Choose an option: ")


def user_menu():
    print("\n" + "="*40)
    print("              USER MENU")
    print("="*40)
    print("1. Browse Products")
    print("2. Place Order")
    print("3. View My Orders")
    print("4. Logout")
    print("="*40)
    return input("Choose an option: ")


def rider_menu():
    print("\n" + "="*40)
    print("              RIDER MENU")
    print("="*40)
    print("1. View Pending Orders")
    print("2. Update Delivery Status")
    print("3. Logout")
    print("="*40)
    return input("Choose an option: ")


# AUTHENTICATION

def register():
    global users
    print("\n--- Register ---")
    username = input("Enter username: ")
    password = input("Enter password: ")
    role = input("Enter role (admin/user/rider): ").lower()

    users.append({
        "username": username,
        "password": password,
        "role": role
    })
    print("✅ Registration successful!")


def login():
    global current_user
    print("\n--- Login ---")
    username = input("Enter username: ")
    password = input("Enter password: ")

    for user in users:
        if user["username"] == username and user["password"] == password:
            current_user = user
            print(f"✅ Welcome, {username}! You are logged in as {user['role']}.")
            return
    print("❌ Invalid credentials")




# ADMIN FUNCTIONS

def add_product():
    name = input("Product name: ")
    stock = int(input("Stock quantity: "))
    products.append({"name": name, "stock": stock})
    print("✅ Product added!")


def restock_product():
    if not products:
        print("⚠ No products available.")
        return
    for i, p in enumerate(products, start=1):
        print(f"{i}. {p['name']} (Stock: {p['stock']})")
    choice = int(input("Select product number to restock: ")) - 1
    amount = int(input("Enter amount to add: "))
    products[choice]["stock"] += amount
    print("✅ Product restocked!")


def view_orders():
    if not orders:
        print("⚠ No orders placed yet.")
    for o in orders:
        print(o)


# USER FUNCTIONS

def browse_products():
    if not products:
        print("⚠ No products available.")
        return
    print("\n--- Products ---")
    for i, p in enumerate(products, start=1):
        print(f"{i}. {p['name']} (Stock: {p['stock']})")


def place_order():
    if not products:
        print("⚠ No products available.")
        return
    browse_products()
    choice = int(input("Select product number: ")) - 1
    if products[choice]["stock"] > 0:
        products[choice]["stock"] -= 1
        order = {
            "user": current_user["username"],
            "product": products[choice]["name"],
            "status": "Pending"
        }
        orders.append(order)
        print("✅ Order placed!")
    else:
        print("❌ Out of stock.")


def view_my_orders():
    my_orders = [o for o in orders if o["user"] == current_user["username"]]
    if not my_orders:
        print("⚠ You have no orders.")
    for o in my_orders:
        print(o)


# RIDER FUNCTIONS

def view_pending_orders():
    pending = [o for o in orders if o["status"] == "Pending"]
    if not pending:
        print("⚠ No pending orders.")
    for i, o in enumerate(pending, start=1):
        print(f"{i}. {o}")


def update_delivery_status():
    pending = [o for o in orders if o["status"] == "Pending"]
    if not pending:
        print("⚠ No pending orders.")
        return
    view_pending_orders()
    choice = int(input("Select order number to deliver: ")) - 1
    pending[choice]["status"] = "Delivered"
    print("✅ Order marked as delivered!")



# MAIN APP LOOP

def run_app():
    global current_user
    while True:
        if not current_user:
            choice = main_menu()
            if choice == "1":
                login()
            elif choice == "2":
                register()
            elif choice == "3":
                print("👋 Goodbye!")
                break
        else:
            if current_user["role"] == "admin":
                choice = admin_menu()
                if choice == "1":
                    add_product()
                elif choice == "2":
                    restock_product()
                elif choice == "3":
                    view_orders()
                elif choice == "4":
                    current_user = None
            elif current_user["role"] == "user":
                choice = user_menu()
                if choice == "1":
                    browse_products()
                elif choice == "2":
                    place_order()
                elif choice == "3":
                    view_my_orders()
                elif choice == "4":
                    current_user = None
            elif current_user["role"] == "rider":
                choice = rider_menu()
                if choice == "1":
                    view_pending_orders()
                elif choice == "2":
                    update_delivery_status()
                elif choice == "3":
                    current_user = None



if __name__ == "__main__":
    run_app()
