MYLIST = []

for i in range(1,10):
    MYLIST.append(i)
    
print(MYLIST)

for i in range(5):
    MYLIST.insert(0, i + 10)

print(MYLIST)

for i in range(5):
    del MYLIST[0]

print(MYLIST)
