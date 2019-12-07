# Rutgers DSBC - HW3 - Python - Jacob Menchak - PyBank:

import os
import csv
import logging

# Import the CSV file:

# My CSV Path:
os.chdir(os.path.dirname(os.path.abspath(__file__)))
budget_data_csv = os.path.join('..', 'Resources', 'budget_data.csv')

# Temporarily hard-coding the CSV file path when error present:
#budget_data_csv = 'C:/Users/jmenc/Documents/DSBC_Rutgers/03-Homework/Python/Instructions/PyBank/Resources/budget_data.csv'


# Variables:
date_count = 0
float_profit_loss_net_total = 0
profits_and_losses = []
profit_loss_net_total = 0
string_date_list = 0
date_list = []
average_profit_loss = 0
average_change = []
successive_difference_list = []
successive_difference_list_total = 0
successive_difference_list_length = 0
successive_difference_list_average = 0
greatest_profit_loss_increase = 0
greatest_profit_loss_decrease = 0
greatest_profit_loss_increase_index = 0
greatest_profit_loss_decrease_index = 0


# Open and read the "budget_data.csv" CSV file, loop through each row in the file:
with open(budget_data_csv, newline="") as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=",")

    # Read the header row first:
    csv_header = next(csvfile)
    #print(f"Header: {csv_header}")

    # Read through each row of data after the header.
    # Find "the total number of months included in the dataset":
    for row in csv_reader:
        date_count += 1
        #print(row)     

        # Find "the net total amount of "Profit/Losses" over the entire period":
        float_profit_loss_net_total = float(row[1])
        # Add each "Profit or Loss" value from "column B" to the end of the "profits_and_losses" list:
        profits_and_losses.append(float_profit_loss_net_total)
        # Add each "Profit or Loss" value from "column B" to the current total, "profit_loss_net_total":
        profit_loss_net_total += float_profit_loss_net_total

        # Create a list of "Date" values:
        string_date_list = str(row[0])
        # Add each "Date" value from "column A" to the end of the "date_list" list:
        date_list.append(string_date_list)

    #print(profits_and_losses)
    #print(date_list)


# Find "the average of the changes in "Profit/Losses" over the entire period":
#average_profit_loss = profit_loss_net_total / date_count
#rounded_average_profit_loss = round(average_profit_loss, 2)

# Using list comprehension to generate a "successive_difference_list":
successive_difference_list = [profits_and_losses[j + 1] - profits_and_losses[j] for j in range(len(profits_and_losses)-1)] 
#print ("The calculated successive_difference_list is: " + str(successive_difference_list))

successive_difference_list_total = sum(successive_difference_list)
#print(successive_difference_list_total)
successive_difference_list_length = len(successive_difference_list)
#print(successive_difference_list_length)
successive_difference_list_average = successive_difference_list_total / successive_difference_list_length
#print(successive_difference_list_average)
rounded_successive_difference_list_average = round(successive_difference_list_average, 2)
#print(rounded_successive_difference_list_average)


# Find "the greatest increase in profits (date and amount) over the entire period":
greatest_profit_loss_increase = max(profits_and_losses)
#print(greatest_profit_loss_increase)


# Find "the greatest decrease in losses (date and amount) over the entire period":
greatest_profit_loss_decrease = min(profits_and_losses)
#print(greatest_profit_loss_decrease)


# This function, "get_indexes_max_value", returns the index position of the maximum values in the "profits_and_losses" list.
# This function then uses these index positions to find the corresponding date values from the "date_list" list.

# Locate the index position(s) of the maximum value(s) in the "profits_and_losses" list:
def get_indexes_max_value(profits_and_losses):
    max_value = max(profits_and_losses)
    if profits_and_losses.count(max_value) > 1:
        return [i for i, x in enumerate(profits_and_losses) if x == max(profits_and_losses)]
    else:
        return profits_and_losses.index(max(profits_and_losses))

greatest_profit_loss_increase_index = get_indexes_max_value(profits_and_losses)
#print(get_indexes_max_value(profits_and_losses))
#print(greatest_profit_loss_increase_index)
#print(date_list[greatest_profit_loss_increase_index])


# This function, "get_indexes_min_value", returns the index position of the minimum values in the "profits_and_losses" list.
# This function then uses these index positions to find the corresponding date values from the "date_list" list.

# Locate the index position(s) of the minimum value(s) in the "profits_and_losses" list:
def get_indexes_min_value(profits_and_losses):
    min_value = min(profits_and_losses)
    if profits_and_losses.count(min_value) > 1:
        return [i for i, x in enumerate(profits_and_losses) if x == min(profits_and_losses)]
    else:
        return profits_and_losses.index(min(profits_and_losses))

greatest_profit_loss_decrease_index = get_indexes_min_value(profits_and_losses)
#print(get_indexes_min_value(profits_and_losses))
#print(greatest_profit_loss_decrease_index)
#print(date_list[greatest_profit_loss_decrease_index])


# Logging:
logging.basicConfig(level=logging.INFO, format='%(message)s')
logger = logging.getLogger()
# ***PLEASE_TAKE_NOTE***: The OUTPUT is being exported to a text file (log file) located at: C:\Users\CURRENT_USER
logger.addHandler(logging.FileHandler('./JMM_RutgersDSBC_HW3_Python_PyBank_LogFileOutput.log', 'a'))
print = logger.info
print('If you can see this message, JMMs HW3 PyBank Logger is exporting the HW3_PyBank.py OUTPUT to this text file correctly :-)')
print('please note that this OUTPUT is being exported to a text file (log file) located at C_Users_CurrentUser')


# Print Statements / Output:
print("'''text \nFinancial Analysis \n----------------------------")
print(f"Total Months: " + str(date_count))
print(f"Total: $" + str(round(profit_loss_net_total)))
print(f"Average Change: $" + str(rounded_successive_difference_list_average))
print(f"Greatest Increase in Profits: " + str(date_list[greatest_profit_loss_increase_index]) + " ($" + str(round(greatest_profit_loss_increase)) + ")")
print(f"Greatest Decrease in Profits: " + str(date_list[greatest_profit_loss_decrease_index]) + " ($" + str(round(greatest_profit_loss_decrease)) + ")")
print("'''")


# Example Output:
#```text
#  Financial Analysis
#  ----------------------------
#  Total Months: 86
#  Total: $38382578
#  Average  Change: $-2315.12
#  Greatest Increase in Profits: Feb-2012 ($1926159)
#  Greatest Decrease in Profits: Sep-2013 ($-2196167)
#  ```