import pandas as pd

# Load your dataset
df = pd.read_csv('1880-1989.csv')

def extract_name_rows(df, name, gender=None):
    # Assuming the first column contains names; adjust if necessary.
    name_column = df.columns[0]
    # Assuming the second column contains gender; adjust if necessary.
    gender_column = df.columns[1]
    # Assuming the third column contains count; adjust if necessary.
    count_column = df.columns[2]
    # Make sure we strip any leading/trailing whitespace from the name entries
    df[name_column] = df[name_column].str.strip()
    # Filter the dataframe for the rows where the name column matches the input name exactly
    result = df[df[name_column] == name]
    # If a gender is specified, further filter by gender
    if gender is not None:
        result = result[result[gender_column] == gender]
    # Calculate the sum of the count column
    total_count = result[count_column].sum()
    return total_count


# Example usage:
name_to_search = 'David'
gender_to_search = 'M'  # Can be 'M' for male, 'F' for female, or None for both
total_count = extract_name_rows(df, name_to_search, gender_to_search)
print(f"Total count for the name '{name_to_search}': {total_count}")

# Save the results to a CSV file
