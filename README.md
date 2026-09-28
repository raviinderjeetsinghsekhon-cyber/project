    from utils.db_handler import initialize_database
    from inventory.menu_manager import manage_inventory
    from billing.order_processor import process_customer_order
    from auth.authentication import authenticate_admin

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
