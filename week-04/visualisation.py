import matplotlib.pyplot as plt
import pandas as pd

import sys
sys.path.append("../week-03")
from student_analysis import get_letter_grade

df = pd.read_csv("../week-03/students.csv")

df["average"] = (df["assignment_1"] + df["assignment_2"] + df["assignment_3"]) / 3
df["average"] = df["average"].round(1)
df["grade"] = df["average"].apply(get_letter_grade)

grade_colours = {
    "HD": "green",
    "D": "blue",
    "C": "yellow",
    "P": "orange",
    "F": "red"
}

colours = [grade_colours[grade] for grade in df["grade"]]

fig, ax = plt.subplots(figsize=(10, 6))
ax.bar(df["name"], df["average"], color = colours)
ax.set_title("Student Average Grades")
ax.set_xlabel("Student")
ax.set_ylabel("Average Grade")
ax.axhline(y=50, color="black", linestyle="--", linewidth=1, label="Pass mark")
ax.legend()
plt.tight_layout()
plt.savefig("student_averages.png")
print("Chart saved as student_averages.png")

fig2, ax2 = plt.subplots(figsize=(8, 8))
grade_counts = df["grade"].value_counts()
pie_colours = [grade_colours[grade] for grade in grade_counts.index]
ax2.pie(grade_counts, labels=grade_counts.index, autopct="%1.0f%%", colors = pie_colours)
ax2.set_title("Grade Distribution")
plt.savefig("grade_distribution.png")
print("Chart saved as grade_distribution.png")
