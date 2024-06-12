import pandas as pd

def combine_csvs(filtered_csv, non_filtered_csv, output_csv):
    # Load the filtered counts
    filtered_data = pd.read_csv(filtered_csv)
    filtered_data.rename(columns={'Count': 'filtered'}, inplace=True)
    
    # Load the non-filtered counts
    non_filtered_data = pd.read_csv(non_filtered_csv)
    non_filtered_data.rename(columns={'Count': 'non_filtered'}, inplace=True)
    
    # Merge the two datasets on the 'Year' column
    merged_data = pd.merge(filtered_data, non_filtered_data, on='Year', how='outer')
    
    # Write the merged data to a new CSV file
    merged_data.to_csv(output_csv, index=False)
    print(f"Merged data written to {output_csv}")

# Example usage:
combine_csvs('yearly_counts.csv', 'yearly_excluded_counts.csv', 'combined_counts.csv')
