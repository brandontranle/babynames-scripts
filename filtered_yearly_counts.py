import pandas as pd

def aggregate_excluded_counts(csv_path, txt_path):
    # Load the dataset
    data = pd.read_csv(csv_path)
    
    # Load names from the txt file
    with open(txt_path, 'r') as file:
        excluded_names = file.read().splitlines()
    
    # Filter out names that are in the txt file
    filtered_data = data[~data['Name'].isin(excluded_names)]
    
    # Aggregate counts by year
    aggregated_data = filtered_data.groupby('Year')['Count'].sum().reset_index()
    
    # Write the aggregated data to a CSV file
    aggregated_data.to_csv('yearly_excluded_counts.csv', index=False)
    print("Aggregated data for excluded names written to yearly_excluded_counts.csv")

# Example usage:
aggregate_excluded_counts('combined.csv', 'christianNames.txt')
