import csv


# Reference: https://docs.python.org/3/library/csv.html
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
def print_formatted_table():
    if not ids:
        print("No data available. Please load the CSV file first.")
        return

    header = f"{'ID':<5} {'Name':<15} {'Age':>5} {'Salary':>10} {'City':<15} {'Experience (Years)':>20}"
    print(header)
    print("=" * len(header))

    for i in range(len(ids)):
        row = f"{ids[i]:<5} {names[i]:<15} {ages[i]:>5} {int(salaries[i]):>10} {cities[i]:<15} {experience_years[i]:>20}"
        print(row)


# Function to add a new row (only to memory, not CSV)
def add_new_record():
    # Get new record details from user with validation for age and salary
    new_name = input("Enter name: ")

    # Validate age input
    while True:
        try:
            new_age = int(input("Enter age (must be a number): "))
            break
        except ValueError:
            print("Invalid input. Please enter a valid number for age.")

    # Validate salary input
    while True:
        try:
            new_salary = int(input("Enter salary (must be a number): "))
            break
        except ValueError:
            print("Invalid input. Please enter a valid number for salary.")

    new_city = input("Enter city: ")

    # Validate experience years input
    while True:
        try:
            new_experience_years = int(input("Enter experience (years) (must be a number): "))
            break
        except ValueError:
            print("Invalid input. Please enter a valid number for experience (years).")

    # Generate the next ID automatically
    new_id = get_next_id()
    new_row = [new_id, new_name, new_age, new_salary, new_city, new_experience_years]

    # Add the new row to the parallel arrays, but NOT to the CSV
    ids.append(new_id)
    names.append(new_name)
    ages.append(new_age)
    salaries.append(new_salary)
    cities.append(new_city)
    experience_years.append(new_experience_years)

    print(f"New row added to memory: {new_row}")


# Automatically generate the next ID based on the current max ID in the CSV
def get_next_id():
    if ids:
        return max(ids) + 1  # Get the next available ID
    else:
        return 1  # If no IDs are present, start with 1


# Function to delete a row by ID
def delete_record_by_id(delete_id):
    if delete_id in ids:
        index = ids.index(delete_id)
        ids.pop(index)
        names.pop(index)
        ages.pop(index)
        salaries.pop(index)
        cities.pop(index)
        experience_years.pop(index)
        print(f"Record with ID {delete_id} has been deleted.")
    else:
        print(f"No record found with ID {delete_id}.")


# Function to save the updated data back to the CSV after deletion or addition
def save_data_to_csv(filename):
    with open(filename, 'w', newline='') as csvfile:
        csvwriter = csv.writer(csvfile)
        # Write header
        csvwriter.writerow(['ID', 'Name', 'Age', 'Salary', 'City', 'Experience (Years)'])
        # Write rows
        for i in range(len(ids)):
            csvwriter.writerow([ids[i], names[i], ages[i], salaries[i], cities[i], experience_years[i]])


# Menu-driven system with validation for numeric inputs
def menu(filename):
    while True:
        print("\nMenu:")
        print("1. Load CSV Data")
        print("2. Display Records")
        print("3. Add a New Record")
        print("4. Delete a Record by ID")
        print("5. Save Records")
        print("6. Exit")

        choice = input("Enter your choice (1-6): ")

        if choice == '1':
            load_csv_to_parallel_arrays(filename)
            print("CSV data loaded successfully.")

        elif choice == '2':
            print_formatted_table()

        elif choice == '3':
            add_new_record()

        elif choice == '4':
            try:
                delete_id = int(input("Enter the ID of the record to delete: "))
                delete_record_by_id(delete_id)
            except ValueError:
                print("Invalid input. Please enter a valid number for ID.")

        elif choice == '5':
            save_data_to_csv(filename)
            print("Data saved to CSV.")

        elif choice == '6':
            print("Exiting the program.")
            break

        else:
            print("Invalid choice. Please try again.")


# Main program
filename = "A1_raw_data.csv"
menu(filename)
