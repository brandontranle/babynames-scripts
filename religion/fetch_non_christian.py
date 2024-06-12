import os

def load_christian_names(file_path):
    """ Load Christian names from a file into a set. """
    with open(file_path, 'r') as file:
        return {line.strip() for line in file}

def get_population_counts(christian_names_set, data_file):
    """ Calculate the total population of non-Christian names for each state found in the data file. """
    state_counts = {}
    with open(data_file, 'r') as file:
        next(file)  # Skip the header
        for line in file:
            parts = line.strip().split(',')
            state, name, count = parts[0], parts[3], int(parts[4])
            if name not in christian_names_set:
                if state not in state_counts:
                    state_counts[state] = 0
                state_counts[state] += count
    return state_counts

def save_results_to_csv(results, output_file):
    """ Save the dictionary of state counts to a CSV file. """
    with open(output_file, 'w') as file:
        file.write('State,Total Non-Christian Name Count\n')
        for state, count in sorted(results.items()):
            file.write(f'{state},{count}\n')

# Path to the Christian names file
christian_names_file = 'christianNames.txt'
# Path to the data CSV file
data_csv_file = '1910_data.csv'
# Path for the output CSV file
output_csv_file = '1910_state_non_christian_name_counts.csv'

# Load Christian names
christian_names = load_christian_names(christian_names_file)

# Get population counts for all states
population_counts = get_population_counts(christian_names, data_csv_file)

# Save results to CSV
save_results_to_csv(population_counts, output_csv_file)

print(f"Data extraction complete. The CSV file has been saved as '{output_csv_file}'.")
