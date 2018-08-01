def main(x,y):
    try:
        quotient = x / y
        print(quotient)
    except ZeroDivisionError:
        print("No divide by zero")
    except ArithmeticError:
        print("You can't divide by zero")
    except ValueError:
        print("Bad value")
    except TypeError:
        print("Bad type")
    except:
        print("Something bad happened")

def oops():
    raise IndexError #for exception testing

if __name__ == "__main__":
    try:
        num1 = float(input("Enter a number: "))
        assert num1 > 0
        num2 = float(input("Enter another number: "))
        assert num3 > 0
        main(num1,num2)
        oops()
    except ValueError:
        print("You must enter a number!!")
    
