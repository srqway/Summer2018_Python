def Factorial(n):
    if n == 1:
        return 1
    else:
        print("The current value of n is: ",n)
        return n * Factorial(n-1)
x = 50
print("The factorial of ", x, "is ",Factorial(x))
