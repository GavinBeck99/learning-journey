import pandas as pd
from student_analysis import get_letter_grade

students = {
    "student_id": ["S001","S002","S003","S004","S005","S006","S007","S008","S009","S010"],
    "name": ["Liam","Sophia","Noah","Emma","Oliver","Ava","Elijah","Mia","Lucas","Charlotte"],
    "assignment_1": [88, 62, 74, 91, 55, 78, 43, 85, 67, 95],
    "assignment_2": [82, 58, 79, 87, 60, 72, 48, 88, 71, 92],
    "assignment_3": [85, 65, 77, 93, 52, 75, 50, 90, 69, 97]
}

df = pd.DataFrame(students)
df["average"] = (df["assignment_1"] + df["assignment_2"] + df["assignment_3"]) / 3
df["average"] = df["average"].round(1)
df["grade"] = df["average"].apply(get_letter_grade)

hd_number = len(df[df["grade"] == "HD"])
lowest_student = df[df["average"] == df["average"].min()]
credit_or_above_students = df[df["average"] >= 65]
ranking = df.sort_values("average", ascending = False)


print(df)

print("\n--- Student Performance ---")
print(f"Class average: {df["average"].mean():.0f}")
print(f"HD number: {hd_number}")
print(f"Lowest performing student: {lowest_student["name"].values[0]}. Average mark: {lowest_student["average"].values[0]}")

print("\n--- Students With C Grade or Above ---")
print(credit_or_above_students[["name", "average", "grade"]])

print("\n--- Student Marks Filtered(Highest -> Lowest) ---")
print(ranking[["name", "average", "grade"]])