student = {'Amit':92, 'Abhishek':89, 'Alice':85,
           'Aditi':80, 'Anuj':57,   'John':73,
           'Mike':76,  'Rechal':71,
           'Albert':98, 'Aradhya':75,
}

Name = input("Enter the student's name: ")
if Name in student:
    print(student[Name])

else:
    print("Student not found.")