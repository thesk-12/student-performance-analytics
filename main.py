"""
main.py
Main entry point for the Student Performance Analytics System.
"""

import numpy as np
import pandas as pd
from functions import (
    load_dataset,
    process_student_data,
    generate_subject_analysis,
    get_top_performers,
    SUBJECTS,
)


def display_header(title):
    print("\n" + "=" * 70)
    print(f" {title}")
    print("=" * 70)


def main():
    display_header("STUDENT PERFORMANCE ANALYTICS SYSTEM")

    # Step 1: Read and inspect dataset
    df = load_dataset("students.csv")
    if df is None:
        return

    print(f"[✓] Dataset loaded successfully. Total Records: {len(df)}")
    print(f"[✓] Columns: {list(df.columns)}")

    # Step 2: Process Data
    df_processed = process_student_data(df)

    # Step 3: Display Processed Records
    display_header("PROCESSED STUDENT RECORDS (SAMPLE)")
    cols_to_show = ["StudentID", "Name", "Department", "Total_Marks", "Average_Marks", "Grade", "Status"]
    print(df_processed[cols_to_show].to_string(index=False))

    # Step 4: Core Class Analytics
    display_header("CLASS PERFORMANCE SUMMARY")
    all_averages = df_processed["Average_Marks"].to_numpy()

    overall_avg = np.round(np.mean(all_averages), 2)
    highest_avg = np.max(all_averages)
    lowest_avg = np.min(all_averages)

    top_student = df_processed.loc[df_processed["Average_Marks"].idxmax()]
    lowest_student = df_processed.loc[df_processed["Average_Marks"].idxmin()]

    passed_count = (df_processed["Status"] == "Pass").sum()
    failed_count = (df_processed["Status"] == "Fail").sum()
    pass_percentage = np.round((passed_count / len(df_processed)) * 100, 2)

    print(f"• Overall Class Average Mark : {overall_avg}")
    print(f"• Highest Student Average    : {highest_avg} ({top_student['Name']}, {top_student['StudentID']})")
    print(f"• Lowest Student Average     : {lowest_avg} ({lowest_student['Name']}, {lowest_student['StudentID']})")
    print(f"• Total Passed               : {passed_count}")
    print(f"• Total Failed               : {failed_count}")
    print(f"• Pass Percentage            : {pass_percentage}%")

    # Step 5: Subject-Wise Performance Analysis
    display_header("SUBJECT-WISE PERFORMANCE ANALYSIS")
    subject_analysis = generate_subject_analysis(df_processed)
    print(subject_analysis.to_string())

    best_subject = subject_analysis["Average"].idxmax()
    print(f"\n[→] Best performing subject by average: {best_subject} ({subject_analysis.loc[best_subject, 'Average']})")

    # Step 6: Grade Distribution
    display_header("GRADE DISTRIBUTION")
    grade_counts = df_processed["Grade"].value_counts().sort_index()
    for grade, count in grade_counts.items():
        print(f"• Grade {grade:<2} : {count} student(s)")

    # Step 7: Top Performers (Top 3)
    display_header("TOP 3 PERFORMING STUDENTS")
    top_3 = get_top_performers(df_processed, n=3)
    print(top_3[["StudentID", "Name", "Department", "Average_Marks", "Grade"]].to_string(index=False))

    print("\n" + "=" * 70)
    print(" Analysis complete. All calculations verified.")
    print("=" * 70 + "\n")


if __name__ == "__main__":
    main()
