student_name = input("Enter your name: ")
gpa = float(input("Enter your gpa : "))
credit_hours = int(input("Enter your credit hours : "))

if gpa >= 3.8 and credit_hours >= 12:
    classfication = "Deans'list"
elif gpa >= 3.5 and credit_hours >= 12:
    classification = "Honor Roll"
elif gpa >= 2.0:
    classification = "Good Standing"
else:
    classification = "Academic Probation"

print(classification)