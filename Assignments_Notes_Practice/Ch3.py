
#Lists
print("------Chapter 3------")
print("This is in CHAPTOR 3 \n")

#This is a list of specifcally bicycles 
bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles)

#When counting items in a list it starts a 0, 1, 2, ect
#To print the first item on the list print item 0
print(bicycles[0])

print(bicycles[0].title())

# To find the last thing in the list do -1 to go in reverse oder of the list
print(bicycles[-1])

#You can print things in a list in a sentance
message = "My first bicycle was a " + bicycles[0].title() + "."
print(message)


#Change item in list
#To change the first item in postion 0
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)
motorcycles[0] = 'ducati'
print(motorcycles)

#Add item to the list
#Use (list name).append('item')
motorcycles.append('honda')
print(motorcycles)

#Inserting into a postion in the list .insert('postion', 'item')
motorcycles.insert(0, 'Harly')
print(motorcycles)

#Removing Elements from a List del list_name[postion]
del motorcycles[0]
print(motorcycles)

#The pop() method removes the last item in a list, but it lets you work with that item after removing it.
popped_motorcycle = motorcycles.pop()
print(motorcycles)
print(popped_motorcycle)
print("The last motorcycle I removed from the list was " + popped_motorcycle.title() + ".")

#Use pop() to remove an item in a list at any position
first_owned = motorcycles.pop(0)
print('The first motorcycle I owned was a ' + first_owned.title() + '.')

#Removing an Item by Value or Name
motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
print(motorcycles)
motorcycles.remove('ducati')
print(motorcycles)


#Organizing a List
#Sorting a List Permanently with the sort() Method
cars = ['bmw', 'audi', 'toyota', 'subaru']
print(cars)

#sort alphabetically
cars.sort()
print(cars)

#Sort list in reverse alphabetical order
cars.sort(reverse=True)
print(cars)

#Printing a List in Reverse Order as orginally inputed
cars.reverse()
print(cars)

#Finding the Length of a List
print(len(cars))

#Video maybe

primes = [2, 3, 5, 7, 11, 13, 17, 19]
print(primes)
#Slicing a list
#only show values in postion 2 thu 5
#The beguining value is inclueded the final is not!!!
print(primes[2:5])

#lists can contain lists
List_1 = [2, 3, 5, [1, 4, 6]]
print(List_1)

#lists can contain any varible at the same time
List_2 = [2, 3, [1, 4, 6], True, "jo mam", 1.789]
print(List_2)

#combine lists
numbers = [1, 2, 3]
letters = ["a", "b", "c"]
print(numbers + letters)


Lists = [primes, List_1]
print(Lists)