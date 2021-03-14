scores = []
score = int(input("Score: "))
while score >= 0:
    scores.append(score)
    score = int(input("Score: "))

if scores == []:
    print("List is empty")
else:
    print("Your highest score is {}".format(max(scores)))
