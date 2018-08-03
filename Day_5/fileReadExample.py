try:
    def file_close():
        numbers_file.close()
    
        if numbers_file.closed:
            print("The file is closed")
            
    def main():
        global numbers_file 
        numbers_file = open('Numbers.txt','r')
        
        print("Name of file is: ", numbers_file.name)
        print(numbers_file.name, "is open in",numbers_file.mode,"mode")
    
        first_line = numbers_file.readline().rstrip('\n')
        second_line = numbers_file.readline().rstrip('\n')
        third_line = numbers_file.readline().rstrip('\n')
              
        print("The current line content is: ")
        print(third_line)

        file_close()
   
    main()
    
except FileNotFoundError as bob:
    print("File not found")
    print(bob)

    

