from utils.db_handler import get_connection

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