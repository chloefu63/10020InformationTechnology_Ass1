import csv

# Field names (6 columns, with two numerical columns)
fields = ['ID', 'Name', 'Age', 'Salary', 'City', 'Experience (Years)']

# Data rows of the CSV file in the desired format
rows = [
    [1, 'James', 25, 55000, 'Sydney', 3],
    [2, 'Emily', 30, 60000, 'Newcastle', 5],
    [3, 'Liam', 22, 45000, 'Wollongong', 2],
    [4, 'Sophia', 35, 70000, 'Melbourne', 7],
    [5, 'Olivia', 28, 50000, 'Brisbane', 4],
    [6, 'Noah', 40, 80000, 'Perth', 10],
    [7, 'Isabella', 27, 62000, 'Adelaide', 6],
    [8, 'Ethan', 31, 75000, 'Canberra', 8],
    [9, 'Michael', 30, 88600, 'Hobart', 12],
    [10, 'Sarah', 18, 90000, 'Darwin', 9],
]

# Name of the CSV file
filename = "A1_raw_data.csv"

# Writing to the CSV file
with open(filename, 'w', newline='') as csvfile:
    # Creating a CSV writer object
    csvwriter = csv.writer(csvfile)


    # Writing the fields (header)
    csvwriter.writerow(fields)

    # Writing the data rows
    csvwriter.writerows(rows)

# Open the file and display the content line by line
with open(filename, mode='r') as file:
    reader = csv.reader(file)

    for row in reader:
        print(','.join(row))





