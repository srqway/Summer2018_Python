def main(): #void function
    print("This is my first function")
    
def anotherfunction(): #void function
    print("This is another function")

def square(x,y): #value returning functioning 2 parameters (x and y)
    return x ** y
    
def quotient(x,y):
    value = x * y
    print(value)
    

main()
anotherfunction()
quotient(2,3)
print(square(2,6)) #invoke function square and pass 2 args 2 and 6

