

### 5. `PROJECT_DOCUMENTATION.md`
Fulfills the 10-section documentation assessment requirement[span_10](start_span)[span_10](end_span).

```markdown
# Student Performance Analytics System – Project Documentation

## 1. Project Title
- **Project**: Student Performance Analytics System
- **Course**: Python with AI – EWB Courses

## 2. Objective
Educational institutions often handle large datasets containing student performance across multiple subjects. Manually determining grades, pass/fail status, and subject trends is error-prone. This project automates that workflow using Pandas and NumPy, offering immediate academic insights.

## 3. Technologies Used
- **Python**: Primary programming language.
- **Pandas**: Reading CSV data, managing DataFrames, and filtering records.
- **NumPy**: Matrix conversion, vector calculations, standard deviation, mean, and min/max aggregation.

## 4. Dataset Description
The dataset `students.csv` contains 20 student entries with the following fields:
- `StudentID`: Unique identifier (e.g., STU101).
- `Name`: Student's full name.
- `Department`: Academic department (CSE, ECE, IT, ME).
- `Mathematics`, `Python`, `Data_Structures`: Marks scored out of 100.
- `Attendance`: Overall attendance percentage.

## 5. Implementation
1. **Data Loading**: `pd.read_csv()` loads the dataset into memory.
2. **Numerical Processing**: Subject marks are converted into a 2D NumPy array for fast row-wise summation (`np.sum`) and averaging (`np.mean`).
3. **Grading & Pass/Fail**: A conditional function classifies averages into grades (A+, A, B, C, D, F). A validation loop checks if any subject mark falls below 40 to determine pass/fail status.
4. **Statistical Analysis**: NumPy functions (`np.mean`, `np.max`, `np.min`, `np.std`) compute subject-level and class-level statistics.
5. **Output**: Formatted outputs are printed to the console.

## 6. Key Features
- Dynamic metric computation (Total Marks, Average Marks, Grade, Pass/Fail).
- Subject-wise metrics with variance analysis.
- Extraction of Top N performers.
- Grade distribution breakdown.

## 7. Sample Output
```text
======================================================================
 CLASS PERFORMANCE SUMMARY
======================================================================
• Overall Class Average Mark : 70.92
• Highest Student Average    : 95.0 (Ananya Iyer, STU104)
• Lowest Student Average     : 37.67 (Gaurav Tiwari, STU119)
• Total Passed               : 16
• Total Failed               : 4
• Pass Percentage            : 80.0%
