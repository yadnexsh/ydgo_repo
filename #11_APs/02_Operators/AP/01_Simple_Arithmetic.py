"""
# Description of the Task
Create a Python program that prompts the user to input two numbers and then computes and displays the sum, difference, product, and quotient of these numbers.

# Instructions
Prompt the user to input the first number.
Prompt the user to input the second number.
Calculate the sum of the two numbers.
Calculate the difference between the two numbers.
Calculate the product of the two numbers.
Calculate the quotient of the two numbers.
Display the results of each calculation.

# Learning Objective
To understand and use basic arithmetic operations in Python.
To practice taking user input and converting it to appropriate data types.
To learn basic output formatting in Python.
"""
#----------------------

# defining

div = "---"

# print(div * 20)

#-------------------

first_number = int(input("First Number >"))
second_number = int(input("Second Number >"))

print(div * 20)
#------------------

sum = first_number + second_number
diff = first_number - second_number
multi = first_number * second_number
quote = first_number // second_number

#--------------------

print("Sum >",sum)
print("Difference >", diff)
print("Product >", multi)
print("Quotient >", quote)

#--------------------



