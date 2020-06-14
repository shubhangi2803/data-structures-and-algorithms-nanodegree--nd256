names=input('Names : ').split(',')
assignments=input('Assignments : ').split(',')
grades=input('Grades : ').split(',')

print(names)
print(assignments)
print(grades)

# names = []
# assignments = []
# grades = []
# for i in range(3):names.append(input("Name: "))
# for i in range(3):assignments.append(input("Assignments: "))
# for i in range(3):grades.append(input("Grades: "))


# message string to be used for each student
# HINT: use .format() with this string in your for loop
for i in range(len(names)):
    message = "Hi {},\n\nThis is a reminder that you have {} assignments left to \
    submit before you can graduate. You're current grade is {} and can increase \
    to {} if you submit all assignments before the due date.\n\n".format(names[i],assignments[i],grades[i],int(grades[i])+2*int(assignments[i]))
    print(message)


# names = input("Enter names separated by commas: ").title().split(",")
# assignments = input("Enter assignment counts separated by commas: ").split(",")
# grades = input("Enter grades separated by commas: ").split(",")
#
# message = "Hi {},\n\nThis is a reminder that you have {} assignments left to \
# submit before you can graduate. You're current grade is {} and can increase \
# to {} if you submit all assignments before the due date.\n\n"
#
# for name, assignment, grade in zip(names, assignments, grades):
#     print(message.format(name, assignment, grade, int(grade) + int(assignment)*2))
