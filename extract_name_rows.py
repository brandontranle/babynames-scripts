import pandas as pd

# Load your dataset
df = pd.read_csv('1880-1989.csv')

def extract_name_rows(df, name, gender=None):
    # Assuming the first column contains names; adjust if necessary.
    name_column = df.columns[0]
    # Assuming the second column contains gender; adjust if necessary.
    gender_column = df.columns[1]
    # Make sure we strip any leading/trailing whitespace from the name entries
    df[name_column] = df[name_column].str.strip()
    # Filter the dataframe for the rows where the name column matches the input name exactly
    result = df[df[name_column] == name]
    # If a gender is specified, further filter by gender
    if gender is not None:
        result = result[result[gender_column] == gender]
    return result

def save_to_csv(data, filename):
    # Save the filtered DataFrame to a CSV file
    data.to_csv(filename, index=False)
    print(f"Data saved to {filename}")

# Example usage:
name_to_search = 'Lyndon'
gender_to_search = 'M'  # Can be 'M' for male, 'F' for female, or None for both
extracted_rows = extract_name_rows(df, name_to_search, gender_to_search)

# Save the results to a CSV file
save_to_csv(extracted_rows, name_to_search + '_' + gender_to_search + '.csv')
