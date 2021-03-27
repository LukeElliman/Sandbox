class User:
    def __init__(self, name="", score=0):
        self.name = name
        self.number_of_tacos = 5
        self.score = score

    def __str__(self):
        return "{} {} {}".format(self.name, self.number_of_tacos, self.score)

    def __give__(self):
        self.number_of_tacos -= give_amount
        return self.number_of_tacos



name = str(input("Name: "))
score = int(input("Score: "))

user1 = User(name, score)


print("{}, {} points, {} tacos left".format(user1.name, user1.score, user1.number_of_tacos))
give_choice = str(input("Do you want to give any tacos (Y/N): "))
if give_choice == "Y":
    give_amount = int(input("How many? "))
    user1.__give__()
    print("{}, {} points, {} tacos left".format(user1.name, user1.score, user1.number_of_tacos))
else:
    print("bye")