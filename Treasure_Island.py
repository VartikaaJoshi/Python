print("Welcome to Treasure Island!"+ "\nYour mission is to find the treasure")

first_step = input("In which direction you want to go? Type L for left and R for right: ")


if first_step == "L":
  second_step = input("Do you want to swim or wait? Type S for swim and W for wait: ")
  if second_step == "W":
    door = input("Which door you want to enter? Type R for red, B for blue and Y for yellow: ")
    if door == "Y":
      print("You win!")
    else:
      print("Game Over!")

  else:
    print("Game Over!")

else:
  print("Game Over!")

    
