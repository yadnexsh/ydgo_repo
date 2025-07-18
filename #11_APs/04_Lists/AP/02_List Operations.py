"""
# Description of the Task
In this task, you'll write a Python program that performs various operations on a list of numbers. You'll create a list, perform different operations like finding the largest and smallest numbers, calculating the sum of all numbers, and printing the list in reverse order.

# Instructions
Create a list of numbers (you can start with a predefined list or ask the user to input the numbers).
Print the list to the console.
Find and print the largest number in the list.
Find and print the smallest number in the list.
Calculate and print the sum of all numbers in the list.
Print the list in reverse order.

# Learning Objective
The objective of this task is to help beginners understand and practice the following Python concepts:
List creation and manipulation
Basic list operations (finding min, max, sum)
Looping through lists
Using built-in functions like max(), min(), and sum()
Reversing a list
"""



a = [ 1, 2, 3, 4, 5, 6, 7]

print(a)

max = max(a)
min = min(a)
sum = sum(a)

reverse = a[::-1]

print(max, min, sum)

print(reverse)


# max min sum is not given in pdf , but how do we understand the synatx for it such as why its not a.max() and why max.(a) > is it cause its fun ? then what others are?