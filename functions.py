"""
functions.py
Reusable calculation and data processing functions for the Student Performance Analytics System.
"""

import numpy as np
import pandas as pd

SUBJECTS = ["Mathematics", "Python", "Data_Structures"]


def load_dataset(filepath="students.csv"):
    """Load student dataset into a Pandas DataFrame."""
    try:
        df = pd.read_csv(filepath)
        return df
    except FileNotFoundError:
        print(f"[!] Error: File '{filepath}' not found.")
        return None


def calculate_grade(average):
    """
    Assign grade based on clear standard rules:
    >= 90: A+, >= 80: A, >= 70: B, >= 60: C, >= 50: D, < 50: F
    """
    if average >= 90:
        return "A+"
    elif average >= 80:
        return "A"
    elif average >= 70:
        return "B"
    elif average >= 60:
        return "C"
    elif average >= 50:
        return "D"
    else:
        return "F"


def check_pass_fail(row, pass_mark=40):
    """
    Determine pass/fail status.
    Condition: Student must score at least 40 marks in every subject.
    """
    for subject in SUBJECTS:
        if row[subject] < pass_mark:
            return "Fail"
    return "Pass"


def process_student_data(df):
    """
    Calculate totals, averages, grades, and pass/fail statuses
    using NumPy arrays and iteration loops.
    """
    marks_matrix = df[SUBJECTS].to_numpy()

    # NumPy calculations
    totals = np.sum(marks_matrix, axis=1)
    averages = np.round(np.mean(marks_matrix, axis=1), 2)

    df["Total_Marks"] = totals
    df["Average_Marks"] = averages

    # Loop to assign grades
    grades = []
    for avg in df["Average_Marks"]:
        grades.append(calculate_grade(avg))
    df["Grade"] = grades

    # Row iteration loop for pass/fail determination
    status_list = []
    for _, row in df.iterrows():
        status_list.append(check_pass_fail(row))
    df["Status"] = status_list

    return df


def generate_subject_analysis(df):
    """Calculate average, highest, and lowest marks per subject using NumPy."""
    subject_stats = {}
    for sub in SUBJECTS:
        marks = df[sub].to_numpy()
        subject_stats[sub] = {
            "Average": np.round(np.mean(marks), 2),
            "Highest": np.max(marks),
            "Lowest": np.min(marks),
            "Median": np.median(marks),
            "Std_Dev": np.round(np.std(marks), 2),
        }
    return pd.DataFrame(subject_stats).T


def get_top_performers(df, n=3):
    """Return the top n performing students sorted by average marks."""
    return df.sort_values(by="Average_Marks", ascending=False).head(n)
