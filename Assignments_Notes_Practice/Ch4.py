#Working with Lists
print("------Chapter 4------")
print("This is in CHAPTOR 4 \n")


#A for look that prints every item in the list.
magicians = ['alice', 'david', 'carolina']
for magician in magicians:
  print(magician)

print()
#adding words
for magician in magicians:
  print(magician.title() + ", that was a great trick!")

print()
#Creating Sentinces
for magician in magicians:
  print(magician.title() + ", that was a great trick!")
  #dont forget to indent inside of a for loop
  print("I can't wait to see your next trick, " +     magician.title() + ".\n")
print("This is out of the for loop!")

print()
#Range(value1, Value2) function
for value in range(1,5):
 print(value)
  #It does not print 5 becasue of off-by-one behavior it includes the first value but not the last!!!

print()

for value in range(1,6):
 print(value)
  #here it prints 5 but not 6

print()
#here it puts the values in a list with the same range
numbers = list(range(1,6))
print(numbers)

#to only get even values we can do this
even_numbers = list(range(2,11,2)) #the two on the end is the value the range counts by 2 2+2 4+2 6+2
print(even_numbers)

even_numbers = list(range(2,17,3))#counts every 3
print(even_numbers)

#this prints square numbers
# (**) represent exponents
#the range it 1-10
#but then raises(**) it to the 2nd power and adds that number to the list 
squares = []
for value in range(1,11):
  square = value**2
  squares.append(square)
print(squares)
#you can also build the same expont right into the list itself rather than in the loop
squares = [value**2 for value in range(1,11)]
print(squares)

print()
#You can also pull min, max and sum from a list of numbers
digits = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
print(min(digits))
print(max(digits))
print(sum(digits))

print()
#slicing a list
players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players)
#Only prints player from 1-3 or index 0 to 2
print(players[0:3])
#You can start and stop at any index
print(players[1:4])
#Without a starting index, Python starts at the beginning of the list
print(players[:4])
#returns all items from the third item through the end of the list:
print(players[2:])
#prints the names of the last three players
print(players[-3:])

print()
#For loop to cycly through the first three players in the list
print("Here are the first three players on my team:")
for player in players[:3]:
 print(player.title())

#You can copy a list with the start and end indexes
my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]
print("My favorite foods are:")
print(my_foods)
print("\nMy friend's favorite foods are:")
print(friend_foods)
#above it coppied the whole list
#below it adds to mine and his list different items
my_foods.append('cannoli')
friend_foods.append('ice cream')
print("My favorite foods are:")
print(my_foods)
print("\nMy friend's favorite foods are:")
print(friend_foods)

#tuple
print()
dimensions = (200, 50)
print("\nOriginal dimensions:")
for dimension in dimensions:
 print(dimension)

dimensions = (400, 100)
print("\nModified dimensions:")
for dimension in dimensions:
 print(dimension)
# tuples are simple data structures and should be used when you want to store a set of values that should not be changed throughout the life of a program.
#You canot dimensions[0] = 250 modify an index like a list