def main():
    numbers_file = open("Numbers.txt",'r')
    
    #line1 = numbers_file.readline().rstrip('\n')
    #line2 = numbers_file.readline().rstrip('\n')
    #line3 = numbers_file.readline().rstrip('\n')

    #line1 = line1.rstrip('\n')
    #line2 = line2.rstrip('\n')
    #line3 = line3.rstrip('\n')
    
    contents_of_file = numbers_file.read()

    numbers_file.close()

    #print(line1)
    #print(line2)
    #print(line3)
    
    print(contents_of_file)

if __name__ == "__main__":
    main()
