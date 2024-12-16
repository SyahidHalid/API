import pandas as pd

# Sample DataFrame
data = {
    'name': ['Alice', 'Bob', 'Charlie'],
    'age': [25, 30, 35],
    'city': ['New York', 'Los Angeles', 'Chicago']
}
df = pd.DataFrame(data)

#Parameters of to_json()
#orient: This parameter defines the format of the JSON output. Common options include:
#'split': Dictionary containing index, columns, and data.
#'records': List of dictionaries (one per row).
#'index': Dictionary with index as keys and rows as values.
#'columns': Dictionary with columns as keys and rows as values.
#'values': Just the values in a nested list format.

# Convert DataFrame to JSON
json_data = df.to_json(orient='records')
print(json_data)


# Split orientation
json_split = df.to_json(orient='split')
print(json_split)

# Index orientation
json_index = df.to_json(orient='index')
print(json_index)

# Columns orientation
json_columns = df.to_json(orient='columns')
print(json_columns)

# Values orientation
json_values = df.to_json(orient='values')
print(json_values)

# Save to a JSON file
df.to_json('data.json', orient='records')

