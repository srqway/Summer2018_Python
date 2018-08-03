import os
### Remember to put all print statements in ()

def menuDisplay():
    print '============================='
    print '= Inventory Management Menu ='
    print '============================='
    print '(1) Add New Item to Inventory'
    print '(2) Remove Item from Inventory'
    print '(3) Update Inventory'
    print '(4) Search Item in Inventory'
    print '(5) Print Inventory Report'
    print '(99) Quit'
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
    print 'Adding Inventory'
    print '================'
    item_description = input("Enter the name of the item: ")
    item_quantity = int(input("Enter the quantity of the item: "))
    
    InventoryFile = open('Inventory.txt', 'a')
    InventoryFile.write(item_description + '\n')
    InventoryFile.write(str(item_quantity) + '\n')

    InventoryFile.close()

    CHOICE = int(input('Enter 98 to continue or 99 to exit: '))
    if CHOICE == 98:
            menuDisplay()
    else:
        exit()

def removeInventory():
    print 'Removing Inventory'
    print '================'
    item_search = input('Enter the item name to remove from inventory: ')

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
    
def updateInventory():
    print 'Updating Inventory'
    print '================'
    item_search = input('Enter the item to update: ')
    quantity_update = int(input(('Enter the updated quantity. Enter 5 for additional or -5 for less: ')))

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
            temp_file.write(item_description + '\n')
            item_quantity = int(item_quantity)
            new_quantity = item_quantity + quantity_update
            new_quantity = str(new_quantity)
            temp_file.write(new_quantity + '\n')
            
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
    
def searchInventory():
    print 'Searching Inventory'
    print '================'
    item_found = False
    
    search_item = input('Enter the name of the item: ')

    InventoryFile = open('Inventory.txt', 'r')
    item_description = InventoryFile.readline()
    
    while item_description != '':
        item_quantity = float(InventoryFile.readline())
        item_description = item_description.rstrip('\n')

        if search_item == item_description:
            print 'Item:    ', item_description
            print 'Quanity: ', item_quantity
            print '---------'
            item_found = True
        item_description = InventoryFile.readline()
        
    InventoryFile.close()

    if not item_found:
        print 'The item was not found in the file.  Please add to inventory if needed'

    CHOICE = int(input('Enter 98 to continue or 99 to exit: '))
    if CHOICE == 98:
       menuDisplay()
    else:
        exit()
    
def printInventory():
    InventoryFile = open('Inventory.txt', 'r')
    item_description = InventoryFile.readline()
    print 'Current Inventory'
    print '-----------------'
    while item_description != '':
        item_quantity = InventoryFile.readline()
        item_description = item_description.rstrip('\n')
        item_quantity = item_quantity.rstrip('\n')
        print 'Item:     ', item_description
        print 'Quantity: ', item_quantity
        print '----------'
        item_description = InventoryFile.readline()
    InventoryFile.close()

    CHOICE = int(input('Enter 98 to continue or 99 to exit: '))
    if CHOICE == 98:
            menuDisplay()
    else:
        exit()
    
menuDisplay()
