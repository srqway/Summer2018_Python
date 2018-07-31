TOTAL = 0

MYLIST = [1,2,3,4,5,6,7,8,9,10]

for i in range(len(MYLIST)):
    TOTAL += MYLIST[i]
    
print(TOTAL)
##############
TOTAL = 0

for i in MYLIST:
    TOTAL += i

print(TOTAL)

################
TOTAL = 0

TOTAL = sum(MYLIST)

print(TOTAL)

