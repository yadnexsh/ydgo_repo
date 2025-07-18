"""
✅ Task Objective:
Accept input for a student’s name, subject, and score.
Remove extra spaces using the strip() method.
Format the student name in lowercase and capitalize the subject.
Use the .format() method to generate a formatted report sentence.
Use an f-string to summarize the performance.
Add a divider line using repetition (*) and show it above and below the report.

🛠 Instructions:
• Ask the user to enter the student’s name, subject, and score.
• Clean each input string using strip().
• Convert the name to lowercase and the subject to title case (capitalize the first letter of each word).
• Use * 40 to create a decorative line.
• Construct a sentence like "Student John has scored 87 in Mathematics." using .format().
• Create a summary sentence using f-string, like "john’s performance in Mathematics is satisfactory."
• Display both sentences surrounded by divider lines.

📤 Sample Output:

Enter student name:  JOHN  
Enter subject:   mathematics  
Enter score: 87

****************************************
Student John has scored 87 in Mathematics.
john’s performance in Mathematics is satisfactory.
****************************************
"""
#----------------------

# defining

div = "---"

# print(div * 20)
#-------------------


in_name = input("Name >")
in_subject = input("Subject >")
in_score = (input("Score >"))

print(div * 40 )

name = in_name.strip().lower()
subject = in_subject.strip().title()
score = in_score.strip()

print("Student {} has scored {} in {}.".format(name, score, subject))

print(f"{name}'s performance in {subject} is satisfactory.")

print(div * 40 )

#-------------------
