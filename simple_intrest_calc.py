"""# Description of the Task:
Write a Python program that calculates the simple interest for a given principal amount, rate of interest, and time period.

# Instructions:
Take input from the user for the principal amount, rate of interest (in percentage), and time period (in years).
Calculate the simple interest using the formula: 
Simple Interest=(Principal×Rate×Time)/100
Print the calculated simple interest

# Learning Objective:
Practice taking user input.
Apply mathematical calculations using Python.
Print the result to the console."""


#----------------------

# defining

div = "---"

# print(div * 20)

#-------------------

#inputs

principal = int(input("Principal Ammount >"))
interest  = float(input("Rate of Interest  >"))
period = float(input("Timer Period >"))

print(div * 20)
#------------------------

simple_interest=(principal * interest  * period) / 100
print("Simple Interest >", simple_interest)

print(div * 20)
#------------------------