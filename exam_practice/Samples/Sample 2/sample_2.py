def main():
    """Program to square age to zero"""
    age = get_valid_int("Enter your age ")
    for i in range(age):
        print(i)
        print(age-i)
        # print((age-i)**2)

def get_valid_int(prompt):
    """Get valid integer"""
    valid = False
    while not valid:
        try:
            age = int(input(prompt))
            if age > 0:
                return age
            else:
                print("Age must be above 0")
        except ValueError:
            print("Enter an integer")

main()