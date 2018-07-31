MYLIST = [1,2,2,3,3,6,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4]
LIST_NO_FOURS = []


for i in MYLIST:
    if i != 4:
        LIST_NO_FOURS.append(i)
        
MYLIST = LIST_NO_FOURS
        
print(MYLIST)



