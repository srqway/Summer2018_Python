import os

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
