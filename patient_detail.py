import pandas as pd

patient_details = {
    "Patient_ID": [101, 102, 103, 104, 105],
    "Name": ["Raj", "Priya", "aksha", "Sneha", "Karan"],
    "Age": [25, 32, 45, 28, 50],
    "Gender": ["Male", "Female", "Female", "Female", "Male"],
    "Disease": ["Fever", "Diabetes", "Asthma", "Typhoid", "Hypertension"],
    "Doctor": ["Dr. Sharma", "Dr. Patel", "Dr. Mehta", "Dr. Shah", "Dr. Joshi"]
}

df = pd.DataFrame(patient_details)

print("Patient Details:")
print(df)