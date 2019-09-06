import os
import csv
csvpath = os.path.join('Resources', 'budget_data.csv')
output_file = os.path.join('Analysis', 'budget_analysis.txt')

total_months = 0
total_profit = 0
change = []
change_month = []
profit_increase = ["", 0]
profit_decrease = ["", 100000000000000000000]

with open(csvpath, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    header = next(csvreader)
    first_row = next(csvreader)

    previous = int(first_row[1])
    total_months = total_months + 1
    total_profit = total_profit + int(first_row[1])
    
    for row in csvreader:
        total_months = total_months + 1
        total_profit = total_profit + int(row[1])
        
        net_change = int(row[1]) - previous
        previous = int(row[1])
        change = change + [net_change]
        change_month = change_month + [row[0]]
        
        if net_change > profit_increase[1]:
            profit_increase[1] = net_change
            profit_increase[0] = row[0]
            
        if net_change < profit_decrease[1]:
            profit_decrease[1] = net_change
            profit_decrease[0] = row[0]
            
        average_change = sum(change) / len(change)
        
        
output = (
    f"\nFinancial Analysis\n"
    f"----------------------------\n"
    f"Total Months: {total_months}\n"
    f"Total: ${total_profit}\n"
    f"Average  Change: ${average_change:.2f}\n"
    f"Greatest Increase in Profits: {profit_increase[0]} (${profit_increase[1]})\n"
    f"Greatest Decrease in Profits: {profit_decrease[0]} (${profit_decrease[1]})\n"
)

print(output)