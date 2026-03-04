import pandas as pd

def get_letter_grade(average):
    if average >= 85:
        return "HD"
    elif average >= 75:
        return "D"
    elif average >= 65:
        return "C"
    elif average >= 50:
        return "P"
    else: 
        return "F"

students = {
    "name": ["Alice", "Bob", "Charlie", "Diana", "Eve"],
    "assignment 1": [72, 85, 60, 91, 78],
    "assignment 2": [68, 79, 55, 88, 82],
    "assignment 3": [74, 83, 61, 95, 80]
}

df = pd.DataFrame(students)

df["average"] = (df["assignment 1"] + df["assignment 2"] + df["assignment 3"]) / 3

df["average"] = df["average"].round(1)

df["grade"] = df["average"].apply(get_letter_grade)

print(df)

print("\n--- Student Performance Report ---")
print(f"Class average: {df["average"].mean():.0f}")
print(f"Highest average: {df["average"].max():.0f}")
print(f"Lowest average: {df["average"].min():.0f}")
passing = len(df[df["average"] >= 50])
print(f"Students passing: {passing} out of {len(df)}")