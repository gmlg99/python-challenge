# Dependencies
import csv
import os

# Files to load and output (update with correct file paths)
file_to_load = os.path.join("Resources", "budget_data.csv")  # Input file path
file_to_output = os.path.join("analysis", "budget_analysis.txt")  # Output file path

# Define variables to track the financial data
total_months = 0
total_net = 0
# Add more variables to track other necessary financial data
monthly_changes = []
months = []

# Open and read the csv
with open(file_to_load) as financial_data:
    reader = csv.reader(financial_data)

    # Skip the header row
    header = next(reader)

    # Extract first row to avoid appending to net_change_list
    first_row = next(reader)
    total_months = 1
    total_net = int(first_row[1])
    previous_net = int(first_row[1])

    # Track the total and net change
    for row in reader:
        # Track the total
        total_months += 1
        current_net = int(row[1])
        total_net += current_net

        # Track the net change
        monthly_change = current_net - previous_net
        monthly_changes.append(monthly_change)
        months.append(row[0])

        # Update previous_net to current_net for the next loop
        previous_net = current_net

# Calculate the greatest increase in profits (month and amount)
greatest_increase = max(monthly_changes)
greatest_increase_month = months[monthly_changes.index(greatest_increase)]

# Calculate the greatest decrease in losses (month and amount)
greatest_decrease = min(monthly_changes)
greatest_decrease_month = months[monthly_changes.index(greatest_decrease)]

# Calculate the average net change across the months
average_change = sum(monthly_changes) / len(monthly_changes)

# Generate the output summary
output = (
    "Financial Analysis\n"
    "----------------------------\n"
    f"Total Months: {total_months}\n"
    f"Total: ${total_net}\n"
    f"Average Change: ${average_change:.2f}\n"
    f"Greatest Increase in Profits: {greatest_increase_month} (${greatest_increase})\n"
    f"Greatest Decrease in Profits: {greatest_decrease_month} (${greatest_decrease})\n"
)

# Print the output
print(output)

# Write the results to a text file
with open(file_to_output, "w") as txt_file:
    txt_file.write(output)