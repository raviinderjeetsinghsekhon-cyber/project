from utils.db_handler import get_connection
from inventory.menu_manager import display_menu

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