print("Welcome to my game!")
name = input("What is your name? ")
age = int(input("What is your age? "))

#convert sting to int
#is_older = int(age) >=18
#print(is_older)
health= 10


if age >= 18:
  print("You are old enough!")
  print("You start with ", health, "health")

  
  wants_to_play = input("Do you want to play? ").lower()
  if wants_to_play == "yes":
    print("Lets Play! ")

    Left_Right = input("First Choice... Left or Right? (Left/Right)").lower()
    if Left_Right == "left":
      
      ans = input("Nice, You followed the path and reched a lake ... Do you swim Across or go Around? (Across/Around)").lower()
      if ans == "around":
        print("You got bit by a snake and lost 5 health")
        health -= 5
                  
      elif ans == "across":
        print("You got bit by a fish and lost 6 health")
        health -= 6

        ans = input("You see a river and see a house,  which do you go to? (river/hosue)").lower()
        if ans == "house":
          print("You go to the house the ower doesnt like you, you lose 5 health")
          health -= 5
        if ans == "river":
          print("You fell in the river and died.")

          if health <= 0:
            print("You have 0 heath and lost the game")
          
        

      else:
        print("you lose")
      
    else:
      print("You fell in a hole and died.")

    
  else:
    print("See ya!")
    
elif age >= 14:
    print("You may play supervised.")
else:
  print("You are not old enough to play...")
