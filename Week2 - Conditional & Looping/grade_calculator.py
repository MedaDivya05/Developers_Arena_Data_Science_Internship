# Week 2 Project: Student Grade Calculator

# Function to calculate grade and return a message based on marks
def calculate_grade(marks):
    """Returns grade and encouraging message based on marks."""
    
    # Check if marks are between 90 and 100
    if 90 <= marks <= 100:
        return "A", "Excellent work! Keep shining!"
    
    # Check if marks are between 80 and 89
    elif 80 <= marks <= 89:
        return "B", "Very Good! Keep it up!"
    
    # Check if marks are between 70 and 79
    elif 70 <= marks <= 79:
        return "C", "Good job! You can do even better!"
    
    # Check if marks are between 60 and 69
    elif 60 <= marks <= 69:
        return "D", "Nice effort! Keep practicing!"
    
    # If marks are below 60, assign grade F
    else:
        return "F", "Don't give up! Keep learning and improving!"

# Function to take valid marks input from the user
def get_valid_marks():
    """Gets valid marks input between 0 and 100 using while loop."""
    
    # Loop until the user enters a valid number
    while True:
        try:
            # Take input and convert it to integer
            marks = int(input("Enter marks (0-100): "))
            
            # Check if marks are within valid range
            if 0 <= marks <= 100:
                return marks
            else:
                print("Invalid input! Marks must be between 0 and 100.")
        
        # Handle case where input is not a number
        except ValueError:
            print("Invalid input! Please enter numbers only.")

# Main Program starts here
print("=" * 60)
print("WELCOME TO THE STUDENT GRADE CALCULATOR")
print("=" * 60)

# Take student name as input
student_name = input("Enter student name: ")

# Get valid marks from user
marks = get_valid_marks()

# Call function to calculate grade and message
grade, message = calculate_grade(marks)

# Display the result
print("\n" + "=" * 60)
print(f"RESULT FOR {student_name.upper()}:")
print(f"Marks: {marks}/100")
print(f"Grade: {grade}")
print(f"Message: {message}")
print("=" * 60)

# Display grading scale for user reference
print("\nGrading Logic:")
print("A: 90-100")
print("B: 80-89")
print("C: 70-79")
print("D: 60-69")
print("F: 0-59")