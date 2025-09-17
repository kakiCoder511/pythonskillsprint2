# main terms for us to understand to effectively begin modelling objects and data...
    # the class - this is the entity we are modelling (e.g. the Car, the Animal, the Person, the House)

    # the object - this is the instance of the class/instance, which has data and behaviours attached to it (e.g. the BMW, the Dog, the Sam)

    # the attribute - this is the info, or the data, that relates to the object... on the class we denote what data is related to the entity we are modelling... on the object we assign actual value to these data points

    # the methods - this is the behaviour / the things it can do, on the class we define the details of this behaviour (the functionality)

    # the constructor - this is a special method which sets our data to the objects when instantiated

class GradeBook:
    def __init__(self, grades):
        self.grades = grades # dta belongs to the object

    def calculate_average(self):
        total = sum(self.grades)
        return total / len(self.grades)

    def display_average(self):
        average = self.calculate_average()
        print("The average Grade is: ",average)

def main():
    #create an instance of the GradeBook class
    gradebook = GradeBook([85,90,78,92,33])

# use the object methods
    gradebook.display_average()


main()

#class Vehicle
class Vehicle:
    #constructor
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    #method
    def start_engine(self):
        print(f"{self.make}{self.model} in {self.year}is running excellently fast")
    def honk(self):
        print(f"{self.make}engine has the best honk : Beep Beep!")
    def display_info(self):
        print(f"the plate will display the year of the car{self.year}")

#create an object instant
car1 = Vehicle("Toyota","Colla", 2023)
car2 = Vehicle("Benz", "AMG", 2025)

#use method
car1.display_info()
car2.start_engine()
car2.display_info()
car2.honk()


#OOP pillars
    # abstraction - hide implementation details and show only essential features, users don't need to know how it works internally, just how to use it
        # achieved in Python via abstract base classes

    # encapsulation - control over the data/attribute in a class, we can ensure attributes can only be updated from within the class.. i.e throught methods like setters
        # achieved in Python using
        #public (everywhere)
        #protected (child classes)
        #private(this class only)

    # polymorphism - same method name can behave differently depending on the object
        # achieved in Python using
        # method overriding (method with the same name, but different number of arguments)

   # inheritance - allow a child class to reuse and extend functionality from another class (parent)
        # in Python
        # a child class inherits using parenthesis: class Child(Parent)
        # supports single and multiple inheritance
        # super() function calls methods from the parent class


