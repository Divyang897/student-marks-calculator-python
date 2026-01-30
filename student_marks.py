subjects = int(input("Enter number of subjects: "))
total = 0

for i in range(subjects):
    marks = int(input(f"Enter marks for subject {i+1}: "))
    total += marks

percentage = total / subjects

if percentage >= 75:
    grade = "A"
elif percentage >= 60:
    grade = "B"
elif percentage >= 40:
    grade = "C"
else:
    grade = "Fail"

print("Total Marks:", total)
print("Percentage:", percentage)
print("Grade:", grade)
