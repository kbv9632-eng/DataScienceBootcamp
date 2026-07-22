#Imports 
from data.database import students
# It is responsible for all student management operations.

#Add Student
def add_student():
    student_id = input("Enter Student ID: ")
    name = input("Enter name of the student :- ")
    age = int(input('Enter the age of the student:- '))
    gender = input("Enter the Gender of the Student:- ")
    student_class = input('Enter Student Class:- ')

    student = {
    "student_id" : student_id,
    "name" : name,
    "age" : age,
    "gender" : gender,
    "student_class" : student_class
    }
    students.append(student)
    print("Student has been added")
    print(students)
#Update Student Info 
def update_student():
    user_input_update = input("Enter the Student ID: ")
    found = False

    for student in students:
        if user_input_update == student["student_id"]:
            found = True
            while True:
                user_input_key = input(
                    "Enter the field you would like to update: "
                )
                if user_input_key in student.keys():
                    break
                else:
                    print("Field does not exist. Please try again.")

            user_updated_info = input("Enter the new value: ")
            student[user_input_key] = user_updated_info
            print("Student information updated successfully!")
            break

    if not found:
        print("Student ID not found.")

                  
        
#Delete Student Info
def delete_student():
    if len(students) == 0:
        print('There are no students to delete !!!')
        return 
    #else:
    while True:
        del_input = input("Enter the id of the student:- ")
        if del_input.strip().lower() == 'exit':
            return 
        
        found = False
        for index, student  in enumerate(students):
            if student['student_id'] == del_input:
                students.pop(index)
                print('The student has been deleted !!!')
                found = True
                return      
                   
        if not found: 
            print('Student_id not found !!!')

#View All Students

def view_all_students():
    if len(students) == 0:
         print("NO Students exist in the database")
    else:        
      for stud in students:        
         print("--------------------------")
         print(stud['student_id'])
         print(stud['name'])
         print(stud['age'])
         print(stud['gender'])
         print(stud['student_class'])
         print("--------------------------")
    
    
#Search Student
def student_search():
    if len(students) == 0:
        print("DataBase is empty !!!")
        return
    while True:
        view_inp = input("Enter the id of the student or enter exit to leave:- ")
        if view_inp.strip().lower() == 'exit':
            return 
        
        found = False

        for student in students:
            if student['student_id'] == view_inp:
                print("--------------------------")
                print(f"Student ID : {student['student_id']}")
                print(f"Name       : {student['name']}")
                print(f"Age        : {student['age']}")
                print(f"Gender     : {student['gender']}")
                print(f"Class      : {student['student_class']}")
                print("--------------------------")
                found = True
                return 

        if not found:
            print('The student id does not exist pls enter the valid id or exit to leave !!!')

