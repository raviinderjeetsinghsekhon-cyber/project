import sqlite3

DB_NAME = "bakery.db"

def get_connection():
    return sqlite3.connect(DB_NAME)

def initialize_database():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            username TEXT PRIMARY KEY,
            password TEXT NOT NULL,
            role TEXT NOT NULL
        )
    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS menu (
            item_id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL UNIQUE,
            price REAL NOT NULL
        )
    ''')

    cursor.execute('''
        INSERT OR IGNORE INTO users (username, password, role)
        VALUES ('admin', 'ef92b778bafe771e89245b89ecbc08a44a4e166c06659911881f383d4473e94f', 'admin')
    ''')

    default_items = [
        ('Cake', 120.0),
        ('Bread', 40.0),
        ('Donut', 30.0),
        ('Cookie', 20.0)
    ]
    cursor.executemany('''
        INSERT OR IGNORE INTO menu (name, price) VALUES (?, ?)
    ''', default_items)

    conn.commit()
    conn.close()


def process_customer_order():
    items = display_menu()
    if not items:
        return

    menu_dict = {item[0]: (item[1], item[2]) for item in items}
    order_details = []
    total = 0.0

    print("\n--- Start Ordering (Enter 0 when finished) ---")
    while True:
        try:
            choice = int(input("\nEnter Item ID (0 to finish): "))
        except ValueError:
            print("Please enter a valid numeric Item ID.")
            continue

        if choice == 0:
            break

        if choice in menu_dict:
            try:
                qty = int(input(f"Enter quantity for {menu_dict[choice][0]}: "))
                if qty <= 0:
                    print("Quantity must be at least 1.")
                    continue
            except ValueError:
                print("Invalid quantity format.")
                continue

            name, price = menu_dict[choice]
            cost = price * qty
            order_details.append((name, qty, price, cost))
            total += cost
            print(f"Added {qty} x {name} (₹{cost:.2f})")
        else:
            print("Invalid Item ID!")

    print("\n" + "="*35)
    print("           BAKERY RECEIPT          ")
    print("="*35)
    if not order_details:
        print("No items purchased.")
    else:
        print(f"{'Item':<12} {'Qty':<5} {'Price':<8} {'Cost':<8}")
        print("-" * 35)
        for name, qty, price, cost in order_details:
            print(f"{name:<12} {qty:<5} ₹{price:<7.2f} ₹{cost:<7.2f}")
        print("-" * 35)
        print(f"TOTAL BILL:                ₹{total:.2f}")
    print("="*35)
import hashlib


def hash_password(password: str) -> str:
    return hashlib.sha256(password.encode()).hexdigest()

def authenticate_admin() -> bool:
    print("\n--- Admin Login ---")
    username = input("Username: ").strip()
    password = input("Password: ").strip()
    hashed_pwd = hash_password(password)

    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT role FROM users WHERE username = ? AND password = ?", (username, hashed_pwd))
    user = cursor.fetchone()
    conn.close()

    if user and user[0] == 'admin':
        print("\nLogin successful! Welcome Admin.")
        return True
    else:
        print("\nInvalid admin credentials!")
        return False    


# Function to show all items in the bakery menu
def display_menu():
    db = get_connection()
    cur = db.cursor()
    cur.execute("SELECT item_id, name, price FROM menu")
    all_items = cur.fetchall()
    db.close()

    print("\n===== BAKERY MENU =====")
    if len(all_items) == 0:
        print("Menu is empty right now!")
        return []
    
    # Printing items line by line
    for item in all_items:
        i_id = item[0]
        name = item[1]
        price = item[2]
        print(str(i_id) + ". " + name + " - Rs. " + str(price))
        
    return all_items


# Function to add a new item (Create)
def add_menu_item():
    item_name = input("Enter new item name: ").strip()
    
    # Simple check for empty name
    if item_name == "":
        print("Item name cannot be blank!")
        return

    try:
        item_price = float(input("Enter price: "))
        if item_price <= 0:
            print("Price should be more than 0!")
            return
    except:
        print("Invalid price! Please enter a number.")
        return

    db = get_connection()
    cur = db.cursor()
    try:
        cur.execute("INSERT INTO menu (name, price) VALUES (?, ?)", (item_name, item_price))
        db.commit()
        print("Success! Added " + item_name + " to the menu.")
    except:
        print("Could not add item. Maybe it already exists?")
    
    db.close()


# Function to change price of an item (Update)
def update_menu_item():
    display_menu()
    try:
        target_id = int(input("\nEnter Item ID to update: "))
        new_price = float(input("Enter new price: "))
        if new_price <= 0:
            print("Price must be positive!")
            return
    except:
        print("Please enter valid numbers.")
        return

    db = get_connection()
    cur = db.cursor()
    cur.execute("UPDATE menu SET price = ? WHERE item_id = ?", (new_price, target_id))
    
    if cur.rowcount > 0:
        db.commit()
        print("Price updated successfully!")
    else:
        print("Item ID not found!")
        
    db.close()


# Function to delete an item (Delete)
def delete_menu_item():
    display_menu()
    try:
        target_id = int(input("\nEnter Item ID to remove: "))
    except:
        print("Invalid ID entered!")
        return

    db = get_connection()
    cur = db.cursor()
    cur.execute("DELETE FROM menu WHERE item_id = ?", (target_id,))
    
    if cur.rowcount > 0:
        db.commit()
        print("Item deleted from menu!")
    else:
        print("No item found with that ID!")
        
    db.close()


# Main inventory management menu
def manage_inventory():
    while True:
        print("\n--- INVENTORY MENU ---")
        print("1. View All Items")
        print("2. Add New Item")
        print("3. Change Item Price")
        print("4. Remove Item")
        print("5. Go Back")
        
        opt = input("Choice (1-5): ").strip()
        
        if opt == "1":
            display_menu()
        elif opt == "2":
            add_menu_item()
        elif opt == "3":
            update_menu_item()
        elif opt == "4":
            delete_menu_item()
        elif opt == "5":
            break
        else:
            print("Wrong option! Select between 1 and 5.")    
def main():

    initialize_database()

    while True:
        print("\n====================================")
        print("   WELCOME TO BAKERY SYSTEM MAIN    ")
        print("====================================")
        print("1. New Customer Order")
        print("2. Admin Portal (Manage Inventory)")
        print("3. Exit Application")

        choice = input("Select an option (1-3): ").strip()

        if choice == '1':
            process_customer_order()
        elif choice == '2':
            if authenticate_admin():
                manage_inventory()
        elif choice == '3':
            print("\nThank you for using Bakery Billing System. Goodbye!")
            break
        else:
            print("Invalid option! Please enter 1, 2, or 3.")

if __name__ == "__main__":
    main()