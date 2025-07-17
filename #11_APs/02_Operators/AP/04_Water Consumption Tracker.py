"""
Task Objective:

Collect input for daily water consumption (in liters) over 3 days.
Calculate the average daily consumption.
Output the average and show the recommended limit for comparison.

📝 Instructions:

• Ask the user to input:
  - Water consumed on Day 1.
  - Water consumed on Day 2.
  - Water consumed on Day 3.
  - The recommended daily water intake (in liters).

• Calculate:
  - The average water consumption across the three days.

• Display:
  - The average water consumed.
  - The recommended limit (no need to compare it yet).

💡 Sample Output:

Enter water consumed on Day 1 (in liters): 2.0  
Enter water consumed on Day 2 (in liters): 1.5  
Enter water consumed on Day 3 (in liters): 2.5  
Enter recommended daily water intake (in liters): 2.0  

Average Daily Consumption: 2.0 liters  
Recommended Limit: 2.0 liters
"""


#----------------------

# defining

div = "---"

# print(div * 20)

#-------------------

day_1 = float(input("Enter water consumed on Day 1 >"))
day_2 = float(input("Enter water consumed on Day 2 >"))
day_3 = float(input("Enter water consumed on Day 3 >"))

recommended_daily = float(input("Enter recommended daily water intake (in liters) >"))

print(div * 20)
#-----------------------

average_water = (day_1 + day_2 + day_3) / 3

#-----------------------

print("Avg > ", average_water)
print("Recommended daily water intake >", recommended_daily)


print(div * 20)
#-------------------