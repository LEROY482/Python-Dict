student = {"name": "Teargas",
"email": "Mayoto@gmail.com",
"Phone_no": 178956432,
"Birthday": "January 21",
"Car": "Toyota",#always add commas at the end
}
print (student)
Teargas= student ["email"]#Using the "Key" i.e Teargas (name of the student) we can get the email.
print (Teargas)
Teargas= student.get("email")
print (Teargas)
Teargas= student.get("Birthday")
print (Teargas)
student ["name"]="Fred"#using this method, we can change things in the dictionary.
print (student)
student ["email"]= "trevor@gmail.com"#using change values method, anything in the dictionary can be changed.
print (student)
for Birthday in student: #the following method allows looping through the keys
  print (Birthday)
for Teargas in student.values():# Using this method, we loop through the values instead of the keys
  print (Teargas)
for k, v in student.items():#this methods shows everything in the dictionary
  print (k, v)
if  "Birthday" in student:# This shows you if an item (i.e "The key") is in the dictionary.
  print ("Birthday is there")
if "Doktari" not in student:# This shows that that the item is not in the dictionary
  print ("Doktari is not there")
  #Adding items in then dictionary
student ["Company"]= "Sony"
print (student)
student ["university"]= "Egerton"
print (student)
#Removing an item from the dictionary
student.pop("Birthday")
print (student)
#print length of the dictionary
print(len(student))
#copying the dictionary
student = student.copy()
print(student)
#Updates items in the dictionary
student.update({"Jacket":"Subaru"})
print (student)
# values method returns a view object that contains the values of the dictionary, as a list.
student = student.values()
print (student)
#Giving a list of keys in the dictionary
student = student.keys()
print(student)