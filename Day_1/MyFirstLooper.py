MAX_NUMBER = -99999999
COUNTER = 0

while True:
    NUMBER = int(input("Enter a number (enter -1 to stop): "))
    if NUMBER == -1:
        break
    COUNTER += 1
    if NUMBER > MAX_NUMBER:
        MAX_NUMBER = NUMBER

if COUNTER:
    print("The largest number is ",MAX_NUMBER)
else:
    print("You have not entered a value!!")
        
        
