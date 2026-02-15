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

tutorial_marks = [55, 67, 43, 74, 88]

average = calculate_average(tutorial_marks)

average_student_grade = get_letter_grade(average)

print(f"Average grade: {average}")
print(f"Average tutorial letter grade: {average_student_grade}")
