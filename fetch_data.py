import pandas as pd

def filter_data(csv_path, txt_path, gender=None, year=None):
    # Load the dataset
    data = pd.read_csv(csv_path)
    
    # Load names from the txt file
    with open(txt_path, 'r') as file:
        names = file.read().splitlines()
    
    # Filter by names
    filtered_data = data[data['Name'].isin(names)]
    
    # Filter by gender if specified
    if gender and gender != 'All':
        filtered_data = filtered_data[filtered_data['Gender'] == gender]

    # Filter by year if specified
    if year is not None:
        filtered_data = filtered_data[filtered_data['Year'] == year]

    # Creating a simplified filename based on the number of names, gender, and year
    num_names = len(names)
    gender_label = gender if gender else 'AllGenders'
    year_label = year if year else 'AllYears'
    filename = f"{num_names}_names_{year_label}_{gender_label}.csv"

    # Write the filtered data to a CSV file
    filtered_data.to_csv(filename, index=False)
    print(f"Data written to {filename}")

# Example usage:
filter_data('combined.csv', 'christianNames.txt', None, None)  # Includes all genders and all years
