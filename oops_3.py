class team() :
    no_of_leaves = 8 #  IT IS A TEMPLATE OF CLASS AND    IT IS A CLASS VARIABLE
    def __init__(self , aname , astd , asec): # IT IS A METHOD AND IT IS A CONSTRUCTOR
        self.name = aname # THESE ARE INSTANCE VARIABLE OS CLASS TEAM
        self.std = astd
        self.sec = asec
    def printdetails(self):
        return f"The name of the student is {self.name} and study in class{self.std} and section is {self.sec}"
    def about(self) : # IT IS A METHOD
        return f"\tSEARCH RESULT FOR {self.name}\nThe name is {self.name}.\nreads " \
               f"in class {self.std}.\nsection is {self.sec}."

    @classmethod # if we want to change the class contant by an instanse variable
    def change_leaves(cls, new_leaves):
        cls.no_of_leaves = new_leaves

    @classmethod #  IT IS A DECORATOR
    def from_dash(cls, string):
    # params = string.split("-")
    # print(params)
    # return cls(params[0], params[1], params[2])
        return cls(*string.split("-"))
    @staticmethod
    def pri_somthing(str): #   IF YOU WANT YOU TAKE ANY ARGUMENT ONLY GIVE OUTPUT
        print("This is good thing " + str)
class The_boss(team) : #    THIS IS THE WAY TO CALL A CLASS
    pass
# anubhav = team()
# himanshu = team() #   IT IS A team nam ka object
# bowin = team()
# anurag = team()
bowin = team.from_dash("Bowin-9th-Theresa") #   ALTERNATIVE CONSTRUCTOR
anubhav = team("Anubhav" , "9th" , "Theresa") # INSTANCE VARIABLE
himanshu = team("Himanshu" , "9th" , "Theresa")
anurag = team("Anurag" , "9th" , "Theresa")
# anubhav.change_leaves(200)
# print(anubhav.no_of_leaves)
# print(bowin.about())
# print(anubhav.__dict__)
# anubhav.pri_somthing("hello")
# print(anubhav.from_dash("he-is-a-good-doy"))
print(bowin.printdetails())