# Program title
print("Students marks analyzer")
print("-----------------------")

# Ask user how many subjects are there
no_of_subjects=int(input("\nEnter the number of subjects:"))

# List to store subject names
subjects=[]
no_of_students=int(input("Enter the number of students:"))

# Dictionary to store total marks of each student across all subjects
overall_total={}

# List to store all marks (used later for class average
all_marks=[]

# Loop for each subject
for i in range(no_of_subjects):
    
    # If there is more than one subject, show subject number
    if no_of_subjects>1:
       subject=input(f"Enter the name of subject number {i+1}:")
    else:
       subject=input("Enter subject name:")


    # Store subject name
    subjects.append(subject)

    # Dictionary to store marks of students for THIS subject only
    students={}

    # Loop for each student
    for student in range(no_of_students):
     
     # Take student name
     name=input(f"\nEnter the name of the student number {student+1}:")

     # Take marks and convert to float
     marks=float(input(f"Enter the marks of {name}:"))

     # Store marks for the subject
     students[name]=marks
     
     # Store marks in list for class average
     all_marks.append(marks)

     # Add marks to overall total (for topper calculation)
     if name in overall_total:
        overall_total[name]+=marks
     else:
        overall_total[name]=marks

    # Display subject-wise analysis
    print("\nSubject:",subject)

    # Find highest and lowest score in this subject
    highest_score=max(students.values())
    lowest_score=min(students.values())

    print(f"Highest score of {subject} is:{highest_score}")
    print(f"Lowest score of {subject} is: {lowest_score}")

    # Calculate average marks of this subject
    average=sum(students.values())/len(students)
    print(f"Average score of {subject} is: {average:.2f}")
    
    # Print top-performing student(s) for the subject
    top_student=[name for name, marks in students.items() if marks==highest_score]
    for student in top_student:
      print(f"Top performing student(s) of {subject} is {student} with {highest_score} marks.\n")


# Calculate overall class average (all students, all subjects)
class_average=sum(all_marks)/len(all_marks)
print(f"\nAverage result for all students of the class is:{class_average:.2f}")

# Sort students based on total marks (descending order)
sorted_students=sorted( overall_total.items(),
                            key=lambda x:x[1],   # sort using total marks
                            reverse=True         # highest first
                          )
    
# Get class topper (highest total marks)
topper_name,topper_marks=sorted_students[0]
print(f"Topper of the class:{topper_name} with {topper_marks} marks.")
