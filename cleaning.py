
import pandas as pd

# =====================================
# STEP 1: IMPORT DATASET
# =====================================

df = pd.read_csv("data.csv")

print("\nORIGINAL DATASET")
print(df)

# =====================================
# STEP 2: INSPECT DATASET
# =====================================

print("\nDATASET INFORMATION")
print(df.info())

print("\nFIRST FIVE ROWS")
print(df.head())

print("\nDATASET SHAPE")
print(df.shape)

print("\nCOLUMN NAMES")
print(df.columns)

print("\nSTATISTICAL SUMMARY")
print(df.describe(include="all"))

# =====================================
# STEP 3: IDENTIFY MISSING VALUES
# =====================================

print("\nMISSING VALUES")
print(df.isnull().sum())

# Treat whitespace-only cells as missing
df = df.replace(r"^\s*$", pd.NA, regex=True)

print("\nMISSING VALUES AFTER CHECKING BLANKS")
print(df.isnull().sum())

# =====================================
# STEP 4: IDENTIFY DUPLICATES
# =====================================

print("\nDUPLICATE RECORDS")
print(df.duplicated().sum())

# Remove duplicate rows
df = df.drop_duplicates()

print("\nDATA AFTER REMOVING DUPLICATES")
print(df)

# =====================================
# STEP 5: HANDLE MISSING VALUES
# =====================================

# Convert Age and Marks into numeric values
# Invalid values such as 'twenty' become NaN

df["Age"] = pd.to_numeric(df["Age"], errors="coerce")
df["Marks"] = pd.to_numeric(df["Marks"], errors="coerce")

# Fill missing Age with median
df["Age"] = df["Age"].fillna(df["Age"].median())

# Fill missing Marks with median
df["Marks"] = df["Marks"].fillna(df["Marks"].median())

# Fill missing City with Unknown
df["City"] = df["City"].fillna("Unknown")

# Fill missing Gender with Unknown
df["Gender"] = df["Gender"].fillna("Unknown")

# =====================================
# STEP 6: CORRECT DATA TYPES
# =====================================

df["Student_ID"] = df["Student_ID"].astype(int)
df["Age"] = df["Age"].round().astype(int)
df["Marks"] = df["Marks"].round(2)

# =====================================
# STEP 7: STANDARDIZE TEXT VALUES
# =====================================

df["Name"] = df["Name"].str.strip().str.title()
df["Gender"] = df["Gender"].str.strip().str.title()
df["City"] = df["City"].str.strip().str.title()

# =====================================
# STEP 8: FINAL DATA INSPECTION
# =====================================

print("\nCLEANED DATASET")
print(df)

print("\nFINAL MISSING VALUES")
print(df.isnull().sum())

print("\nFINAL DUPLICATE COUNT")
print(df.duplicated().sum())

print("\nFINAL DATA TYPES")
print(df.dtypes)

# =====================================
# STEP 9: SAVE CLEANED DATASET
# =====================================

df.to_csv("cleaned_data.csv", index=False)

print("\nDataset cleaned successfully!")
print("Cleaned file saved as cleaned_data.csv")