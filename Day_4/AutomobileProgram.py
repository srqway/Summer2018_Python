import Automobiles

def main():
    used_truck = Automobiles.Trucks('Dodge','2013','35000','25000','Y','8ft')
    print("Make: ",used_truck.get_make()) #defined in superclass
    print("Model: ",used_truck.get_model()) #defined in superclass
    print("Towing: ",used_truck.get_towing_capacity()) #defined in subclass
    print("Bed Length: ",used_truck.get_bed_length()) #defined in subclass
    print()
    
    used_suv = Automobiles.SUVs('Honda','2016','28656','29599','Y')
    print("Make: ",used_suv.get_make()) #defined in superclass
    print("Model: ",used_suv.get_model()) #defined in superclass
    #print("Towing Capacity: ",used_suv.get_towing_capacity())
    print("Auto Hatch: ",used_suv.get_auto_hatch()) #defined in subclass
    

if __name__ == "__main__":
    main()
