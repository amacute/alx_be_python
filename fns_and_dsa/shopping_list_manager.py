# shopping_list_manager.py

def display_menu():
    """Prints the menu options for the shopping list manager."""
    print("\nShopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")

def main():
    """Main function to run the shopping list manager program."""
    shopping_list = [] # Initialize an empty list for the shopping list

    while True:
        display_menu() # Display the menu
        choice = input("Enter your choice: ").strip() # Get user's choice, strip whitespace

        if choice == '1':
            # Add Item functionality
            item = input("Enter the item to add: ").strip()
            if item: # Ensure item is not empty
                shopping_list.append(item)
                print(f"'{item}' added to the list.")
            else:
                print("Item name cannot be empty.")
        elif choice == '2':
            # Remove Item functionality
            if not shopping_list:
                print("The shopping list is empty. Nothing to remove.")
                continue # Go back to menu
            
            item = input("Enter the item to remove: ").strip()
            if item in shopping_list:
                shopping_list.remove(item)
                print(f"'{item}' removed from the list.")
            else:
                print(f"'{item}' not found in the list.")
        elif choice == '3':
            # View List functionality
            if not shopping_list:
                print("The shopping list is empty.")
            else:
                print("\n--- Shopping List ---")
                for i, item in enumerate(shopping_list, 1):
                    print(f"{i}. {item}")
                print("---------------------")
        elif choice == '4':
            # Exit functionality
            print("Goodbye!")
            break # Exit the loop, ending the program
        else:
            # Handle invalid menu choices
            print("Invalid choice. Please try again.")

# Program entry point
if __name__ == "__main__":
    main()
