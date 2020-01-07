import os
import csv

#open file
bank_path = os.path.join('/Users/mignonduplessis/Documents/BootCampRep/python_challenge/PyBank/Resources/budget_data.csv')

with open(bank_path, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    #covert csv file into list
    rows=list(csvreader)

    total_months=0
    total_profit = 0
    total_changes=0
    greatest_profit_increease=0
    greatest_profit_increease_month=""
    greatest_profit_decrease=0
    greatest_profit_decrease_month=""



    #get every row in dataset
    for x in range(1,len(rows)):


        total_months += 1

        total_profit =total_profit + int(rows[x][1])

        #check if current row is max
        max_row = x != len(rows)-1
    
        if max_row:
            total_changes = total_changes + int(rows[x+1][1]) - int(rows[x][1])
           
    
          #greatest increase argument
            if(greatest_profit_increease < int(rows[x + 1][1]) - int(rows[x][1])):
                greatest_profit_increease = int(rows[x + 1][1]) - int(rows[x][1])
                greatest_profit_increease_month = rows[x + 1][0]

         #greatest decrease argument
            if (greatest_profit_decrease < int(rows[x][1]) - int(rows[x +1][1])):
                greatest_profit_decrease = int(rows[x + 1][1]) - int(rows[x][1])
                greatest_profit_decrease_month = rows[x][0]

#print results
def printResults():
    print("Financial Analysis")
    print("-------------------------")
    print("Total Months:", total_months)
    print("Total Profit:$", total_profit)
    print("Average Change: $-", round(abs(total_changes) / (len(rows) -1),2))
    print("Greatest Increase in Profits:" , greatest_profit_decrease_month + "($" + str(greatest_profit_increease) +")")
    print("Greatest Decrease in Profits:", greatest_profit_increease_month + "($-"+ str(greatest_profit_decrease)+")")

#output results to text file
def writeResults():
    output_file="Financial_Analysis.txt"

    #open output file
    file =open(output_file,"w")

    #write text file rows
    file.write("Financial Analysis\n")
    file.write("-----------------------\n")
    file.write("Total Months: " + str(total_months)+"\n")
    file.write("Total:" + str(total_profit)+ "\n")
    file.write("Average Change $-" + str(round(abs(total_changes) / (len(rows) -1),2)) + "\n")
    file.write("Greatest Increase in Profits:" + str(greatest_profit_decrease_month + "($" + str(greatest_profit_increease)+")")+ "\n")
    file.write("Greatest Decrease in Profits:" + str(greatest_profit_increease_month + "($-"+ str(greatest_profit_decrease)+")")+ "\n")

printResults()
writeResults()