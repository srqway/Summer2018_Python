class Automobile():
    def __init__(self,make,model,mileage,price):
        self.__make = make
        self.__model = model
        self.__mileage = mileage
        self.__price = price

    def set_make(self,make):
        self.__make = make
    def set_model(self,model):
        self.__model = model
    def set_mileage(self,mileage):
        self.__mileage = mileage
    def set_price(self,price):
        self.__price = price

    def get_make(self):
        return self.__make
    def get_model(self):
        return self.__model
    def get_mileage(self):
        return self.__mileage
    def get_price(self):
        return self.__price

class Trucks(Automobile):
    def __init__(self,make,model,mileage,price,towing_capacity,bed_length):
      Automobile.__init__(self,make,model,mileage,price)
      self.__towing_capacity = towing_capacity
      self.__bed_length = bed_length

    def set_towing_capacity(self,towing_capacity):
        self.__towing_capacity = towing_capacity
    def set_bed_length(self,bed_length):
        self.__bed_length = bed_length

    def get_towing_capacity(self):
        return self.__towing_capacity
    def get_bed_length(self):
        return self.__bed_length

#class SUVs(Trucks):
class SUVs(Automobile):
    def __init__(self,make,model,mileage,price,auto_hatch):
    #def __init__(self,make,model,mileage,price,towing_capacity,\
    #             bed_length,auto_hatch):
        Automobile.__init__(self,make,model,mileage,price)
        #Trucks.__init__(self,make,model,mileage,price,\
        #                towing_capacity,bed_length)
        self.__auto_hatch = auto_hatch
        
    def set_auto_hatch(self,auto_hatch):
        self.__auto_hatch = auto_hatch

    def get_auto_hatch(self):
        return self.__auto_hatch
        
