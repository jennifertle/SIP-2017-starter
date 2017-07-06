You are lost in the forest and desperate to find your way home.
'''


print(start)


print("Type 'left' to go left or 'right' to go right.")

user_input = input()
if user_input == "right":
    print("You choose to go right and you see a fire. You go towards the fire? Yes or No?")
if user_input == "left":
    print("You decide to go left and run into big foot. Do you 'run' or 'ignore'?") # finished the story by writing what happens
user_input = input()



if user_input == "run":
    print("You meet big foot's agressive family and unfortunately die. :( )")
    user_input = input()
if user_input=="ignore":
    print("You become friends with Big Foot and he eventually gives you directions of the location of a hidden boat and you get to go home.")



if user_input=="Yes":
    print("Yay! You found someone who can take you home.")
    user_input = input()
if user_input=="No":
    print("You get lost and die from starvation.")
