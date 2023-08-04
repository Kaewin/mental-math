import random




def two_digit_addition():

    status = False

    number_1 = random.randint(10, 99)
    number_2 = random.randint(10, 99)

    sum = number_1 + number_2
    print(sum)

    print(number_1, 
          "\n", 
          number_2, 
          "\n", 
          "------------")
    
    val = input("Enter your answer: ")
    val = int(val)    

    while (status == False):

        if val == sum:
            print("Correct")
            status = True
        if val != sum:
            val = input("Try again: ")
            val = int(val)



    return


#def three_digit_addition():


#def two_digit_subtraction():

#def three_digit_subtraction():


def number_generator(base, length):

    number = random.randint(base, length)

    return number


def main():

    print("Welcome to the mental math trainer.")
    print("What would you like to do?")

    print("Two-Digit Addition\nThree-Digit Addition\nTwo-Digit Subtraction\nThree-Digit Subtraction")

    two_digit_addition()

    return  

if __name__ == "__main__":
    main()