import os
import csv 

csv_path ='budget_data.csv'

#create lists to put volues to
month_count = []
profit = []
profit_change = [] 
# total_pr_loss = 0 
 

#open and read file
with open(csv_path) as csv_file:
    csv_reader = csv.reader(csv_file)
    cvs_header =next(csv_reader)
    print(f'Header :{cvs_header}')

# read after header
    for row in csv_reader:
        month_count.append(row[0])
        profit.append(int(row[1]))

#
    for i in range(len(profit)-1):
        profit_change.append(profit[i+ 1] - profit[i])

#avg profit/loss change

    total_mo = len(month_count)
    max_inc = max(profit_change)
    min_decr = min(profit_change)
    profit_change_avg = round(sum(profit_change)/len(profit_change),2)

#print 
print('Financial Analysis')
print('-------------------------------')
print('Total Month: ' + str(len(month_count)))
print('Total: ' + '$' + str(sum(profit)))
print('Average Change: ' + '$' + str(profit_change_avg))
print(f'Greatest Increase in Profits: {[profit_change.index(max(profit_change))+ 1]} ($ { max_inc})')
print(f'Greatest Decrease in Profits: {[profit_change.index(min(profit_change))+ 1]} ($ {min_decr})')

#write 
text_file = open('output.txt', 'w')
text_file.write('Financial Analysis' + '\n')
text_file.write('---------------------------------------' + '\n')
text_file.write('Total Month'  + str(len(month_count)) +'\n')
text_file.write('Total: ' + '$' + str(sum(profit)) +'\n')
text_file.write('Average change: ' + '$' + str(profit_change_avg)+'\n')
text_file.write(f'Greatest Increase in Profits: {[profit_change.index(max(profit_change))+ 1]} ($ {max_inc})\n')
text_file.write(f'Greatest Decrease in Profits: {[profit_change.index(min(profit_change))+ 1]} ($ {min_decr})\n')
text_file.close()
