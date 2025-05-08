# --- OOP SECTION ---

class Pet:
    def __init__(self, name, animal_type, age):
        self.name = name
        self.animal_type = animal_type
        self.age = age

    def describe(self):
        print(f"{self.name} is a {self.age}-year-old {self.animal_type}.")


a1 = Pet("Nenk", "cat", 2)
a2 = Pet("Tink", "dog", 3)
a1.describe()
a2.describe()


class Student:
    def __init__(self, name):
        self.name = name
        self.grades = [8, 6, 9, 5, 7, 9]

    def average_grade(self):
        return sum(self.grades) / len(self.grades)

    def display_info(self):
        avg = self.average_grade()
        print(f"{self.name}'s average grade is {avg:.2f}")

    def status(self):
        avg = self.average_grade()
        if avg >= 5:
            print("You have passed the semester.")
        else:
            print("You did not pass the semester.")


s1 = Student("Nenk Sine")
s1.status()
s1.display_info()


# --- FILE HANDLING SECTION ---

# Reading file using best practice
file_path = r"D:\PYTON PROGRAMMING\PYTHON FILES\Practice.txt"

# Read and check if 'learning' exists
try:
    with open(file_path, "r") as f:
        data = f.read()
        if "learning" in data:
            print("Found 'learning' in the file.")
        else:
            print("'learning' not found.")
except FileNotFoundError:
    print("File not found.")

# Replace "java" with "python" and overwrite the file
try:
    with open(file_path, "r") as f:
        data = f.read()

    new_data = data.replace("java", "python")

    with open(file_path, "w") as f:
        f.write(new_data)
    print("Replaced 'java' with 'python' successfully.")
except FileNotFoundError:
    print("Cannot replace text. File not found.")



