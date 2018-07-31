number_of_items = int(input("How many numbers are in the list? "))
                       
number_list = []
    
for x in range(number_of_items):
    number = int(input("Enter a number: "))
    number_list.append(number)

working_ascending_list = [] #This is used for sorting
   
i = 0 #This is track values in the list
    
lowest_number = number_list[0] #assume that first number is the lowest
                     
#sort low to high            
while len(number_list) > 0: #making sure the entire list is analyzed
    if number_list[i] < lowest_number: #is the current number less than the lowest
        lowest_number = number_list[i] #ensure there is a new lowest number
    i += 1 #move to next number in the list

    if i == len(number_list): # has the end of the list been reached?
        working_ascending_list.append(lowest_number) #put lowest number in the working list
        number_list.remove(lowest_number) #remove that number from the original list
        if number_list: #is the number_list still present?
            lowest_number = number_list[0] #assign a new lowest number from the original list
        i = 0 #reset the position in the list to the first number
            
print(working_ascending_list)
    
