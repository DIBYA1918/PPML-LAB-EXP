import pandas as pd

df = pd.DataFrame({
    'Name': ['Ram', 'Sam', 'John'],
    'Age': [20, 21, 22],
    'Marks': [85, 90, 95]
})

df.to_csv('data.csv', index=False)
df.to_json('data.json', orient='records')

csv_data = pd.read_csv('data.csv')
json_data = pd.read_json('data.json')

print("CSV File Data:")
print(csv_data)

print("\nJSON File Data:")
print(json_data)