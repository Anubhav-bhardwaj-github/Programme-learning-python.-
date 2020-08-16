class Employee:
    no_of_leaves = 8

    def __init__(self, aname, asalary, arole):
        self.name = aname
        self.salary = asalary
        self.role = arole

    def printdetails(self):
        return f"The Name is {self.name}. Salary is {self.salary} and role is {self.role}"

    @classmethod
    def change_leaves(cls, newleaves):
        cls.no_of_leaves = newleaves

    def __add__(self, other):
        return self.salary + other.salary

    def __truediv__(self, other):
        return self.salary / other.salary

    def __repr__(self):
        return f"Employee('{self.name}', {self.salary}, '{self.role}')"
        # or self.printdetails()

    def __str__(self):
        return f"The Name is {self.name}. Salary is {self.salary} and role is {self.role}"
    @property #   WE WILL NOT BE REQURED FOR EXTRA ()PERENTHESIS
    def email(self):
        return f"the email is == {self.name}@gmail.com"

emp1 =Employee("Harry", 345, "Programmer")
# emp2 =Employee("Rohan", 55, "Cleaner")
print(emp1) # THE FIRST PREFERENCE IS STR METHOD
print(repr(emp1)) # TOU CAN CLL YOUR DISERED METHOD LIKE THIS
#   FOR MORE DUNDER METHOD I HAVE TAKEN 2 SCREENSHOTS NAMED PYTHON CLASS DUNDEN METHOD.
#   OR YPU COULD ALSO USE THE WEBSITE "maping operators to function"
print(emp1.email) # THIS IS BECAUSE OF PROPERTY METHOD