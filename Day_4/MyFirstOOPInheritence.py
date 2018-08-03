class Person():
    def __init__(self,first,last):
        self.__firstname = first
        self.__lastname = last

    #def get_name(self):
    def __str__(self): #__str__ special like __init__ but is invoked
                       #automatically upon print(object)
        return self.__firstname + " " + self.__lastname

class Employee(Person):
    def __init__(self,first,last,empID):
        #Person.__init__(self,first,last)
        super().__init__(first,last)
        self.__empID = empID

    #def get_employee(self):
        #return self.get_name() + " " + self.__empID
    def __str__(self):
        return super().__str__() + " " + self.__empID
        
    
class Programmer(Employee):
    def __init__(self,first,last,empID,language):
        #Employee.__init__(self,first,last,empID)
        super().__init__(first,last,empID)
        self.__language = language

    #def get_programmer(self):
        #return self.get_name() + " " + self.__language
    def __str__(self):
        return super().__str__() + " " + self.__language
         
### Below is my code for these classes


def main():
    fname = input("Enter your first name: ")
    lname = input("Enter your last name: ")
    empID = input("Enter the employee ID: ")
    language = input("Enter their prefered language: ")

    person1 = Person(fname,lname)
    employee1 = Employee(fname,lname,empID)
    programmer1 = Programmer(fname,lname,empID,language)

    #print(person1.get_name())
    print(person1)
    
    #print(employee1.get_employee())
    print(employee1)
    
    #print(programmer1.get_programmer())
    print(programmer1)


if __name__ == "__main__":
    main()

        
