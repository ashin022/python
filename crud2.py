
students = [
    {'id':'101','name':'Aswin','rno':'1','course':'BCA'},
    {'id':'102','name':'Arun','rno':'2','course':'BCA'},
    {'id':'103','name':'Anwin','rno':'3','course':'BCA'}
]
while True:
    choice = input("1. Add a student name\n2. Display student names\n3. Update a student name\n4. Remove a student\n5. Exit\nEnter your choice: \t")
    match choice:
        case "1":
            id=input("Enter student id: ")
            name = input("Enter the name: ")
            rno = input("Enter the roll no.: ")
            course = input("Enter the course: ")
            students.append({"id":id,"name":name,"rno":rno,"course":course})
        case "2":
            print(f"{'Sl. No.':<10}{'id':<4}{'Name':<10}{'Roll No.':<10}{'Course':<10}")
            for index,student in enumerate(students):
                print(f"{index+1:<10}{student['id']:<4}{student['name']:<10}{student['rno']:<10}{student['course']:<10}")
            print(f"Total names:{len(students):>5}")
        case "3":
            print(f"{'Sl. No.':<10}{'id':<4}{'Name':<10}{'Roll No.':<10}{'Course':<10}")
            for index,student in enumerate(students):
                print(f"{index+1:<10}{student['id']:<4}{student['name']:<10}{student['rno']:<10}{student['course']:<10}")
            edit_id = input("Enter the id of the student you want to edit: ")
            for student in students:
                if student['id'] == edit_id:
                    student['name'] = input("Enter the name: ")
                    student['rno'] = input("Enter the roll no.: ")
                    student['course'] = input("Enter the course: ")
        case "4":
            print(f"{'Sl. No.':<10}{'id':<4}{'Name':<10}{'Roll No.':<10}{'Course':<10}")
            for index,student in enumerate(students):
                print(f"{index+1:<10}{student['id']:<4}{student['name']:<10}{student['rno']:<10}{student['course']:<10}")
            delete_id = input("Enter the id of the student you want to remove: ")
            for student in students:
                if student['id'] == delete_id:
                    students.remove(student)
        case "5":
            print("Exiting...")
            break
        case _:
            print("invalid Entry")