# let make a classs

class Employee:
    def __init__(self):
        self.name = "John"
        self.id = "234"
        self.salary = 50000
        print("Employee created")

    def travel(self, destination):
        print(f"Travelling to {destination}")


sam = Employee()
print(sam.id)
#sam.name = "Sam"  # adding a new attribute to the instance sam, which is not defined in the class Employee. This is possible in Python because it is a dynamic language, and we can add attributes to instances at runtime. However, it is generally not recommended to add attributes to instances that are not defined in the class, as it can lead to confusion and make the code harder to maintain.

# # calling a method
# sam.travel("New York")

print(type(sam))