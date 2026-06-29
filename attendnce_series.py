import pandas as pd
stu_attendance=pd.Series([82,76,90,74,85,70,95,92,80])
print(stu_attendance)
print("student with attendance less than 75:")
print(stu_attendance[stu_attendance<75])
print("maximum marks",stu_attendance.max())
print("minimum marks",stu_attendance.min())
print("average marks",stu_attendance.mean())