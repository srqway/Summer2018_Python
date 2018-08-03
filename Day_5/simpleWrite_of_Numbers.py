def main():
    numbers_file = open("Numbers.txt",'w')
    
    num1 = 0
    num2 = 1
    num3 = 2

    numbers_file.write(str(num1) + '\n')
    numbers_file.write(str(num2) + '\n')
    numbers_file.write(str(num3) + '\n')
    
    numbers_file.close()

if __name__ == "__main__":
    main()
