# CSV reader and os
import csv
import os
import statistics

#Variable to count the number of months 
num_months = 0
#Variable to calculate total profits/losses
profit_loss_count = 0

#Lists to store the calculated differences and dates
difference_list = []
date_list = []

#Stored value for calculating differences
stored_val = 0

#Stored values for greatest increase and decrease 
greatest_inc = 0
greatest_dec = 0

csvpath = os.path.join("Resources", "budget_data.csv")
with open(csvpath, "r") as csv_file: 
    csv_reader = csv.reader(csv_file)

    #Skip headers 
    next(csv_reader)

    for line in csv_reader: 
        #Calculate total number of months included in the dataset
        num_months += 1
        #Changes in profit/losses over the entire period
        profit_loss_count = profit_loss_count + int(line[1])
        
        #Add change in profits to a list and dates to list
        difference_list.append((int(line[1]))-stored_val)
        stored_val = int(line[1])
        date_list.append(line[0])

    #Removes the first item from the list
    del difference_list[0]
    del date_list[0]
    #Loops though difference list to check for greatest increase and greatest decrease
    for num in difference_list:
        if num > greatest_inc:
            greatest_inc = num
        if num < greatest_dec:
            greatest_dec = num
    #Calculates average change
    avg_change = statistics.mean(difference_list)
    #Finds the dates from the greatest increase and greatest decrease from date_list using the index method
    date_inc = date_list[difference_list.index(greatest_inc)]
    date_dec = date_list[difference_list.index(greatest_dec)]

txtpath = os.path.join("Analysis", "Financial_Analysis.txt")
file = open(txtpath, "x")
file.write(f"Financial Analysis \n")
file.write(f"Total Months: {num_months}\n")
file.write(f"Total: ${profit_loss_count}\n")
file.write(f"Average Change: ${round(avg_change,2)}\n")
file.write(f"Greatest Increase in Profits: {date_inc} ({greatest_inc})\n")
file.write(f"Greatest Decrease in Profits: {date_dec} ({greatest_dec})\n")
#Outputs
print(f"Financial Analysis")
print(f"Total Months: {num_months}")
print(f"Total: ${profit_loss_count}")
print(f"Average Change: ${round(avg_change,2)}")
print(f"Greatest Increase in Profits: {date_inc} ({greatest_inc})")
print(f"Greatest Decrease in Profits: {date_dec} ({greatest_dec})")