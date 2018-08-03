def power(L):
	list2 = []
	for i in L:
		z = 2 ** i
		list2.append(z)
	print(list2)

list1 = [0,1,2,3,4]
power(list1)

#####################################

list1 = [x for x in range(5)]

list2 = list(map(lambda z: 2 ** z, list1)) 

print(list2)

for x in map(lambda x: x * x, list2):
    print(x,end=" ")
    
