# call in modules for easy reading
import csv
import os

# save the output file path and map to location
csvpathbudget = os.path.join("python_bank_data.csv")

#open the file in this manner to only have it open while using
with open(csvpathbudget,newline="") as file_handler:
    csvreader = csv.reader(file_handler, delimiter=",")
    next(csvreader)

    #name the variables
    # use none to deal with increments! 
    # "" is empty string, [] is empty list
    # all those examples are empty
    # 0 is something - NOT NONE

    max_profit = None
    max_loss = None
    total = 0
    tot_delt = 0
    delta = 0
    avg_delt = 0
    last_profit = None
    profit = 0
    cur_month = None
    max_month = None
    min_month = None
    
    # MAKE THE LOOP - to create the list you can append in the loop but
    # that isn't how I'm doing it here. This is both how Will and Katherine helped me understand it clearer.
    for i in csvreader:
        profit = int(["Profit/Losses"])
        cur_month = ["Date"]
        #this line handles the very first row being ignored I think.
        if last_profit !=None:
            delta = profit - last_profit
        # the next line uses the following tools 
        # != (not equal) | : means (then)
        if last_profit != None:
           tot_delt = tot_delt + delta
           last_profit = profit
        if last_profit == None:
           total = total + profit
        if max_profit == None or max_profit < delta:
           max_profit = delta
           max_month = cur_month
        if max_loss == None or max_loss > delta:
           max_loss = delta
           min_month = cur_month
        last_profit = profit

#Count the rows
    file_handler.seek()
    row_count = sum(1 for i in csvreader)
    row_count = row_count - 1

    avg_delt = tot_delt / (row_count-1)

    #Display
    print("Financial Analysis")
    print("------------------------------")
    print(f"Total Months: {row_count}")
    print(f"Total: ${total}")
    print(f"Average Change: {f(avg_delt)}")
    print(f"Greatest Increase in Profits: {max_month}\({max_profit})")
    print(f"Greatest Decrease in Profits: {min_month}\({max_profit})")






    # print(row_count)
    # print(max_profit)
    # print(max_loss)
    # print(total)
    # print(max_month)
    # print(min_month)
   

#     print("Financial Analysis")
#     print("------------------")
#     print(f"Total Months: {total_months}")
#     print(f"Total: ${total_net_dollars}")
#     print(f"Average Change: {delta}")


#         #declare variable to hold the cell value I was to use to calculate, located in the second column here referred to as 1.
        
        

# #print(data)





    
    
        
                  
            
            

        
#     #the average of the changes in P&L over the entire period
#     #the greatest increase in profits (date and amount) over the entire period
#     #the greatest decrease in losses (date and amount) over the entire period


    





    
    

