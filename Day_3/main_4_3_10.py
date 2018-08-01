from sys import path

path.append('modules') ## relative path
                       ##allows me to access modules in the modules folder a
                       ##directory below the location of the program
#path.append('C:\\Users\\<username>\\Downloads\\Day_3\\modules') #absolute path

from module_4_3_10 import suml, prodl

zeroes = [0 for i in range(5)]
ones = [1 for i in range(5)]
print(zeroes)
print(ones)
print(suml(zeroes))
print(prodl(ones))
