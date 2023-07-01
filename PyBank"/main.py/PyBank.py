# Import modules os and csv

import os
import csv

# Set the path for the CSV file 
budget_csv = os.path.join("Resources","budget_data.csv")

# Open the CSV using the set path PyBankcsv
with open(budget_csv, 'r') as csvfile:
    
    csvreader = csv.reader(csvfile, delimiter=",")

    csv_header = next(csvreader)

    header = next(csvreader)

    # Set veriables to store data.
    total_months = 0
    total_profit_loss = 0
    total_change_profit_loss = 0
    initial_profit = 0

    # Create list to store data
    final_profit = []
    monthly_changes = []
    date = []

    # variables to store column index for profit or loss
    plcol = header.index("Profit/loss")

    # variables to store column index for date
    datecol = header.index("Date")

# Looping through the rows 
for row in csvreader:    
      
      # Use counter veriable to count the total months 
      total_months +=1

      # adding total profit or loss
      total_profit_loss += int(row[plcol])

      # appending dates
      date.append(row[datecol])

      # appending profit
      final_profit.append(row[plcol])

      # calculate the average change in profits from month to month. Then calulate the average change in profits
      final_profit = int(row[plcol])
      monthly_change_profits = final_profit - initial_profit

      # store monthly changes in a list
      monthly_changes.append(monthly_change_profits)

      total_change_profits = total_change_profits + monthly_change_profits
      initial_profit = final_profit

      # calculate the average change in profits
      average_change_profits = (total_change_profits/total_months)
      
      # Find out the max and min change in profits 
      greatest_increase_profits = max(monthly_changes)
      greatest_decrease_profits = min(monthly_changes)

      increase_date = date[monthly_changes.index(greatest_increase_profits)]
      decrease_date = date[monthly_changes.index(greatest_decrease_profits)]
      
     # print output
      print("Financial Analysis")
      print("")
      print("---------------------------")
      print("")
      print("Total Months:" + str(total_months))
      print("")
      print("Total Profits: " + "$" + str(total_profit_loss))
      print("")
      print("Average Change: " + "$" + str(int(average_change_profits)))
      print("")
      print("Greatest Increase in Profits: " + str(increase_date) + " ($" + str(greatest_increase_profits) + ")")
      print("")
      print("Greatest Decrease in Profits: " + str(decrease_date) + " ($" + str(greatest_decrease_profits)+ ")")
      print("----------------------------------------------------------")
     
     # creating a .txt file to store output
     
with open('financial_analysis.txt', 'w') as text:
    text.write("----------------------------------------------------------\n")
    text.write("  Financial Analysis"+ "\n")
    text.write("----------------------------------------------------------\n\n")
    text.write("    Total Months: " + str(total_months) + "\n")
    text.write("    Total Profits: " + "$" + str(total_profit_loss) +"\n")
    text.write("    Average Change: " + '$' + str(int(average_change_profits)) + "\n")
    text.write("    Greatest Increase in Profits: " + str(increase_date) + " ($" + str(greatest_increase_profits) + ")\n")
    text.write("    Greatest Decrease in Profits: " + str(decrease_date) + " ($" + str(greatest_decrease_profits) + ")\n")
    text.write("----------------------------------------------------------\n")

# closing the .txt file

