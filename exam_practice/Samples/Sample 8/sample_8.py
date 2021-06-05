def main():
    """Programs to double letters in sentence"""
    sentence = input("Enter your sentence ")
    doubled_letters = double_letters(sentence)
    print(doubled_letters)


def double_letters(sentence):
    """Double letters in a sentence"""
    doubled_letters = ""
    for i in range(len(sentence)):
        if sentence[i] != " ":
            for value in range(2):
                doubled_letters += sentence[i]
        else:
            doubled_letters += sentence[i]
    return doubled_letters

main()