#imoji
print("⋆༺𓆩☠︎︎𓆪༻⋆")
print("there are two doors in front of you: a red door 🚪 and blue door 🚪")
door_choice = input("which door do you want open ? \n ").lower()

#check user's choice

if door_choice == "red" :
    print("Great ! Now you entered a room " \
    "you found three boxes:🗂️ white ,🗂️ black , 🗂️ green")
    choice_box = input("which box do you want to open ?\n").lower()

    #check user's choice for the first chest

    if choice_box == "white" :
        print("Oops! you opened a box filled with snakes 🐍🐍🐍. ")
    elif choice_box == "black" :
        print("oops! you opened a box filled with spiders 🕷️ 🕷️🕷️.")
    elif choice_box == "green" :
        print("Congratulations ! you found the treasure 🎁🎁🎁 !")
    else :
        print("Invalid choice 🤔")
elif door_choice == "blue" :
    print("oops! you chose the crocodile door 🐊🐊🐊 ," \
    " Game over")
else :
    print("invalid choice 🤔")





