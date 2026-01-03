# This program calculate average, highest, and lowest marks, 
#and prints top scoring students


print("\nStudent Marks Analyzer")
print("----------------------")
# Creating a directory
students={
    "Aaila Ahmed":42,
    "Noor Fatima":39,
    "Areeba Zaheer":41,
    "Noor Ul Ain":40,
    "Um E Habiba":39,
    "Noor Ul Huda":29,
    "Momena Noor":28,
    "Amina Faisal":32,
    "Zil-e-Huma":26,
    "Alishba Jamil":39,
    "Bushra Rehman":36,
    "Tehreem Nazir":31,
    "Maida Nisar":41,
    "Seher Rubab":16,
    "Ayla Arzoo":32,
    "Rabiya Shaheen":34,
    "Eman Fatima":24,
    "Huma Farooq":23,
    "Kalsoom Khalid":37,
    "Esha Sultan":30,
    "Malaika Jameel":33,
    "Amna Imran":30,
    "Zarmina Rubab":30,
    "Almas Afzal":31,
    "Haleema Sadia":32,
    "Aiman Jamil":30,
    "Uzma Abid":0,
    "Areeba Basharat":36,
    "Nayab Sajid":25,
    "Zunaira Shahzad":24,
    "Minahil Imran":16,
    "Kainat Khalid":27,
    "Iraj Bibi":42,
    "Laraib Fiaz":33,
    "Mahrukh Kiyani":25,
    "Noor-ul-ain-zafran":10,
    "Zil-e-huma":27
}
print("\nSubject: System and Network Administration")

# Print names of students with their respective marks
print("Students Marks:\n")
for name,marks in students.items():
   print(name,":",marks)

total_marks=sum(students.values())
no_of_stds=len(students)

# Calculate Average
avg=total_marks/no_of_stds
print("\nThe average marks of the class for the given subeject is:",avg)

# Highest and Lowest Marks
highest=max(students.values())
lowest=min(students.values())
print("Highest Marks:",highest)
print("Lowest Marks:",lowest)

# Top scoring Student(s)(there can be multiple students having Top Score)
top_std= [name for name, marks in students.items() if marks==highest]
print("\nTop scoring students:")
for student in top_std:  
  print(student,"with",highest,"marks")