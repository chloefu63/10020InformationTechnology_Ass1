import csv

# Define global parallel arrays (one array per column)
ids = []
names = []
ages = []
salaries = []
cities = []
experience_years = []

# Function to read CSV data into the parallel arrays
def load_csv_to_parallel_arrays(filename):
    with open(filename, 'r') as csvfile:
        csvreader = csv.reader(csvfile)

        # Skip the header row
        next(csvreader)

        # Clear arrays to avoid duplicating data when reloading
        ids.clear()
        names.clear()
        ages.clear()
        salaries.clear()
        cities.clear()
        experience_years.clear()

        # Loop through each row and populate the parallel arrays
        for row in csvreader:
            ids.append(int(row[0]))  # ID
            names.append(row[1])  # Name
            ages.append(int(row[2]))  # Age
            salaries.append(int(row[3]))  # Salary
            cities.append(row[4])  # City
            experience_years.append(int(row[5]))  # Experience (Years)

# Function to print the data in a formatted table
def print_formatted_table(ids, names, ages, salaries, cities, experience_years):
    header = f"{'ID':<5} {'Name':<15} {'Age':>5} {'Salary':>10} {'City':<15} {'Experience (Years)':>20}"
    print(header)
    print("=" * len(header))

    for i in range(len(ids)):
        row = f"{ids[i]:<5} {names[i]:<15} {ages[i]:>5} {int(salaries[i]):>10} {cities[i]:<15} {experience_years[i]:>20}"
        print(row)

# Question 5:
# New row to be added
new_row = [11, 'Jacob', 29, 72000, 'Gold Coast', 4]

# Function to add a new row to the CSV file
def add_new_row_to_csv(filename, row):
    with open(filename, 'a', newline='') as csvfile:  # 'a' mode is for appending
        csvwriter = csv.writer(csvfile)
        csvwriter.writerow(row)
    print(f"New row added to {filename}: {row}")

# Add the new row to the existing CSV file
filename = "A1_raw_data.csv"
add_new_row_to_csv(filename, new_row)

# Reload the CSV file into the parallel arrays and print the updated table
load_csv_to_parallel_arrays(filename)
print_formatted_table(ids, names, ages, salaries, cities, experience_years)
