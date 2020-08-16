# 45*3=555 , 56+9=77 , 56/4=4
print("This is the faulty calculator made by me")
var1=int(input("Enter first number : "))
var3=input("Enter the operetion you want to perform")
var2=int(input("Enter second number : "))
if var1 == 45 and var2 == 3 and var3 == "*" :
    print(555)
elif var1 == 56 and var2 == 9 and var3 == "+" :
    print(77)
elif var1 == 56 and var2 == 4 and var3 == "/" :
    print(4)
elif var3 == "+" :
    print(var1 + var2)
elif var3 == "-" :
    print(var1 - var2)
elif var3 == "*" :
    print(var1 * var2)
elif var3 == "/" :
    print(var1 / var2)
else : print(var1 ** var2)