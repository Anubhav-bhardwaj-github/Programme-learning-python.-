# name Harry and rohan and hammad
def getdate() :
    import datetime
    return datetime.datetime.now()
name_list = ["Harry" , "Rohan" , "Hammad"]
type = ["Dite" , "Exercise"]
catogary_list = ["retrieve" , "lock"]
print(name_list)
name = int(input("press 1 for harry , 2 for rohan and 3 for hammad \n"))
print(type)
type1 = int(input("press 1 for dite and 2 for exercise \n"))
print(catogary_list)
catogary = int(input("press 1 for retrieveing your data and 2 for locking your data \n"))
if name == 1 :
    if type1 == 1 :
        if catogary == 2 :
            with open("harry food.txt", "a") as h_lock :
                 ram = h_lock.write(str(input("enter your dite here without pressing enter\n")))
                # print(str([getdate()] + (ram)))
                 h_lock.write(str([str(getdate())]) + ": " + ram + "\n")
# h_lock.write(str(input("enter your dite here without pressing enter\n")))

        elif catogary == 1 :
            with open("harry food.txt", "r") as h_view :
                print("here is your past dite info below")
                print(h_view.read())
                # ram1 = h_view.read()
    elif type1 == 2 :
        if catogary == 2 :
            with open("harry exercise.txt" , "a") as h_ex_lock :
                h_ex_lock.write(str(input("Enter your exercise here without presinh enter\n")))
        elif catogary == 1 :
            with open("harry exercise.txt" , "r") as h_ex_view :
                print("Here is your past Exercise info below")
                print(h_ex_view.read())
elif name == 2 :
    if type1 == 1 :
        if catogary == 2 :
            with open("rohan food.txt" , "a") as r_lock :
                r_lock.write(str(input("Enter your data without pressing enter\n")))
        elif catogary == 1 :
            with open("rohan food.txt" , "r") as r_view :
                print("Here is your past Dite info brlow")
                print(r_view.read())
    elif type1 == 1 :
        if catogary == 2 :
            with open("rohan exercise.txt") as r_ex_lock :
                r_ex_lock.write(str(input("Enter your data without pressing enter\n")))
        elif catogary == 1 :
            with open("rohan exercise.txt" , "r") as r_ex_view :
                print("Here is your past exercise info brlow")
                print(r_ex_view.read())
elif name == 3 :
    if type1 == 1 :
        if catogary == 2 :
            with open("harry food.txt" , "a") as h_lock :
                h_lock.write(str(input("Enter your dite without pressing enter\n")))
        elif catogary == 1 :
            with open("harry food.txt" , "r") as h_view :
                print("Here is your past Dite info below")
                print(h_view.read())
    elif type1 == 2 :
        if catogary == 2:
            with open("harry exercise.txt" , "a") as h_ex_lock :
                h_ex_lock.write(str(input("Enter your exercise without pressing enter\n")))
        elif catogary == 1 :
            with open("harry exercise.txt" , "r") as h_ex_view :
                print("Here is your Exercise info below")
                print(h_ex_view.read())
print("\nThanks for coming here \nAnd i will see you next time")
#
#
# import datetime
# def gettime():
#     return datetime.datetime.now()
# def take(k):
#     if k==1:
#         c=int(input("enter 1 for excersise and 2 for food"))
#         if(c==1):
#             value=input("type here\n")
#             with open("harry-ex.txt","a") as op:
#                 op.write(str([str(gettime())])+": "+value+"\n")
#             print("successfully written")
#         elif(c==2):
#             value = input("type here\n")
#             with open("harry-food.txt", "a") as op:
#                 op.write(str([str(gettime())]) + ": " + value + "\n")
#             print("successfully written")
#     elif(k==2):
#         c = int(input("enter 1 for excersise and 2 for food"))
#         if (c == 1):
#             value = input("type here\n")
#             with open("rohan-ex.txt", "a") as op:
#                 op.write(str([str(gettime())]) + ": " + value + "\n")
#             print("successfully written")
#         elif (c == 2):
#             value = input("type here\n")
#             with open("rohan-food.txt", "a") as op:
#                 op.write(str([str(gettime())]) + ": " + value + "\n")
#             print("successfully written")
#     elif(k==3):
#         c = int(input("enter 1 for excersise and 2 for food"))
#         if (c == 1):
#             value = input("type here\n")
#             with open("hammad-ex.txt", "a") as op:
#                 op.write(str([str(gettime())]) + ": " + value + "\n")
#             print("successfully written")
#         elif (c == 2):
#             value = input("type here\n")
#             with open("hammad-food.txt", "a") as op:
#                 op.write(str([str(gettime())]) + ": " + value + "\n")
#             print("successfully written")
#     else:
#         print("plz enter valid input (1(harry),2(rohan),3(hammad)")
# def retrieve(k):
#     if k==1:
#         c=int(input("enter 1 for excersise and 2 for food"))
#         if(c==1):
#             with open("harry-ex.txt") as op:
#                 for i in op:
#                     print(i,end="")
#         elif(c==2):
#             with open("harry-food.txt") as op:
#                 for i in op:
#                     print(i, end="")
#     elif(k==2):
#         c = int(input("enter 1 for excersise and 2 for food"))
#         if (c == 1):
#             with open("rohan-ex.txt") as op:
#                 for i in op:
#                     print(i, end="")
#         elif (c == 2):
#             with open("rohan-food.txt") as op:
#                 for i in op:
#                     print(i, end="")
#     elif(k==3):
#         c = int(input("enter 1 for excersise and 2 for food"))
#         if (c == 1):
#             with open("hammad-ex.txt") as op:
#                 for i in op:
#                     print(i, end="")
#         elif (c == 2):
#             with open("hammad-food.txt") as op:
#                 for i in op:
#                     print(i, end="")
#     else:
#         print("plz enter valid input (harry,rohan,hammad)")
# print("health management system: ")
# a=int(input("press 1 for lock the value and 2 for retrieve "))
#
# if a==1:
#     b = int(input("press 1 for harry 2 for rohan 3 for hammad "))
#     take(b)
# else:
#     b = int(input("press 1 for harry 2 for rohan 3 for hammad "))
#     retrieve(b)