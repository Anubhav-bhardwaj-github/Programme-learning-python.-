def printhar(string):
    return f"Ye string harry ko de de thakur {string}"
def add(num1, num2):
    return num1 + num2 + 5

print("and the name is", __name__)

# if you want to import this file in another file then use the following command
#  so that the print statement will not exicute
if __name__ == '__main__':
    print(printhar("Harry1"))
    o = add(4, 6)
    print(o)