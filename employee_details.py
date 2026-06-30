import pandas as pd

employee_detail = {
    "employee_id": [201, 202, 203, 204, 205],
    "name": ["Riya", "Priya", "Aksha", "mahek", "Krisha"],
    "department": ["HR", "Sales", "IT", "Finance", "Marketing"],
    "salary": [35000, 42000, 50000, 45000, 38000],
    "experience": [2, 5, 4, 6, 3]
}

df = pd.DataFrame(employee_detail)

print("Employee Details")
print(df)


print("\n\nEmployee Information")
print(df.info())

print("\n\nEmployee Description")
print(df.describe())

