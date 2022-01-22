from cgitb import handler


print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

# https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload

# Write your code below this line 👇

# My Code
choice1 = input("You are at a fork in the road. "
                "Going left takes you on a long mountainous route, "
                "whereas going right takes you along a beach. "
                "Do you want to go left or right? ").lower()
if choice1 == "left":
    choice2 = input("You come across a sign that says "
                    'Warning: Flash Flooding. '
                    "However, the river doesn't seem too deep. "
                    "Do you swim or wait? ").lower()
    if choice2 == "wait":
        choice3 = input("You make it to three different doors. "
                        "The first is black with a gold handle. "
                        "The second is silver with a triangle handle. "
                        "The third is blue with a red orb in the middle. "
                        "Which door do you choose? "
                        "Black, Silver, or Blue? ").lower()
        if choice3 == "black":
            print("You run into Shia Labeouf and can't help but "
                  "sing the song 'Shia Labeouf'. "
                  "You run for your life from Shia Labeouf, "
                  "but he gets you. Game Over.")
        elif choice3 == "silver":
            print("You run into Newman saying you forgot the magic word. "
                  "As you fiddle with the computer to open the treasure chest."
                  " A raptor sneaks up behind you and you become a wonderful "
                  "ingredient to a raptor shepard's pie. Game Over.")
        elif choice3 == "blue":
            print("Congratulations! Willy Wonka pops out of the treasure chest"
                  " singing 'Pure Imagination' which is really the reward from"
                  " the chest: your imagination. You Win? I guess?")
    else:
        print("You hear the magic conch shell and suddenly a rush of water "
              "comes down the river. Should have read the sign. Game Over.")
else:
    print("Yum! You have been eaten by a group of hungry cannibals. "
          "Game Over.")