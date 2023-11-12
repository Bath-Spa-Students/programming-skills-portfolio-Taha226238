# Function to calculate the average of course marks
def calculate_average(course_marks):
    total_marks = sum(course_marks)
    average = total_marks / len(course_marks)
    return average

# Function to calculate the percentage
def calculate_percentage(course_marks, total_marks):
    total_obtained_marks = sum(course_marks)
    percentage = (total_obtained_marks / total_marks) * 100
    return percentage

# Input the number of courses and individual course marks
num_courses = int(input("Enter  number of courses: "))
course_marks = []

for i in range(num_courses):
    mark = float(input(f"Enter the marks of the course {i+1}: "))
    course_marks.append(mark)

# You can either set the total marks to 500 or take it as input from the user
# total_marks = 500  # You can uncomment this line if you want to use a fixed total marks

# Alternatively, you can take total marks from the user as input
total_marks = float(input("Enter total marks: "))

average = calculate_average(course_marks)
percentage = calculate_percentage(course_marks, total_marks)

print(f"Average of course marks: {average}")
print(f"Percentage: {percentage}%")
