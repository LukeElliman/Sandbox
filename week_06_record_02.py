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

    def __add_tacos__(self):
        self.number_of_tacos += give_amount
        return self.number_of_tacos


name = str(input("Name: "))
score = int(input("Score: "))

user1 = User(name, score)

name = str(input("Name: "))
score = int(input("Score: "))

user2 = User(name, score)


print("{}, {} points, {} tacos left".format(user1.name, user1.score, user1.number_of_tacos))
print("{}, {} points, {} tacos left".format(user2.name, user2.score, user2.number_of_tacos))

give_choice = str(input("Do you want to give any tacos to user 1 (Y/N): "))
if give_choice == "Y":
    give_amount = int(input("How many? "))
    user2.__give__()
    user1.__add_tacos__()
    print("User 2 {}, {} points, {} tacos left".format(user2.name, user2.score, user2.number_of_tacos))
    print("User 1 {}, {} points, {} tacos left".format(user1.name, user1.score, user1.number_of_tacos))
else:
    print("bye")