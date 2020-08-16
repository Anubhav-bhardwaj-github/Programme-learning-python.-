# take = int(input("please enter 1 or 0 : "))
# file = open("theven.txt" , "r")
# if take == 1 :
#     r = file.read(13)
#     print(r)
# elif take == 0 :
#     file2 = open("theven2.txt" , "r") ; a = file2.read(13)
#     print(a)
# else : print("there is an error please enter 0 or 1")
print("How Many Row You Want To Print")
one= int(input())
print("Type 1 Or 0")
two = int(input())
new =bool(two)
if new == True:
    for i in range(1,one+1):
        for j in range(1,i+1):
            print("*",end=" ")
        print()
elif new ==False:
    for i in range(one,0,-1):
        for j in range(1,i+1):
            print("*", end="")
        print()