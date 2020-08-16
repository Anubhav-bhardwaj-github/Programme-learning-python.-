# print("plese guse the number")
# while(True):
#     ip=int(input("enter a number : "))
#     if ip > 100 :
#         print("you have entered a number greater then orignal number")
#         continue
#     elif ip < 100 :
#         print("you have entered a number lesser then orignal number")
#         continue
#     elif ip == 100 :
#         print("you entered number is right")
#         break
# n = 18
# number_of_guesses = 1
# print("Number of guesses is limited to only 9 times: ")
# while (number_of_guesses <= 9):
#     guess_number = int(input("Guess the number :\n"))
#     if guess_number < 18:
#         print("you enter less number please input greater number.\n")
#     elif guess_number > 18:
#         print("you enter greater number please input smaller number.\n ")
#     else:
#         print("you won\n")
#         print(number_of_guesses, "no.of guesses he took to finish.")
#         break
#     print(9 - number_of_guesses, "no. of guesses left")
#     number_of_guesses = number_of_guesses + 1
#
# if (number_of_guesses > 9):
#     print("Game Over")
no_of_gusses = 1
while (no_of_gusses <= 7) :
    gusse = int(input("Enter your number : "))
    if gusse > 19 :
        print("number is greater")
    elif gusse < 19 :
        print("number is lesser")
    elif no_of_gusses > 9 :
        print("you loose")
    else:
        print(no_of_gusses , "no. of gusses you have used \t you won")
        break
    print(7 - no_of_gusses, " \t guesses left")
    no_of_gusses = no_of_gusses + 1

