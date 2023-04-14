from Student import Student

# Create object 
student1 = Student("Bruce Wayne","Computer Science",8.7,False)
student2 = Student("Clark Kent","Mechanical Engineering",3.2,True)

print(student1.name + " GPA: " + str(student1.gpa))
print(student2.name + " GPA: " + str(student2.gpa))

print(student1.on_honor_roll())
print(student2.on_honor_roll())