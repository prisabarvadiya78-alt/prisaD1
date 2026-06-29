import pandas as pd

stud_details = {
    "Roll no": [101, 102, 103, 104, 105],
    "Name": ["Nirali", "Priya", "Kangana", "Kruti", "Nensi"],
    "Marks": [85, 92, 78, 88, 82],
    "City": ["Rajkot", "Jetpur", "Virpur", "Gondal", "Jamnagar"]
}

df = pd.DataFrame(stud_details)

print(df)