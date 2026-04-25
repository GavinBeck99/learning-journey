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