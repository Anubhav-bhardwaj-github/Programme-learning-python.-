#####___You should learn___###########
# Abstraction
# Encapculation
# Inheritance
# Polymorphism

######___SOME__ACCESS__SPECIFIERS___################
# Public - EVERYONE
# Protected - WITH THE LINK CAN VIEW
# Private - ONLY YOU

class Employee:
    no_of_leaves = 8
    var = 8 #   THIS IS THE EXTENTOION OF PUBLIC
    _protec = 9 #   THIS IS THE EXTENTION FOR PROTECTED
    __pr = 98 #   THIS IS THE EXTENT OF PRIVATE

emp = Employee()
print(emp.var)
print(emp._protec)
print(emp._Employee__pr) #  FOR PRIVATE YOU HAVE TO USE CLASS NAME AS WELL

##################____POLYMORPHISM____############################
# print(5+4)
# print("5" + "4")
# polymorphism mean alag alag roop dharan kerna.

#################_____Super()__and__Overriding_____###############
class A:
    classvar1 = "I am a class variable in class A"
    def __init__(self):
        self.var1 = "I am inside class A's constructor"
        self.classvar1 = "Instance var in class A"
        self.special = "Special"
class B(A):
    classvar1 = "I am in class B"
    def __init__(self):
        self.var1 = "I am inside class B's constructor"
        self.classvar1 = "Instance var in class B"
        super().__init__()
        print(super().classvar1)
a = A()
b = B()
# print(b.special, b.var1, b.classvar1) # FOR MORE INFO. SEE TUT. NO. 65 (CODE WITH HARRY)
print(b.classvar1)