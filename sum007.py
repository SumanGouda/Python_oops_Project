# class Pet :
#     def __init__ (self,name,animal_type,age):
#         self.name = name
#         self.animal_type = animal_type
#         self.age = age
        
#     def describe(self):
#         print(self.name," is a ",self.age, " year old ",self.animal_type)
        
# a1 = Pet("Nenk","cat",2)
# a2 = Pet("Tink","dog",3)
# Pet.describe(a1)
# Pet.describe(a2)

# class Student:
#     def __init__ (self,name):
#         self.name = name
#         self.grades = [8,6,9,5,7,9]
        
#     def average_grade(self):
#         return sum(self.grades) / len(self.grades)
  
#     def display_info(self):
#         avg = self.average_grade()
#         print("Your average grade is ",avg)
        
#     def status(self):
#         avg = self.average_grade()
#         if avg  >= 5:
#             print("You have passed the semester.")
#         elif avg < 5:
#             print("You did not passed the semester.")
            
# s1 = Student("Nenk Sine")
# s1.status()
# s1.display_info()



# f = open("demo.txt","r")  # if there is no such file and you still runned it then python will automatically create one for you

# data = f.read()
# print(data)         #this will print entire line. 
# print(type(data))

# line1 = f.readline() # only reads the signle line.
# print(line1)        #this will print a empty line because the cursor has reached the end and there is no more line for it to read so it will print an empty line.
                

# line2 = f.readline()
# print(line2)        #this will print a empty line because the cursor has reached the end and there is no more line for it to read so it will print an empty line.

# f.close()           # try to close the file always this is a sign of a good programer.


# f = open("demo.txt","w")  # this will delete the previous things on the txt file add the the new stuffs to the file.
# f.write ("this is my laptop") # this will going to add into that text file.

# f = open("demo.txt","a") # this will append the text into that file without removing the old stuffs.
# f.write ("\nthis is my laptop") # this will add into that file without removing the previous stuffs. \n is used to take the file into a new line.


# different important modes:
# a+ :   read + append      -  pointer at end    - no truncate
# w+ :   read + overwrite   -  truncate
# r+ :   read + overwrite   -  pointter at start  - no truncate

# f = open("D:\PYTON PROGRAMMING\PYTHON FILES\HELLO.txt","r")

# line1 = f.readline(5)
# print(line1)

# f.close()


# better syntax :
#      with open("D:\PYTON PROGRAMMING\PYTHON FILES\HELLO.txt","r") as f

# with open("D:\PYTON PROGRAMMING\PYTHON FILES\HELLO.txt","r") as f:      # when you use the with syntax it will automatically close your program after it is done you do not need to add f.close
#     line1 = f.readline(4)
#     #f.close   (no need)
    
# import os                  #to delete a file you need to import a module os
# os.remove("D:\PYTON PROGRAMMING\PYTHON FILES\HELLO.txt")             # this will delete the file.


# with open ("D:\PYTON PROGRAMMING\PYTHON FILES\Practice.txt","r") as f:
#     data = f.read()
    
#     new_data = data.replace("java","python")
#     print(new_data)
    
# with open ("D:\PYTON PROGRAMMING\PYTHON FILES\Practice.txt","w") as f:
#     f.write(new_data)

with open ("D:\PYTON PROGRAMMING\PYTHON FILES\Practice.txt","r") as f:
    data = f.read()
    if (data.find("learning")):
        print("found")
        
    



    