import pandas as pd

def combine_datasets(christian_file, non_christian_file, output_file):
    # Load the datasets
    christian_data = pd.read_csv(christian_file)
    non_christian_data = pd.read_csv(non_christian_file)
    
    # Combine the datasets on the 'State' column
    combined_data = pd.merge(christian_data, non_christian_data, on='State', how='outer')
    
    # Rename columns to make them clearer
    combined_data.columns = ['State', 'Christian Count', 'Non-Christian Count']
    
    # Save the combined data to a new CSV file
    combined_data.to_csv(output_file, index=False)
    print(f'Combined file saved as {output_file}')

# Example usage
combine_datasets('./1910_state_christian_name_counts.csv',
                 './1910_state_non_christian_name_counts.csv',
                 './1910_state_combined_counts.csv')
