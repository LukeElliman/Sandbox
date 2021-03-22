def main():
    """Convert list of numbers to positives and negatives"""
    numbers = [-8, 3, 4, 5, -3, -5]
    display_numbers(numbers)


def display_numbers(numbers):
    negatives = []
    positives = []
    for number in range(len(numbers)):
        if numbers[number] < 0:
            negatives.append(numbers[number])
        else:
            positives.append(numbers[number])
    print("negatives {}".format(negatives))
    print("positives {}".format(positives))


main()
