import pandas as pd

data = {
    'Name': ['Ram', 'Sam', 'John', 'Ravi'],
    'Age': [20, 21, 22, 23],
    'Marks': [85, 90, 75, 95]
}

df = pd.DataFrame(data)

print("Original DataFrame:")
print(df)

print("\nName Column:")
print(df['Name'])

df['Grade'] = ['A', 'A+', 'B', 'A+']

print("\nAfter Adding Grade Column:")
print(df)

print("\nFirst Two Rows:")
print(df.head(2))

print("\nDataFrame Information:")
print(df.describe())