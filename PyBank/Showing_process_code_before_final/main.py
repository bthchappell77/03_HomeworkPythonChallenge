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
    


#     #read the header
#     csv_header = next(csvreader)
#     print(f'csv_header: {csv_header}')
    

#     first_pass = True
#     total_months = 0
#     total_net_dollars = 0
#     prior_amount = 0
#     amount = 0
#     delta = 0 
#     average = 0

#     for row in csvreader:
#         #left side is the variable of the equal sign and the right side is the calculations
#         total_months = total_months + 1
        
#         amount = float(row[1])
#         total_net_dollars = amount + total_net_dollars
        
#     #double equal signs is a comparison and single equal signs is an assignment
#         if first_pass == True:
#             first_pass = False

#         else: 
#             delta = prior_amount - amount
#         prior_amount = amount
#         print(delta)

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


    





    
    

