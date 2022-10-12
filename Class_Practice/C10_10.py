entrees  = ['Shark', 'Dolphin', 'Narwhal']
AddOns1 = ['Rice', 'Beans']
for Food in entrees:
  print("---------Todays entree---------")
  print('On todays menu you can get the', Food, 'with a side of')
  print("---------Add Ons---------")
  for side in AddOns1:
    print(side)
  print()


squares = []
for value in range(1,11):
  square = value**2
  squares.append(square)
print(squares)



fours = []
for value in range(1,11):
  four = value**4
  fours.append(four)
print(fours)

fives = []
for value in range(1,11):
  five = value**5
  fives.append(five)
print(fives)
