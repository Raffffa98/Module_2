
isGameRunning = True

print ("Hello, I want to play a game")
print("You are in an abandonned bathroom with your'e foot chained to the floor, there is a rusty saw on the floor... what do you do nex?")

    options = ["Yell for help", "fdsfds", "zdsad"]
    first_item = options[0]
    second_item = options[1]
    third_item = options[2]

    while (isGameRunning):

        action = input().lower()

         if action != ("cut off leg"):
        print (f"The Player is {action}")
        print ("The Game continues...")
        isGameRunning = True
        continue

         else:
             print (f"The Player is {action}")
             print ("Some People are so ungreatful to be alive, but not you, not anymore")
             print ("GAME OVER!")
            isGameRunning = False
         break

 