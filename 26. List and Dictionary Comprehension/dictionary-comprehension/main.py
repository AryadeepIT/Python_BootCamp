import random
names = ["Arya", "Aryadeep", "Munu", "Sanchita"]


# students_score = {new_key:new_value} for item in list}
students_score = {student: random.randint(1, 100) for student in names}
print(students_score)

# passed_students = {new_key: new_val for (key, value) in dictionary.items()}
passed_students = {student: score for (student, score) in students_score.items() if score >= 60}
print(passed_students)