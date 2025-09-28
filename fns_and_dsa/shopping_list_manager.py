shopping_list = []  # start with an empty list


def display_menu():
    """Display the shopping list menu options."""
    print("\n===== Shopping List Manager =====")
    print("1. Add an item")
    print("2. Remove an item")
    print("3. View shopping list")
    print("4. Exit")

def add_item(shopping_list):
    """Add an item to the shopping list."""
    item = input("Enter the item to add: ").strip()
    if item:
        shopping_list.append(item)
        print(f"✅ '{item}' has been added to the shopping list.")
    else:
        print("⚠️ Item name cannot be empty.")


def remove_item(shopping_list):
    """Remove an item from the shopping list."""
    item = input("Enter the item to remove: ").strip()
    if item in shopping_list:
        shopping_list.remove(item)
        print(f"❌ '{item}' has been removed from the shopping list.")
    else:
        print(f"⚠️ '{item}' not found in the shopping list.")
def view_list(shopping_list):
    """View all items in the shopping list."""
    if shopping_list:
        print("\n🛒 Your Shopping List:")
        for idx, item in enumerate(shopping_list, 1):
            print(f"{idx}. {item}")
    else:
        print("\n🛒 Your shopping list is empty.")
def main():
    shopping_list = []  # start with an empty list
    
    while True:
        display_menu()
        choice = input("Choose an option (1-4): ").strip()
        
        if choice == "1":
            add_item(shopping_list)
        elif choice == "2":
            remove_item(shopping_list)
        elif choice == "3":
            view_list(shopping_list)
        elif choice == "4":
            print("👋 Exiting Shopping List Manager. Goodbye!")
            break
        else:
            print("⚠️ Invalid choice. Please select a valid option (1-4).")

if __name__ == "__main__":
    main()