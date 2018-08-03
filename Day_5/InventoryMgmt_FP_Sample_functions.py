import os

def menuDisplay():
    print ('=============================')
    print ('= Inventory Management Menu =')
    print ('=============================')
    print ('(1) Add New Item to Inventory')
    print ('(2) Remove Item from Inventory')
    print ('(3) Update Inventory')
    print ('(4) Search Item in Inventory')
    print ('(5) Print Inventory Report')
    print ('(99) Quit')
    CHOICE = int(input("Enter choice: "))
    menuSelection(CHOICE)

def menuSelection(CHOICE):
    if CHOICE == 1:
        addInventory()
    elif CHOICE == 2:
        removeInventory()
    elif CHOICE == 3:
        updateInventory()
    elif CHOICE == 4:
        searchInventory()
    elif CHOICE == 5:
        printInventory()
    elif CHOICE == 99:
        exit()

def addInventory():
    print ('Adding Inventory')
    print ('================')
    item_description = raw_input("Enter the name of the item: ")
    item_quantity = int(input("Enter the quantity of the item: "))
    item_quantity = str(item_quantity)
    
    InventoryFile = open('Inventory.txt', 'a')
    InventoryFile.write(item_description + '\n')
    InventoryFile.write(item_quantity + '\n')

    InventoryFile.close()

    CHOICE = int(input('Enter 98 to continue or 99 to exit: '))
    if CHOICE == 98:
            menuDisplay()
    else:
        exit()

def removeInventory():
    print ('Removing Inventory')
    print ('================')
    item_search = raw_input('Enter the item name to remove from inventory: ')

    InventoryFile = open('Inventory.txt', 'r') 
    temp_file = open('tempfile.txt', 'w') 

    item_description = InventoryFile.readline()

    while item_description != '':
        item_description = item_description.rstrip('\n')
        
        item_quantity = InventoryFile.readline()
        item_quantity = item_quantity.rstrip('\n')

        if item_description != item_search:
            temp_file.write(item_description + '\n')
            temp_file.write(item_quantity + '\n')
        else:
            found = True
        item_description = InventoryFile.readline()
    InventoryFile.close()
    temp_file.close()

    os.remove('Inventory.txt')
    os.rename('tempfile.txt', 'Inventory.txt')
    
    CHOICE = int(input('Enter 98 to continue or 99 to exit: '))
    if CHOICE == 98:
        menuDisplay()
    else:
        exit()
    
