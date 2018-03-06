months = []
monthly_revenue = {}
monthly_difference = {}

import os
csvpath = os.path.join('resources', 'budget_data_2.csv')

import csv
with open(csvpath, newline='') as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    print(csvreader)

    #  Each row is read as a row
    for row in csvreader:
        monthly_revenue[row[0]] = row[1]
        months.append(row[0])
        
del monthly_revenue["Date"]
del months[0]

total_revenue = 0

for month in months:
    total_revenue = total_revenue + int(monthly_revenue[month])

i = 0

while i < len(months) - 1:
    monthly_difference[months[i + 1]] = int(monthly_revenue[months[i + 1]]) - int(monthly_revenue[months[i]])
    i = i + 1
    
total_revenue_change = 0

for month in months:
    if month in monthly_difference:
        total_revenue_change = total_revenue_change + int(monthly_difference[month])

average_revenue_change = int(total_revenue_change / len(monthly_difference))
        
import operator    
max_key = max(monthly_difference.items(), key=operator.itemgetter(1))[0]

min_key = min(monthly_difference.items(), key=operator.itemgetter(1))[0]
print(min_key + ": " + str(monthly_difference[min_key]))

print("Financial Analysis")
print("-------------------")
print("Total Months: " + str(len(months)))
print("Total Revenue: $" + str(total_revenue))
print("Average Revenue Change: $" + str(average_revenue_change))
print("Greatest Increase in Revenue: " + max_key + " ($" + str(monthly_difference[max_key]) + ")")
print("Greatest Decrease in Revenue: " + min_key + " ($" + str(monthly_difference[min_key]) + ")")

f = open('output/PyBank2.txt','w')
f.write("Financial Analysis\n")
f.write("-------------------\n")
f.write("Total Months: " + str(len(months)) + "\n")
f.write("Total Revenue: $" + str(total_revenue) + "\n")
f.write("Average Revenue Change: $" + str(average_revenue_change) + "\n")
f.write("Greatest Increase in Revenue: " + max_key + " ($" + str(monthly_difference[max_key]) + ")\n")
f.write("Greatest Decrease in Revenue: " + min_key + " ($" + str(monthly_difference[min_key]) + ")\n")
f.close()