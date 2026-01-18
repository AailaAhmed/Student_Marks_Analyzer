#Student Marks Analyzer (Interactive)
#User enters student names and scores

print("Student Marks Analyzer")
print("----------------------")

students={}

std=int(input("\nHow many students in the class? "))
subject=input("Enter Subject Name: ")

for i in range(std):
    name=input(f"\nEnter full name of student no. {i+1}: ")
    marks=int(input(f"Enter marks of {name}: "))
    students[name]=marks

#Print all students
print("\nStudent Marks")
for name,marks in students.items():
    print(name,":",marks)

#Highest & Lowest marks
highest_score=max(students.values())
lowest_score=min(students.values())
print("\nHighest marks: ",highest_score)
print("lowest marks: ",lowest_score)

#Calculate Average
avg_marks=sum(students.values())/len(students)
print("Average marks: ",round(avg_marks,2))

#Top scoring students(s)
top_std=[name for name,marks in students.items() if marks==highest_score]
print(f"Top performing student(s) in {subject} is {name} with {highest_score} marks")