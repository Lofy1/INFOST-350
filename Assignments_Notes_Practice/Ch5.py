#Working with IF Statements
print("------Chapter 5------")
print("This is in CHAPTOR 5 \n")

#cycles through cars and prints the one BMW in all caps
cars = ['audi', 'bmw', 'subaru', 'toyota']
for car in cars:
  if car == 'bmw':
   print(car.upper())
  else:
    print(car.title())

#if not statments
requested_topping = 'mushrooms'
if requested_topping != 'anchovies':
 print("Hold the anchovies!")

answer = 17
if answer != 42:
 print("That is not the correct answer. Please try again!")

#a different if not
banned_users = ['andrew', 'carolina', 'david']
user = 'marie'

if user not in banned_users:
 print(user.title() + ", you can post a response if you wish.")

#If less than
age = 19
if age >= 18:
  print("You are old enough to vote!")
#else statements
else:
 print("Sorry, you are too young to vote.")
 print("Please register to vote as soon as you turn 18!")


#The if-elif-else Chain
age = 12
if age < 4:
 print("Your admission cost is $0.")

elif age < 18:
 print("Your admission cost is $5.")
else:
 print("Your admission cost is $10.")

#Testing Multiple Conditions
age = 12
if age < 4:
 print("Your admission cost is $0.")

elif age < 18:
 print("Your admission cost is $5.")
else:
 print("Your admission cost is $10.")

#putting it in a string
requested_toppings = ['mushrooms', 'green peppers', 'extra cheese']
for requested_topping in requested_toppings:
 print("Adding " + requested_topping + ".")
print("\nFinished making your pizza!")