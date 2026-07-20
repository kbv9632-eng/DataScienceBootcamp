from services.student_service import (
    add_student,
    update_student,
    delete_student,
    student_search,
    view_all_students,
)

# Welcome Msg 
print("Welcome to Student Management System!")

#Loop - Menu for the system 

while True:
    print("-----Student Management System-------")
    print("1. Add Student")
    print("2. Update Student")
    print("3. Delete Student")
    print("4. Search for Student")
    print("5. View all Students")
    print("0. To exit")
# User Input 
    user_input= int(input("What action would like to perform : "))

    if user_input == 1:
        add_student()        
    elif user_input == 2:
        update_student()
    elif user_input == 3:
        delete_student()
    elif user_input == 4:
        student_search()
    elif user_input == 5:
        view_all_students()
    elif user_input == 0:
        print("Thank You See you Later!!!")
        break
    else:
        print("Invalid Choice. Please select from the menu")
    