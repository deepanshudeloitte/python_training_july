import json

# Load grades from a JSON file
with open('grades.json') as f:
    grades = json.load(f)

# Calculate average grade for each student
averages = {}
highest_average = 0.0
highest_student = ''

print("Grades Analysis:\n")

for student, student_grades in grades.items():
    average = sum(student_grades) / len(student_grades)
    averages[student] = average

    print(f"Student: {student}")
    print(f"Average Grade: {average:.2f}\n")

    if average > highest_average:
        highest_average = average
        highest_student = student

print("Student with the highest average grade:")
print(f"Name: {highest_student}")
print(f"Average Grade: {highest_average:.2f}")
