from random import randint

class Coin():  #name of the class created
    
    #self allows all methods in the class to access the variables.  For example
    #self.__sideup can be used in all methods of this class. If a new variable
    #(x) is declared, only the method in which x is declared can use the variable
    #if self. is added to the variable x, then it can be used by all methods
    #While not a requirement, it is best practice to use self.

    #__init__ is a constructor
    def __init__(self): #is executed upon instantiation of the object
        self.__sideup = 'Tails' #assigning a property it's value
        #self.sideup = 'Tails' #public/global variable
        
    #toss is a mutator
    def toss(self): #activity to simulate the tossing of a coin in the air
        if randint(0,1) == 0: #using randint to determine heads/tails
            self.__sideup = 'Heads' #assigning value
            #self.sideup = 'Heads'  #public/global variable
        else:
            self.__sideup = 'Tails' #assigning value
            #self.sideup = 'Tails'  #public/global variable
              
    #get_sideup is an accessor
    def get_sideup(self):  #activity to show the value of the coin facing up
        return self.__sideup #return the value of the variable
        #return self.sideup  #public/global variable

#code below is NOT a part of the class created above

def main():
    myCoin = Coin() #creating an object using the Coin class (instantiation)
    print("The current side of the coin showing is", myCoin.get_sideup())
    print("Tossing the coin.........")
    myCoin.toss()
    #myCoin.sideup = "I got you fooled" #use this to demonstrate how to manipulate
                                        #variable inside class (uncomment public/
                                        #global variable and comment out double
                                        #underscore variables
    print("After the toss the side of the coin showing is", myCoin.get_sideup())
    
if __name__ == "__main__":
    main()
    
    
    




        
        
    


    
