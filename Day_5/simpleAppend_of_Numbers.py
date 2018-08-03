def main():
    numbers_file = open("Numbers.txt",'a')
    
    num1 = 6
    num2 = 7
    num3 = 8

    numbers_file.write(str(num1) + '\n')
    numbers_file.write(str(num2) + '\n')
    numbers_file.write(str(num3) + '\n')
    
    numbers_file.close()

if __name__ == "__main__":
    main()
