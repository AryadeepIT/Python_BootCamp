student_scores = {
  "Harry": 81,
  "Ron": 78,
  "Hermione": 99, 
  "Draco": 74,
  "Neville": 62,
}


#TODO-1: Create an empty dictionary called student_grades.
student_grades = {}

#TODO-2: Write your code below to add the grades to student_grades.👇
student_grades = student_scores

for i in student_scores:
    if student_scores[i]>=91 and student_scores[i]<=100:
        student_grades[i]= "Outstanding"
    elif student_scores[i]>=81 and student_scores[i]<=90:
        student_grades[i]= "Exceeds Expectations"
    elif student_scores[i]>=71 and student_scores[i]<=80:
        student_grades[i]= "Acceptable"
    elif student_scores[i]<=71:
        student_grades[i]= "Fail"




print(student_grades)