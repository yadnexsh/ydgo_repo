"""
✅ Task Objective:

• Use the input() function to collect user data.
• Store the inputs in variables using correct naming conventions.
• Combine first and last names into a single variable.
• Print all values clearly using the print() function.
• Use the type() function to display the data type of each variable.
• Use the len() function to calculate the number of characters in the full name.
• Perform an arithmetic operation on the age value to show the age after 5 years.

🛠️ Instructions:

1. Prompt the user to enter:
   • First name
   • Last name
   • Age
   • City of residence

2. Combine the first and last name into one variable called `full_name`.

3. Print the following with clear labels:
   • Full name
   • Age
   • City

4. Use the `type()` function to print the data type of each variable.

5. Use the `len()` function to:
   • Calculate the number of characters in the full name.
   • Print the character count.

6. Convert the `age` input to a number.
   • Add 5 to it.
   • Print the result as the future age.

7. Use meaningful variable names following the `snake_case` convention.

🖥️ Sample Output:

Enter your first name: Alice  
Enter your last name: Smith  
Enter your age: 25  
Enter your city of residence: Toronto

Full Name: Alice Smith  
City: Toronto  
Age: 25

Data Types:  
full_name: <class 'str'>  
age: <class 'str'>  
city: <class 'str'>

Length of full name: 11 characters  

In 5 years, you will be 30 years old.
"""


#----------------------

# defining

div = "---"

# print(div * 20)

#-------------------

#collect

first_name = input("Enter First Name Here >")
last_name = input("Enter Last Name Here >")
age = int(input("Enter Age Here >"))
city = input("Enter City Name Here >")

print(div * 20)
#-----------------------

#combine

full_name = first_name + " " + last_name
final_age = age + 5
#-----------------------------

#prints 

print("Full Name >", full_name)
print("Age >", age)
print("City >", city)



print("Types >", type(full_name), type(age), type(city))
print("Length of full name>", len(full_name))

print(div * 20)

print("In 5 years you will be", final_age, "years old")

#-----------------------------