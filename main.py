import random

def two_digit_addition():

    counter = 0
    print("How many practice problems would you like?")
    iterations = int(input())

    while counter != iterations:

        print("Currently on problem: ", counter)

        status = False

        number_1 = random.randint(10, 99)
        number_2 = random.randint(10, 99)

        sum = number_1 + number_2

        print("  ", 
            number_1, 
            "\n", 
            "+",
            number_2, 
            "\n", 
            "-----")
        
        val = input("Enter your answer: ")
        val = int(val)    

        while (status == False):

            if val == sum:
                print("Correct")
                print()
                status = True
            if val != sum:
                print("Try again\n")
                print("  ", 
                    number_1, 
                    "\n", 
                    "+",
                    number_2, 
                    "\n", 
                    "-----")
                
                val = input("Enter your answer: ")
                val = int(val)  

        counter += 1

    return

def three_digit_addition():

    counter = 0
    print("How many practice problems would you like?")
    iterations = int(input())

    while counter != iterations:
    
        print("Currently on problem: ", counter")

        status = False

        number_1 = random.randint(100, 999)
        number_2 = random.randint(100, 999)

        sum = number_1 + number_2

        print("  ", 
            number_1, 
            "\n", 
            "+",
            number_2, 
            "\n", 
            "-----")
        
        val = input("Enter your answer: ")
        val = int(val)    

        while (status == False):

            if val == sum:
                print("Correct")
                print()
                status = True
            if val != sum:
                print("Try again\n")
                print("  ", 
                    number_1, 
                    "\n", 
                    "+",
                    number_2, 
                    "\n", 
                    "-----")
                
                val = input("Enter your answer: ")
                val = int(val)  

        counter += 1

    return

def two_digit_subtraction():

    counter = 0
    print("How many practice problems would you like?")
    iterations = int(input())

    while counter != iterations:
    
        print("Currently on problem: ", counter")

        status = False

        number_1 = random.randint(10, 99)
        number_2 = random.randint(10, 99)

        sum = number_1 - number_2

        print("  ", 
            number_1, 
            "\n", 
            "-",
            number_2, 
            "\n", 
            "-----")
        
        val = input("Enter your answer: ")
        val = int(val)    

        while (status == False):

            if val == sum:
                print("Correct")
                print()
                status = True
            if val != sum:
                print("Try again\n")
                print("  ", 
                    number_1, 
                    "\n", 
                    "+",
                    number_2, 
                    "\n", 
                    "-----")
                
                val = input("Enter your answer: ")
                val = int(val) 

        counter += 1 

    return

def three_digit_subtraction():

    counter = 0
    print("How many practice problems would you like?")
    iterations = int(input())

    while counter != iterations:
    
        print("Currently on problem: ", counter")
              
        status = False

        number_1 = random.randint(100, 999)
        number_2 = random.randint(100, 999)

        sum = number_1 - number_2

        print("  ", 
            number_1, 
            "\n", 
            "-",
            number_2, 
            "\n", 
            "-----")
        
        val = input("Enter your answer: ")
        val = int(val)    

        while (status == False):

            if val == sum:
                print("Correct")
                print()
                status = True
            if val != sum:
                print("Try again\n")
                print("  ", 
                    number_1, 
                    "\n", 
                    "+",
                    number_2, 
                    "\n", 
                    "-----")
                
                val = input("Enter your answer: ")
                val = int(val)  

        counter += 1

    return

def number_generator(base, length):

    number = random.randint(base, length)

    return number

def menu():

    print("\nWelcome to the mental math trainer.")
    print("What would you like to do?\n")

    print("1 Two-Digit Addition\n2 Three-Digit Addition\n3 Two-Digit Subtraction\n4 Three-Digit Subtraction\n")

    selection = input("Input your selection: ")
    selection = int(selection)
    print()

    if selection == 1:
    
        two_digit_addition()

    if selection == 2:

        three_digit_addition() 

    if selection == 3:

        two_digit_subtraction() 

    if selection == 4:

        three_digit_subtraction() 

def main():

    menu()
    
    return

if __name__ == "__main__":
    main()