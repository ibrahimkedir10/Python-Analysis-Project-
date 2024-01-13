import csv

import csv

# Assuming the CSV file is in the 'data' directory and named 'city-of-seattle-2012-expenditures-dollars.csv'
csv_file_path = 'data/city-of-seattle-2012-expenditures-dollars.csv'

# Create a dictionary to store department-wise expenses
department_expenses = {}

# Read the CSV file and process the data
with open(csv_file_path, 'r') as csvfile:
    reader = csv.DictReader(csvfile)
    
    for row in reader:
        department = row['Department']
        expense_str = row['2012 Actual']

        # Skip rows with empty '2012 Actual' values
        if expense_str:
            expense = float(expense_str)

            # Update department expenses in the dictionary
            if department in department_expenses:
                department_expenses[department] += expense
            else:
                department_expenses[department] = expense

# Print the results
for department, total_expense in department_expenses.items():
    print(f"{department}: {total_expense}")
