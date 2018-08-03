def main():
    number_of_consonants = 0
    number_of_vowels = 0
    number_of_spaces = 0
    number_of_digits = 0
    number_of_upper = 0
    number_of_lower = 0
    total_number_of_characters = 0
    number_of_punctuation = 0

    vowels_list = ['A','a','E','e','I','i','O','o','U','u']
    #vowels_tuple = ('A','a','E','e','I','i','O','o','U','u')
    #vowels_string = 'AaEeIiOoUu'

    punctuation_list = ['.',',']
    
    testfile = open('test.txt')
    file_contents = testfile.read()
    testfile.close()
    
    #with open('test.txt') as testfile:
    #    file_contents = testfile.read()

    for ch in file_contents:
        if ch.isupper():
            number_of_upper += 1
        elif ch.islower():
            number_of_lower += 1
        elif ch.isdigit():
            number_of_digits += 1
        elif ch.isspace():
            number_of_spaces += 1

    for ch in file_contents:
        if ch in vowels_list:
            number_of_vowels += 1
        elif ch.isalpha():
            number_of_consonants += 1
        elif ch in punctuation_list:
            number_of_punctuation += 1
            
    #for ch in file_contents:
    #    total_number_of_characters += 1
    
    total_number_of_characters = number_of_digits + number_of_vowels \
                                 + number_of_consonants \
                                 + number_of_punctuation \
                                 + number_of_spaces
    
    #total_number_of_characters = len(file_contents)

    print("Consonants: ",number_of_consonants)
    print("Vowels: ",number_of_vowels)
    print("Spaces: ",number_of_spaces)
    print("Digits: ",number_of_digits)
    print("UpperCase: ",number_of_upper)
    print("LowerCase: ",number_of_lower)
    print("Punctuation: ",number_of_punctuation)
    print("Total: ",total_number_of_characters)
    

if __name__ == "__main__":
    main()
    
