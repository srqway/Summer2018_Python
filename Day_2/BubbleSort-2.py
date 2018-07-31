number_of_items = int(input("How many numbers are in the list? "))
                       
number_list = []
    
for x in range(number_of_items):
    number = int(input("Enter a number: "))
    number_list.append(number)

print("Here is the original list ", number_list)

for i in range(len(number_list) - 1, 0, -1):
    for j in range(i):
        if number_list[j] > number_list[j + 1]:
            number_list[j], number_list[j + 1] = number_list[j + 1], number_list[j]
            print (number_list)
