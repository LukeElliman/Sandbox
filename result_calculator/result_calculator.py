N_PERCENT = [0, 0.49]
P_PERCENT = [0.5, 0.64]
C_PERCENT = [0.65, 0.74]
D_PERCENT = [0.75, 0.84]
HD_PERCENT = [0.85, 1]
MIN_PERCENT = 0
MAX_PERCENT = 1
NUMERATOR = 0
DENOMINATOR = 1


def main():
    total_denominator = 0
    total_min_numerator = 0
    total_max_numerator = 0
    total_fraction_numerator = 0
    number_of_results = get_valid_integer("How many assessment pieces have you received grades for? ")
    number_of_letter_grades = get_valid_integer("How many letter results have you received? ")
    while number_of_letter_grades > number_of_results:
        print("You can't have more letter results, then total results")
        number_of_letter_grades = get_valid_integer("How many letter results have you received? ")
    # Letter based grades eg C
    for num_of_letters in range(number_of_letter_grades):
        letter_percent = turn_letter_into_percent(num_of_letters)
        assessment_weight = get_assignment_weight()
        min_numerator = letter_percent[MIN_PERCENT]*assessment_weight
        max_numerator = letter_percent[MAX_PERCENT]*assessment_weight
        total_min_numerator += min_numerator
        total_max_numerator += max_numerator
        total_denominator += assessment_weight

    # Fraction based grades eg 12/20
    for num_of_fractions in range(number_of_results - number_of_letter_grades):
        split_number_grade = get_fraction_grade(num_of_fractions, number_of_letter_grades)
        while float(split_number_grade[NUMERATOR]) > float(split_number_grade[DENOMINATOR]):
            print("Numerator can't be higher then denominator")
            split_number_grade = get_fraction_grade(num_of_fractions, number_of_letter_grades)
        assessment_weight = get_assignment_weight()
        numerator = float(split_number_grade[NUMERATOR])/(float(split_number_grade[DENOMINATOR])/assessment_weight)
        total_fraction_numerator += numerator
        total_denominator += assessment_weight

    if number_of_letter_grades >= 1:
        total_min_numerator += total_fraction_numerator
        total_max_numerator += total_fraction_numerator
        print(f"Your grade is between {total_min_numerator:,.2f}/{total_denominator:,.2f} and "
              f"{total_max_numerator:,.2f}/{total_denominator:,.2f}")
    else:
        print(f"Your grade is {total_fraction_numerator:,.2f}/{total_denominator:,.2f}")


def get_valid_integer(prompt):
    """Gets a valid integer above 1"""
    valid_input = False
    while not valid_input:
        try:
            number = int(input(prompt))
            if number < 0:
                print("Input must be 0 or above")
            elif number == "":
                print("Input can no be blank")
            else:
                valid_input = True
        except ValueError:
            print("Input must be integer")
    return number


def turn_letter_into_percent(num_of_letters):
    """Get percentage value for letter grade"""
    valid_input = False
    while not valid_input:
        letter = str(input(f"Enter the letter grade for assessment "
                           f"{num_of_letters + 1} (N, P, C, D or HD) ")).upper()
        if letter == "N":
            return N_PERCENT
        elif letter == "P":
            return P_PERCENT
        elif letter == "C":
            return C_PERCENT
        elif letter == "D":
            return D_PERCENT
        elif letter == "HD":
            return HD_PERCENT
        else:
            print("Input must be N, P, C, D or HD")


def get_fraction_grade(num_of_fractions, number_of_letter_grades):
    """Get fraction grade and split it into numerator and denominator"""
    valid_input = False
    while not valid_input:
        number_grade = str(input(f"Enter the fraction grade for assessment "
                                 f"{number_of_letter_grades + num_of_fractions + 1} (eg 12/20) "))
        if "/" not in number_grade and number_grade != "":
            print("The input must be a fraction")
        elif number_grade == "":
            print("The input can't be blank")
        else:
            valid_input = True
    split_number_grade = number_grade.split("/")
    return split_number_grade


def get_assignment_weight():
    """Get the assignment weighting"""
    valid_input = False
    while not valid_input:
        try:
            assessment_weight = float(input("Enter the letter grades,"
                                            "weight without percentage symbol "
                                            "(eg 20% becomes 20): "))
            valid_input = True
        except ValueError:
            print("Input must be a float")
    return assessment_weight


main()
