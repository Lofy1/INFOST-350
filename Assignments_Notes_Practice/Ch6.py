#Dictionaries

#Git
'''
GIT stores a copy of the project then each user pull down a local copy to work on and pushes it back to the clould copy and git takes care of the changes.
'''
#dictinary
'''
Dictinarys can hold all sorts of varibles 
'''

#has the title color or points then holds a value such as string or int with that title
alien_0 = {'color': 'green', 'points': 5}
print(alien_0['color'])
print(alien_0['points'])

#adds a new item in the dict and adds an int for that title
new_points = alien_0['points']
print("You just earned " + str(new_points) + " points!")

#adds two items x and y postion then add the num to that
alien_0['x_position'] = 0
alien_0['y_position'] = 25
print(alien_0)

#Change a value in the dict
print("The alien is " + alien_0['color'] + ".")
alien_0['color'] = 'yellow'
print("The alien is now " + alien_0['color'] + ".")


alien_0 = {'x_position': 0, 'y_position': 25, 'speed': 'medium'}
print("Original x-position: " + str(alien_0['x_position']))

# Move the alien to the right.
# Determine how far to move the alien based on its current speed.
if alien_0['speed'] == 'slow':
 x_increment = 1
elif alien_0['speed'] == 'medium':
 x_increment = 2
else:
 # This must be a fast alien.
 x_increment = 3
# The new position is the old position plus the increment.
alien_0['x_position'] = alien_0['x_position'] + x_increment
print("New x-position: " + str(alien_0['x_position']))


#A Dictionary of Similar Objects
favorite_languages = {
 'jen': 'python',
 'sarah': 'c',
 'edward': 'ruby',
 'phil': 'python',
 }

print("Sarah's favorite language is " +
favorite_languages['sarah'].title() +
".")


for name, language in favorite_languages.items():
  print(name.title() + "'s favorite language is " +
  language.title() + ".")
  friends = ['phil', 'sarah']

  
for name in favorite_languages.keys(): 
  print(name.title())

if name in friends:
 print(" Hi " + name.title() +
 ", I see your favorite language is " +
  favorite_languages[name].title() + "!")

#Looping Through All Key-Value Pairs
user_0 = {
 'username': 'efermi',
 'first': 'enrico',
 'last': 'fermi',
 }

for key, value in user_0.items():
  print("\nKey: " + key)
  print("Value: " + value)

print("")
print("")
print("")

#make 30 green   aliens
alien_0 = {'color': 'green', 'points': 5}
alien_1 = {'color': 'yellow', 'points': 10}
alien_2 = {'color': 'red', 'points': 15}

aliens = [alien_0, alien_1, alien_2]
for alien in aliens:
 print(alien)

  # Make an empty list for storing aliens.
aliens = []
# Make 30 green aliens.
for alien_number in range(30):
  new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
  aliens.append(new_alien)

# Show the first 5 aliens:
for alien in aliens[:5]:
 print(alien)
print("...")
# Show how many aliens have been created.
print("Total number of aliens: " + str(len(aliens)))


for alien in aliens[0:3]:
 if alien['color'] == 'green':
   alien['color'] = 'yellow'
   alien['speed'] = 'medium'
   alien['points'] = 10
 elif alien['color'] == 'yellow':
   alien['color'] = 'red'
   alien['speed'] = 'fast'
   alien['points'] = 15