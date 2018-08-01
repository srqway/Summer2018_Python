#!/usr/bin/env python3 

""" module.py - an example of Python module """

__counter = 0

def suml(L):
	global __counter
	__counter += 1
	SUM = 0
	for el in L:
		SUM += el
	return SUM

def prodl(L):
	global __counter	
	__counter += 1
	prod = 1
	for el in L:
		prod *= el
	return prod

if __name__ == "__main__":
	print("I prefer to be a module, but I can do some tests for you")
	l = [i+1 for i in range(5)]
	print("Below is the list created")
	print(l)
	print()
	print("Verification")
	print(suml(l) == 15)
	print(prodl(l) == 120)
	print()
	print("Messing with counter variable")
	print(__counter)
	print(__counter + 5)
