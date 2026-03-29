import pandas as pd
df = pd.read_csv("new_students.csv")
print("Original DataFrame:")
print(df)
df["name"] = df["name"].str.strip()
df["department"] = df["department"].str.strip()
df["department"] = df["department"].fillna("Unknown")
df["marks"] = df["marks"].fillna(0)
df.drop_duplicates(inplace=True)
print("\nAfter Data Cleaning:")
print(df)
df["Result"] = "Pass"
df.loc[df["marks"] < 40, "Result"] = "Fail"
df.rename(columns={"marks": "Score"}, inplace=True)
print("\nAfter DataFrame Modification:")
print(df)

