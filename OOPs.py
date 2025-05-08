class Student:
    def __init__(self,name,roll_number,grades):
        self.name = name
        self.roll_number = roll_number
        self.grades = grades
        
    def avg_grades(self):
        avg_grades = sum(self.grades) / len(self.grades)
           
        if avg_grades >= 50 :
            print("Your average grade is: ",avg_grades,"\n","You did not passsed the semester.")
        else:
            print("Your average grade is: ",avg_grades,"\n","You passsed the semester.")

class School:
    def __init__(self):
        self.students = {} 
        
    def add_student(self,student):
        self.students[student.roll_number] = student
        
    def remove_student(self,roll_number):
        if roll_number in self.students:
            del self.students[roll_number]
        
        else:
            print("No such student.")
        
    def show_all_students(self):
        for roll, student in self.students.items():
            print(f"Name: {student.name}, Roll: {roll}, Grades: {student.grades}")
            
s1 = Student("Alice", 101, [60, 70, 80])
s2 = Student("Bob", 102, [40, 45, 50])

school = School()
school.add_student(s1)
school.add_student(s2)

school.show_all_students()

s1.avg_grades()
s2.avg_grades()
        
               
               
class Product:
    def __init__(self,name,price,stock):
        self.name = name
        self.price = price
        self.stock =stock
        
class Cart:
    def __init__ (self):
        self.cart = {}
        
    def add_to_cart(self, product, quantity):
        if quantity <= product.stock:
            if product in self.cart:
                self.cart[product] += quantity
            
            else:
                self.cart[product] = quantity
            product.stock -= quantity
        
        else:
            print(f"{product.name} is out of stock.")
            
    def remove_from_cart(self,product,quantity):
        if product in self.cart:
            if quantity >= self.cart[product]:
                del self.cart[product]
            
            else:
                self.cart[product] - quantity
            product.stock +=quantity
        
        else:
            print("No such product in your cart.")
        
        
        
    def view_cart(self):
        print("\n--- Your Cart ---")
        for product, quantity in self.cart.items():
            print(f"{product.name} (x{quantity}) - ${product.price * quantity}")
            
    def checkout(self):
        if not self.cart:
            print("Your cart is empty.")
            return

        total = 0
        print("\n--- Checkout Summary ---")
        for product, quantity in self.cart.items():
            subtotal = product.price * quantity
            print(f"{product.name} (x{quantity}) - ${subtotal}")
            total += subtotal

        print(f"Total Amount: ${total}")
        self.cart.clear()
        print("Thank you for your purchase!")

        
p1 = Product("Apple", 2, 50)
p2 = Product("Milk", 3, 30)
p3 = Product("Bread", 4, 20)
p4 = Product("Chocolate", 5, 10)

cart = Cart()
cart.add_to_cart(p1, 5)     
cart.add_to_cart(p2, 2)    
cart.add_to_cart(p3, 1)

cart.view_cart()


cart.checkout()


        
