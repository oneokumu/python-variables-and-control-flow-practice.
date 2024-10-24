# Ask the user for the score
score = int(input("Enter the score (0-100): "))

# Categorize the score into a grade
if 90 <= score <= 100:
    grade = 'A'
elif 80 <= score < 90:
    grade = 'B'
elif 70 <= score < 80:
    grade = 'C'
elif 60 <= score < 70:
    grade = 'D'
elif 0 <= score < 60:
    grade = 'F'
else:
    grade = 'Invalid score'

# Print the grade
if grade != 'Invalid score':
    print(f"Your grade is: {grade}")
else:
    print("Please enter a valid score between 0 and 100.")
