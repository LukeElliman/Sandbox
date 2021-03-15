def main():
    """Run the program"""
    age = is_valid_age()
    print("Your age is {}".format(age))


def is_valid_age():
    """Get user input, validates it is above 0 and an integer"""
    valid_input = False
    while not valid_input:
        try:
            age = int(input("What is your age: "))
            if age >= 0:
                print("valid age")
                valid_input = True
            else:
                print("The age must not be negative")
        except ValueError:
            print("Input must be int")
    return age


main()
