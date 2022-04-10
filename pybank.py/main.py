import os
import csv

#set path for csv file and text file analysis result 
csvpath = os.path.join('C:\\Users\\Danny Dao\\Desktop\\UCI program\\HOMEWORK\\Python\\pybank.py\\Resources\\budget_data.csv')

with open(csvpath, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

    
#skips header
    csv_header = next(csvreader)
    
    
#assigning variables
    month = []
    revenue = []
    revenue_change = []
    monthly_change = []
                  

#Months       
    for row in csvreader:
        month.append(row[0])
        revenue.append(row[1])
    #print(len(month))
    
 #Revenue 
    revenue_int = map(int,revenue)
    total_revenue = (sum(revenue_int))
    #print(total_revenue)

 #Average Change
    i = 0
    for i in range(len(revenue) - 1):
        profit_loss = int(revenue[i+1]) - int(revenue[i])
        
 # append profit_loss
        revenue_change.append(profit_loss)
    Total = sum(revenue_change)
    #print(revenue_change)
    monthly_change = Total / len(revenue_change)
    #print(monthly_change)
    #print(Total)
    
#Greatest Increase
    profit_increase = max(revenue_change)
    #print(profit_increase)
    k = revenue_change.index(profit_increase)
    month_increase = month[k+1]
    
#Greatest Decrease
    profit_decrease = min(revenue_change)
    #print(profit_decrease)
    j = revenue_change.index(profit_decrease)
    month_decrease = month[j+1]


#Print Statements

print(f'Financial Analysis'+'\n')
print(f'----------------------------'+'\n')


print("Total number of months: " + str(len(month)))

print("Total Revenue in period: $ " + str(total_revenue))
      
print("Average monthly change in Revenue : $" + str(monthly_change))

print(f"Greatest Increase in Profits: {month_increase} (${profit_increase})")

print(f"Greatest Decrease in Profits: {month_decrease} (${profit_decrease})")

#Output text file

f = open('Financial Analysis.txt','w')
f.write('Financial Analysis')
f.write('------------------------------'+'\n')
        
f.write("Total number of months: " + str(len(month)
                                        ))
        
f.write("Total Revenue in period: $ " + str(total_revenue))
        
f.write('Average monthly change in Revenue : $' + str(round(monthly_change, 2)))

f.write('Greatest Increase in Profits:' + str(month_increase) + ' ($' + str(profit_increase)+ ')')

f.write('Greatest Decrease in Profits:' + str(month_decrease) + ' ($' + str(profit_decrease)+ ')')
        
        