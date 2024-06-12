import pandas as pd

def aggregate_counts(csv_path, txt_path):
    # Load the dataset
    data = pd.read_csv(csv_path)
    
    # Load names from the txt file
    with open(txt_path, 'r') as file:
        names = file.read().splitlines()
    
    # Filter by names
    filtered_data = data[data['Name'].isin(names)]
    
    # Aggregate counts by year
    aggregated_data = filtered_data.groupby('Year')['Count'].sum().reset_index()
    
    # Write the aggregated data to a CSV file
    aggregated_data.to_csv('yearly_counts.csv', index=False)
    print("Aggregated data written to yearly_counts.csv")

# Example usage:
aggregate_counts('combined.csv', 'christianNames.txt')
