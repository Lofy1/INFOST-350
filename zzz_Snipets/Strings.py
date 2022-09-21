'''
f String
More information at
https://realpython.com/python-f-strings/
'''
hello = "Hello World!"
Name = "Nicholas Lofy"
Major = "IST"
Hobbie = "Water sking "+"Test"
Fav = "My favorite movie is Speed"
Question = "My Question is, are personal code projects more important to a recruiter than like an internship"


#option 1
print("Option 1")


paragraph = (hello+" "+Name +" "+Major+" "+Hobbie+" "+Fav+" "+Question)

print(paragraph)



print("\n---------------\n")



#Option 2
print("Option 2")

#the f before varables is to "format" string
paragraph2 = f"{hello} {Name} {Major} {Hobbie} {Fav} {Question}"

print(paragraph2)