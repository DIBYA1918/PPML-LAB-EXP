import pandas as pd

data = {
    'Maths': [80, 85, 90, 95, 100],
    'Science': [70, 75, 85, 90, 95],
    'English': [60, 65, 70, 75, 80]
}

df = pd.DataFrame(data)

print("DataFrame:")
print(df)

print("\nCorrelation Matrix:")
print(df.corr())