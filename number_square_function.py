import math


def main():
    """Main function for program"""
    number = int(input("Enter a number: "))
    squared_number = square_number(number)
    print("{0} squared is {1}".format(number, squared_number))


def square_number(value):
    """Squares a number"""
    return  value ** 2


main()