class team() :
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname

    @property # By this we will not be required for any perenthesis()
    def email(self):
        if self.fname == None or self.lname == None :
            return "email is not set up yet...."
        return f"The email is [{self.fname}.{self.lname}@gmail.com]"

    @email.deleter # This decoretor is for deliting the emails
    def email(self):
        self.fname = None
        self.lname = None

    @email.setter # By this we can change the nemes for the emails
    def email(self, str):
        print("wirking....")
        name = str.split ("@") [0]
        self.fname = name.split(".") [0]
        self.lname = name.split(".") [1]

anubhav = team("Anubhav", "Bhardwaj")
himanshu = team("Himanshu", "Gangwar")
print(anubhav.email)
anubhav.email = "anubhav.best@gmail.com"
# del anubhav.email # This is the command for deleting the emails
print(anubhav.email)