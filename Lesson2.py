students = {
    "S001":{
        "name": "Alex",
        "age": 15,
        "class": "10th",
        "marks": { 
            "Maths": 88,
            "Science": 92,
            "English": 85
        }
        
    },
    "S002": {
        "name": "Amelie",
        "age": 14,
        "class": "9th",
        "marks":{
            "Maths": 78,
            "Science": 89,
            "English": 89
        }
        
    }
}
for student_id, student_data in students.items():
    print ("\nstudent ID:",student_id)
    print("Name:",student_data["name"])
    print("Age:",student_data["class"])
    
    print("Marks:")
    for subject, score in student_data["marks"].items():
        print(" ",subject,":",score)
for student_data in students.values():
    student_data["marks"]["Maths"] += 5
print("\nUpdated Maths Marks after Bonus:")
for student_id, student_data in students.items():
    print(student_id, "=", student_data["marks"]["Maths"])