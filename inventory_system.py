# Your program should allow the user to:
# Add products
# Remove products
# Update quantities
# Check stock
# Display all product


inventory = {
    "jersey": 10,
    "sneakers": 5,
    "caps": 8
}
menu = ""
while menu != 6:
    menu = input("1.Add new product\n2.Remove a product\n3.update quantity\n4.check a particular stock\n5.List all products\n6.Exit\nselect an option: ")
    if menu == "1":
        product = input("Enter product you'd like to add: ")
        quantity = int(input("Enter the quantity: "))
        inventory[product] = quantity
        print(f"{product} added to inventory")
    elif menu == "2":
        delete_product = input("Enter a product you'd like to delete: ")
        if delete_product in inventory:
            del inventory[delete_product]
            print(f"{delete_product} removed from inventory")
    elif menu == "3":
        search_product = input("Enter the product you'd like to update: ")
        
        if search_product in inventory:
            update_quantity = int(input("Enter the quantity  you'd like to update: "))
            inventory[search_product] = update_quantity
            print(f"{search_product} updated to {update_quantity}")
        else:
            print(f"{search_product} invalid")
    elif menu == "4":
        check_stock = input ("Enter the product to check: ")
        if check_stock in inventory:
            print(f"{check_stock}:{inventory[check_stock]}")
        else:
            print("Product not found")
    elif menu == "5":
        for product, quantity in inventory.items():
            print(f"{product}:{quantity}")
    elif menu =="6":
        print("exiting")
        exit()
    else:
        print("Stock not found")
        print("Try Again")