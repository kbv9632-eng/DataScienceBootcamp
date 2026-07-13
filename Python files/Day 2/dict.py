# Here we are going to learn about Dictionaries in Py
# Stored as key value pair 

employee = { "name" : "Kiran","age" : 30,"gender" : "male","salary" : 0}

print("This is a sample dictionary ")
print(employee)


# LookUp - works by accessing the key 

print(employee["age"])
print(employee["salary"])


#mini challenge
student = {
    "name": "Kiran",
    "age": 24,
    "course": "Data Science",
    "marks": 92
}

#Q1 
print(student['name'])

#Q2
print(student.get("marks"))

#Q3
student['city'] = 'Bangalore'

#Q4
student["marks"] = 95

#Q5
student.pop("course")

# Q6
print(student.keys())
print(student.values())
print(student.items())