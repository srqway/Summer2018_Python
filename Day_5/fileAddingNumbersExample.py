import os

def main():
    if os.path.isfile('Numbers.txt'):
        print("File exists")
        
    names_file = open('Numbers.txt','r')

    line1 = int(names_file.readline().rstrip('\n'))
    line2 = int(names_file.readline().rstrip('\n'))
    line3 = int(names_file.readline().rstrip('\n'))
    
    total = line1 + line2 + line3
    print("The total is",total)

    names_file.close()

main()
