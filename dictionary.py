#Create dictionary name student_info.

student_info = {'Alice' : 78 ,'Adam' : 70, 'Daniel' :56 , 'Elon' : 80 , 'John' : 90}
#take user input for student name.
student_name = input("Enter the student name: ")
#check student name with the key is present in dictionary or not.
if student_name in student_info:
    print(student_name,"'s marks: ",student_info[student_name])
else:
    print("Student not found.")

