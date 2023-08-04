import random




#def two_digit_addition():


#def three_digit_addition():


#def two_digit_subtraction():

#def three_digit_subtraction():

def number_generator(base, length):

    number = random.randint(base, length)

    return number

def main():
    print(number_generator(100, 399))

    return  

if __name__ == "__main__":
    main()