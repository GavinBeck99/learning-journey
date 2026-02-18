def calculate_average(grades):
    sum_of_grades = sum(grades)
    number_of_grades = len(grades)

    grade_average = sum_of_grades / number_of_grades
    
    return grade_average

def get_letter_grade(average):
    if average >= 85:
        return "HD"
    elif average >= 75:
        return "D"
    elif average >= 65:
        return "C"
    elif average >= 50:
        return "P"
    else : return "F"

def find_highest_grade(grades):
    return max(grades)

def find_lowest_grade(grades):
    return min(grades)

def count_passing(grades, passing_mark):
    count = 0
    for grade in grades:
        if grade >= passing_mark:
            count += 1
    return count

tutorial_marks = [55, 67, 43, 74, 88]

average = calculate_average(tutorial_marks)
average_student_grade = get_letter_grade(average)
highest_grade = find_highest_grade(tutorial_marks)
lowest_grade = find_lowest_grade(tutorial_marks)
number_of_passing_students = count_passing(tutorial_marks, 50)

print(f"Average grade: {average}")
print(f"Average tutorial letter grade: {average_student_grade}")
print(f"Highest grade: {highest_grade}")
print(f"Lowest grade: {lowest_grade}")
print(f"Number of students that have passed: {number_of_passing_students} out of {len(tutorial_marks)}")
