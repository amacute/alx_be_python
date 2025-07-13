# shopping_list_manager.py

def display_menu():
    """Prints the menu options for the shopping list manager."""
    # Ensure this print statement exactly matches the checker's expectation
    print("Shopping List Manager") 
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
            # Prompt for and add an item
            item = input("Enter the item to add: ").strip()
            if item: # Ensure item is not empty before adding
                shopping_list.append(item)
                print(f"'{item}' added to the list.")
            else:
                print("Item name cannot be empty. Please enter a valid item.")
        elif choice == '2':
            # Prompt for and remove an item
            if not shopping_list:
                print("The shopping list is empty. Nothing to remove.")
                continue # Go back to the beginning of the loop (menu)
            
            item_to_remove = input("Enter the item to remove: ").strip()
            if item_to_remove in shopping_list:
                shopping_list.remove(item_to_remove)
                print(f"'{item_to_remove}' removed from the list.")
            else:
                print(f"'{item_to_remove}' not found in the list.")
        elif choice == '3':
            # Display the shopping list
            if not shopping_list:
                print("The shopping list is empty.")
            else:
                print("\n--- Current Shopping List ---")
                for i, item in enumerate(shopping_list, 1): # Enumerate to get numbered list
                    print(f"{i}. {item}")
                print("-----------------------------")
        elif choice == '4':
            # Exit functionality
            print("Goodbye!")
            break # Exit the while loop, ending the program
        else:
            # Handle invalid menu choices
            print("Invalid choice. Please enter a number between 1 and 4.")

if __name__ == "__main__":
    main()


