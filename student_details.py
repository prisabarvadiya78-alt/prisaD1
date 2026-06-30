import pandas as pd

student_detail = {
    "roll_no": [101, 102, 103, 104, 105],
    "name": ["Raj", "Priya", "Het", "Nishtha", "Karan"],
    "gender": ["Male", "Female", "Male", "Female", "Male"],
    "course": ["BCA", "B.Com", "BSc IT", "BBA", "BCA"],
    "marks": [85, 92, 78, 88, 95]
}

df = pd.DataFrame(student_detail)

print("Student Details:")
print(df)

print("\n\nstudents informations")
print(df.info())

print("\n\nstudents description")
print(df.describe())