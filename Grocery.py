"""
✅ Task Objective:

• Accept user input for the quantity and unit price of two grocery items.
• Calculate the total cost for each item and the grand total.
• Output a summary including the cost of each item and the grand total.

📝 Instructions:

1. Prompt the user to enter:
   • Quantity and unit price for Item 1
   • Quantity and unit price for Item 2
   • Their total spending limit

2. Perform the following calculations:
   • Item 1 Total = quantity × unit price
   • Item 2 Total = quantity × unit price
   • Grand Total = Item 1 Total + Item 2 Total

3. Display the following:
   • Total cost of Item 1
   • Total cost of Item 2
   • Grand Total
   • Spending Limit (no need to compare it yet)

💡 Sample Output:

Enter quantity for Item 1: 3  
Enter unit price for Item 1: 2.5  
Enter quantity for Item 2: 2  
Enter unit price for Item 2: 5.0  
Enter your spending limit: 20  

Item 1 Total: 7.5  
Item 2 Total: 10.0  
Grand Total: 17.5  
Spending Limit: 20.0
"""

#----------------------

# defining

div = "---"

# print(div * 20)

#-------------------

item_1 = int(input("Enter Item 1 >"))
price_1 = float(input("Enter Price of Item 1 >"))

item_2 = int(input("Enter Item 2 >"))
price_2 = float(input("Enter Price of Item 2 >"))

limit = float(input("Enter Spending Limit >"))

print(div * 20)
#------------------

total_1 = item_1 * price_1

total_2 = item_2 * price_2

grand_total = total_1 + total_2

# ------------------------

print("Total Cost of Item 1>", total_1)
print("Total Cost of Item 2>", total_2)

print("Grand Total >", grand_total)
print("Spending Limit>", limit)

print(div * 20)
#------------------