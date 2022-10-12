entrees  = ['Shark', 'Dolphin', 'Narwhal']
AddOn = ['Rice', 'Beans']
AddOn1 = ['Table', 'Desk']
num = 1
for Food in entrees:
  print("---------Todays entree---------")
  print('On todays menu you can get the', Food, 'with a side of')
  print("---------Add Ons---------")
  for side in AddOn:
    print(side)
    var_holder['AddOn' + str(side)] = "iterationNumber=="+str(side)
     
  print()