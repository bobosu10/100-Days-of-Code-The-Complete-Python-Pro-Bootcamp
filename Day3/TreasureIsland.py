print(''',,
`""*$b..
     ""*$o.
         "$$o.
           "*$$o.
              "$$$o.
                "$$$$bo...       ..o:
                  "$$$$$$$$booocS$$$    ..    ,.
               ".    "*$$$$SP     V$o..o$$. .$$$b
                "$$o. .$$$$$o. ...A$$$$$$$$$$$$$$b
          ""bo.   "*$$$$$$$$$$$$$$$$$$$$P*$$$$$$$$:
             "$$.    V$$$$$$$$$P"**""*"'   VP  * "l
               "$$$o.4$$$$$$$$X
                "*$$$$$$$$$$$$$AoA$o..oooooo..           .b
                       .X$$$$$$$$$$$P""     ""*oo,,     ,$P
                      $$P""V$$$$$$$:    .        ""*****"
                    .*"    A$$$$$$$$o.4;      .
                         .oP""   "$$$$$$b.  .$;
                                  A$$$$$$$$$$P
                                  "  "$$$$$P"
                                      $$P*"
    mls                              .$"
                                     "   ''')
direction = input("Welcome to Treasure Island! Your mission is to find the treasure.\nYou`re at a cross road. Where do you want to go?\n Type left or right: ").lower()
if direction == "right":
    print("Fall into a hole\nGAME OVER")
elif direction == "left":
    direction = input("'You've come to a lake. There is an island in the middle of the lake.\nType 'wait' to wait for a boat. Type 'swim' to swim across. ").lower()
    if direction == "wait":
        direction = input("You arrive at the island unharmed. There is a house with 3 doors.One red, one yellow and one blue. Which colour do you choose? ").lower()
        if direction == "red":
            print("burned by fire\nGAME OVER")
        elif direction == "yellow":
            print("YOU WIN")
        elif direction == "blue":
            print("Eaten by beasts\nGAME OVER")
        else:
            print("YOU LOSE\nGAME OVER")
    else:
        print("Attacked by trout\nGAME OVER")

