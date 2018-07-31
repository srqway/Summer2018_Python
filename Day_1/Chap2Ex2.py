#Paul Burkholder
#08/28/2017
#Program Chapter2 Exercise2
#Pseudocode

"""Get input for total sales
calculate projected profit by multiplying total sales by 23% (.23)
display projected profit"""

#If total sales greater than 100,000 then Sales Percentage will be 25%
#Else sales perecentage is 23%

#Variable Declarations
TOTAL_SALES_PERCENTAGE_23_PERCENT = .23 # Represents 23% applied to total sales
TOTAL_SALES_PERCENTAGE_25_PERCENT = .25

#TOTAL_SALES_PERCENTAGE = 0.0
TOTAL_SALES = 0.0 # Represents total gross sales
TOTAL_PROFIT = 0.0 # Represent total profit (my take home)

#Prompting user for total sales
TOTAL_SALES = float(input("Enter projected sales: "))

#Making decision on total sales
if TOTAL_SALES > 100000:
     TOTAL_PROFIT = TOTAL_SALES * TOTAL_SALES_PERCENTAGE_25_PERCENT
     print("Total sales is greater than 100,000")


#Calculate total profit based on sales recorded
#TOTAL_PROFIT = TOTAL_SALES * TOTAL_SALES_PERCENTAGE

#Display total profit
print ("Your total profit is: $", format(TOTAL_PROFIT, ',.2f'))
