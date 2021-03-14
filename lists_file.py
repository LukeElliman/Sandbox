input_file = open("subjects.txt", "r")
subjects = input_file.readlines()
subjects = [subject.strip() for subject in subjects]
print(subjects)
input_file.close()

# for subject in subjects:
#     if subject[2] == "1":
#         print(subject)

first_year_subjects = [subject for subject in subjects if subject[2] == "1"]
print(first_year_subjects)
