import random
options =("r","s","p")
choice_comp=random.choice(options)
user_input =input("Enter the choice r(-rock) ,s(-scissors) & p(-paper)")
print("Computer =" + choice_comp)
print("user_input = "+ user_input)
if choice_comp == user_input :
    print("Tie")
elif choice_comp == "r" and user_input == "s":
    print("Computer win")
elif choice_comp == "s"  and user_input =="p":
     print("Computer Win")   
elif choice_comp == "p" and user_input == "r":
   print ("Computer Win")   
else:
   print("User Wins")

