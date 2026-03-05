import pandas as pd
from student_analysis import get_letter_grade 

df = pd.read_csv("students.csv")

df["average"] = (df["assignment_1"] + df["assignment_2"] + df["assignment_3"]) / 3

df["average"] = df["average"].round(1)

df["grade"] = df["average"].apply(get_letter_grade)

print("\n--- Student Performance Report ---")
print(f"Class average: {df['average'].mean():.0f}")
print(f"Highest average: {df['average'].max():.0f}")
print(f"Lowest average: {df['average'].min():.0f}")
passing = len(df[df["average"] >= 50])
print(f"Students passing: {passing} out of {len(df)}")