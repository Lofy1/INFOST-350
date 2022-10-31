#User In put an d wh i le L o ops
#input function
message = input("Tell me something, and I will repeat it back to you: ")
print(message)

#take input variable and put it in a print statment 
name = input("Please enter your name: ")
print("Hello, " + name + "!")

#Adding to input varible (+=) this is cool
prompt = "If you tell us who you are, we can personalize the messages you see."
prompt += "\nWhat is your first name? "
name = input(prompt)

#age
age = input("How old are you? ")
print("You are, " + age + "!")

#input conditions
height = input("How tall are you, in inches? ")
height = int(height)
if height >= 36:
 print("\nYou're tall enough to ride!")
else:
 print("\nYou'll be able to ride when you're a little older.")

#odd or even
number = input("Enter a number, and I'll tell you if it's even or odd: ")
number = int(number)
if number % 2 == 0:
 print("\nThe number " + str(number) + " is even.")
else:
 print("\nThe number " + str(number) + " is odd.")

#while look count to 5
current_number = 1
while current_number <= 5:
 print(current_number)
 current_number += 1


#let user quit the loop
# prompt = "\nTell me something, and I will repeat it back to you:"
# prompt += "\nEnter 'quit' to end the program. "
# message = ""
# while message != 'quit':
#   message = input(prompt)
#   print(message)
  
#user decides
active = True
while active: 
  message = input(prompt)
  if message == 'quit':
    active = False
  else:
    print(message)

prompt = "\nPlease enter the name of a city you have visited:"
prompt += "\n(Enter 'quit' when you are finished.) "
while True:
 city = input(prompt)

 if city == 'quit':
   break
 else:
   print("I'd love to go to " + city.title() + "!")


'''
Moving Items from One List to Another
'''
# Start with users that need to be verified,
# and an empty list to hold confirmed users.
unconfirmed_users = ['alice', 'brian', 'candace']
confirmed_users = []
# Verify each user until there are no more unconfirmed users.
# Move each verified user into the list of confirmed users.
while unconfirmed_users:
  current_user = unconfirmed_users.pop()

  print("Verifying user: " + current_user.title())
  confirmed_users.append(current_user)

# Display all confirmed users.
print("\nThe following users have been confirmed:")
for confirmed_user in confirmed_users:
  print(confirmed_user.title())


#Removing All Instances of Specific Values from a List
pets = ['dog', 'cat', 'dog', 'goldfish', 'cat', 'rabbit', 'cat']
print(pets)
while 'cat' in pets:
 pets.remove('cat')

print(pets)

#Filling a Dictionary with User Input
responses = {}
# Set a flag to indicate that polling is active.
polling_active = True
while polling_active:
 # Prompt for the person's name and response.
  name = input("\nWhat is your name? ")
  response = input("Which mountain would you like to climb someday? ")

 # Store the response in the dictionary:
  responses[name] = response

 # Find out if anyone else is going to take the poll.
  repeat = input("Would you like to let another person respond? (yes/ no) ")
  if repeat == 'no':
    polling_active = False

# Polling is complete. Show the results.
print("\n--- Poll Results ---")
for name, response in responses.items():
 print(name + " would like to climb " + response + ".")