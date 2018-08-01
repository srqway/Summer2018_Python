def recursive_function(number):
    a = 0
    b = 1
    for i in range(0,number):
        temp = a
        a = b
        b += temp
    return a   

def iterative_function(number):
    fiblist = [0,1]
    i = 2
    while i <= number:
        fiblist.append(fiblist[i - 1] + fiblist[i - 2])
        i += 1
    return fiblist


#for i in range(0,15):
#    print(recursive_function(i),end=',')
    
print(iterative_function(15),end=',')
