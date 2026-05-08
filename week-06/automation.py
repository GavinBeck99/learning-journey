import pandas as pd
import os
from datetime import datetime

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
REPORTS_DIR = os.path.join(BASE_DIR, "reports")

os.makedirs("reports", exist_ok=True)

def create_subject_csv(subject_name, students):
    df = pd.DataFrame(students)
    df.to_csv(os.path.join(REPORTS_DIR, f"{subject_name}.csv"), index=False)
    print(f"Created: {subject_name}.csv")

maths_students = {
    "name": ["Alice", "Bob", "Charlie", "Diana", "Eve"],
    "grade": [85, 72, 91, 68, 78]
}

science_students = {
    "name": ["Alice", "Bob", "Charlie", "Diana", "Eve"],
    "grade": [79, 88, 65, 92, 71]
}

create_subject_csv("maths", maths_students)

create_subject_csv("science", science_students)

def generate_report(subject_name):
    filepath = os.path.join(REPORTS_DIR, f"{subject_name}.csv")
    df = pd.read_csv(filepath)
    print(f"\n--- {subject_name} grades ---")
    average_grade = df["grade"].mean()
    print(f"Average grade: {df["grade"].mean():.0f}")
    print(f"Highest grade: {df["grade"].max():.0f}")
    print(f"Lowest grade: {df["grade"].min():.0f}")
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"{subject_name}_{timestamp}.txt"
    with open(os.path.join(REPORTS_DIR, filename), "w") as f:
        f.write(f"--- {subject_name} grades ---\n")
        f.write(f"Average grade: {average_grade:.0f}\n")
        f.write(f"Highest grade: {df["grade"].max():.0f}\n")
        f.write(f"Lowest grade: {df["grade"].min():.0f}\n")
    

generate_report("maths")
generate_report("science")
    
