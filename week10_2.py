import pandas as pd
n = int(input("Enter number of students: "))
names = []
ages = []
marks = []
for i in range(n):
print(f"\nEnter details for student {i+1}")
names.append(input("Name: "))
ages.append(int(input("Age: ")))
marks.append(int(input("Marks: ")))
df = pd.DataFrame({
"Name": names,
"Age": ages,
"Marks": marks
})
print("\nOriginal DataFrame:")
print(df)
print("\nSorted by Marks (Ascending):")
print(df.sort_values(by="Marks"))
print("\nSorted by Age (Descending):")
print(df.sort_values(by="Age", ascending=False))
print("\nSorted by Name (Alphabetical):")
print(df.sort_values(by="Name"))
print("\nFirst 4 rows:")
print(df.iloc[:4:1])
print("\nLast 3 rows:")
print(df.iloc[-3:])
print("\nRows from index 1 to 3:")
print(df.iloc[1:4])
print("\nOnly Name and Marks columns:")
print(df[["Name", "Marks"]])
