"""
Task Objective:
Create a dictionary named shot_tracker containing nested dictionaries for individual shots.
Store shot-specific details like artist, status, and frame_range.
Modify the nested dictionary for an existing shot by updating values.
Add a new shot to the tracker with the same structure.
Print the updated dictionary.
Safely access a key that doesn’t exist using the get() method.

📝 Instructions:
• Define a dictionary named shot_tracker with three shots: shot_001, shot_002, and shot_003.
  - Each should include the keys: artist, status, and frame_range.
• Update the artist and status for shot_003.
• Add a new shot named shot_004 with the same key structure.
• Print the entire shot_tracker dictionary.
• Use the get() method to access the artist of a non-existent shot (shot_005) and return "Unassigned" if it's missing.

💡 Sample Output:

Updated shot_003: {'artist': 'Charlie', 'status': 'In Progress', 'frame_range': (301, 400)}  
Added shot_004: {'artist': 'Diana', 'status': 'Not Started', 'frame_range': (401, 500)}  

Full Shot Tracker:  
{'shot_001': {'artist': 'Alice', 'status': 'In Progress', 'frame_range': (100, 200)},  
 'shot_002': {'artist': 'Bob', 'status': 'Not Started', 'frame_range': (201, 300)},  
 'shot_003': {'artist': 'Charlie', 'status': 'In Progress', 'frame_range': (301, 400)},  
 'shot_004': {'artist': 'Diana', 'status': 'Not Started', 'frame_range': (401, 500)}}  

Artist for shot_005: Unassigned
"""



tracker ={
    "shot_1" : {"artist":"alice", "no": 30},
    "shot_2" : {"artist":"alice", "no": 30},
    "shot_3" : {"artist":"alice", "no": 30}
}



tracker["shot_3"]["no"] = 40
tracker["shot_3"]["artist"] = "sam"
# tracker["shot_4"][]


new_tracker =  tracker.update({"shot_4" : {"artist":"kiwi", "no": 30}})

print(tracker)


if "shot_5" in tracker:
    print(tracker["shot_5"]["artist"])
else :
    print("Artist for shot_005: Unassigned")
