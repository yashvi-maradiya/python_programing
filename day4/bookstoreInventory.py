'''Scenario: Bookstore Inventory Management
Problem: You are managing the inventory of a bookstore. You need to create a Python program that
allows you to add new books to the inventory and display the current inventory.

Description: 
Program should contain add_book function which ask user name of book and
in second line quantity of book. Add it in inventory dictionary
display_inventory: Print all books currently in dict
update_book_quantity: input book_name and updated quantity and update in dictionary.
Application should keep running until user wants to exit

Main Options:
1. Add a book to inventory
2. Display current inventory
3. Update book quantity
4. Exit'''


class BookstoreInventory:
    def __init__(self):
        self.inventory = {}

    def add_book(self):
        book_name = input("Enter the name of the book: ")
        quantity = int(input("Enter the quantity of the book: "))
        if book_name in self.inventory:
            print("Book already exists in inventory. Updating quantity...")
            self.update_book_quantity(book_name, quantity)
        else:
            self.inventory[book_name] = quantity
            print(f"Book '{book_name}' added to inventory with quantity {quantity}.")

    def display_inventory(self):
        print("\nCurrent Inventory:")
        for book, quantity in self.inventory.items():
            print(f"{book}: {quantity}")

    def update_book_quantity(self, book_name, updated_quantity):
        if book_name in self.inventory:
            self.inventory[book_name] = updated_quantity
            print(f"Book '{book_name}' quantity updated to {updated_quantity}.")
        else:
            print("Book not found in inventory.")

    def run(self):
        while True:
            print("\nMain Options:")
            print("1. Add a book to inventory")
            print("2. Display current inventory")
            print("3. Update book quantity")
            print("4. Exit")
            choice = int(input("Enter your choice: "))
            if choice == 1:
                self.add_book()
            elif choice == 2:
                self.display_inventory()
            elif choice == 3:
                book_name = input("Enter the name of the book: ")
                updated_quantity = int(input("Enter the updated quantity of the book: "))
                self.update_book_quantity(book_name, updated_quantity)
            elif choice == 4:
                print("Exiting...")
                break
            else:
                print("Invalid choice. Please try again.")

if __name__ == "__main__":
    inventory_manager = BookstoreInventory()
    inventory_manager.run()
