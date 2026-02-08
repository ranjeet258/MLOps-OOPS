# let make a classs

class Employee:
    def __init__(self):
        self.id = "234"
        self.salary = 50000
        print("Employee created")

    def travel(self, destination):
        print(f"Travelling to {destination}")


sam = Employee()
print(sam.id)

# # calling a method
# sam.travel("New York")

print(type(sam))