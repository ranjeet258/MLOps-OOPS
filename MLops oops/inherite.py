# # concepts of inheritance in python
# # Inheritance is a fundamental object-oriented programming (OOP) concept that allows a new class
# # (called a child class or subclass) to inherit attributes and methods from an existing class (called a parent class or superclass). This promotes code reusability and establishes a natural hierarchical relationship between classes.

# class animal:
#     def __init__(self):
#         self.name = "Animal"
    
#     def speak(self, sound):
#         print (f"Animal speaks: {sound}")


# class dog(animal):
#     # def __init__(self):
#     #     super().__init__()  # calling the __init__ method of the parent class (animal) to initialize the name attribute
#     #     self.name = "Dog"   # overriding the name attribute in the dog class
#     def speak(self, sound):
#         print (f"Dog speaks: {sound}")  # overriding the speak method in the dog class to provide a different implementation

# dog1 = dog()
# print(dog1.name)  # Output: Dog

# '''here speak method is inherited from the animal class to the dog class, 
# which means that we can call the speak method on an instance of the dog class, 
# and it will execute the code defined in the animal class. However, since we have overridden the name attribute 
# in the dog class, when we access dog1.name, it will return "Dog" instead of "Animal". When we call dog1.speak("Woof!"),
#  it will execute the speak method defined in the animal class, which prints "Animal speaks: Woof!" instead of "Dog speaks: Woof!" because we have not overridden the speak method in the dog class.
#  If we want to override the speak method in the dog class to provide a different implementation, we can define a new speak method in the dog class that will override the one inherited from the animal class.'''
 
# dog1.speak("Woof!")  # Output: Dog speaks: Woof! , Requred argument sound, which is passed as an argument when calling the speak method on the dog1 instance. The speak method in the dog class overrides the speak method in the animal class, so when we call dog1.speak("Woof!"), it executes the speak method defined in the dog class, which prints "Dog speaks: Woof!" instead of "Animal speaks: Woof!"

# animal1 = animal()
# print(animal1.name)  # Output: Animal


#lets learn supper() function in python
# The super() function in Python is used to call a method from the parent class. It is commonly used in the __init__ method of a child class to ensure that the parent class's __init__ method is called, allowing the child class to inherit and initialize attributes from the parent class.
class animal:
    def __init__(self):
        self.name = "Animal"
    
    def speak1(self, sound):
        print (f"Animal speaks: {sound}")

class dog(animal):
    def __init__(self):
        super().__init__()  # Calling the __init__ method of the parent class (animal) to initialize the name attribute
        self.name = "Dog"   # overriding the name attribute in the dog class, when we override the name attribute in the dog class, it will take precedence over the name attribute defined in the animal class. This means that when we create an instance of the dog class and access the name attribute, it will return "Dog" instead of "Animal". The super().__init__() call is not necessary in this case because we are not using any attributes or methods from the parent class that require initialization. However, if we were to use any attributes or methods from the parent class that require initialization, we would need to call super().__init__() to ensure that those attributes are properly initialized.
    
    def speak(self, sound):
        super().speak1(sound)  # calling the speak1 method from the parent class (animal) using super() to reuse the implementation of the speak1 method in the animal class
        print (f"Dog speaks: {sound}")  # overriding the speak method in the dog class to provide a different implementation

dog1 = dog()
dog1.speak("Woof!")  # Output: Dog speaks: Woof!
dog1.speak1("Woof!")  # Output: Animal speaks: Woof! 
print(dog1.name)   # overriding the name attribute in the dog class

















