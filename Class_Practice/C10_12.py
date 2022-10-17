#10/12/22
import random
A = ["Barcelona", "Rome", "Grenada", "London", "Paris"]
B = ["Milwaukee","New York", "Los Angles", "Sayner", "Platville"]
C = ["Pot Stickers", "Dumplimngs", "Tacos", "Pizza", "Steak"]
D = ["English", "Spanish", "French", "Chineese", "Lattin"]
E = ["Speed", "22", "PYTHON CRASH COURSE", "Self Care", "Condemned"]
F = ["Pita Pit", "Chen’s Dumpling House", "Amazon", "Good Will", "Free Geek"]
G = ["Meadow", "Viet", "Tony", "Steven", "Nathen"]
H = ['"Howdy Partner"', '"Greedings Good Sir"', '"The Casual Nod"', '"Aloha"', '"hi"']

#list with random value in the index value
print('Once apon a time in the city of', A[random.randint(0, 4)], "the city of fun they call it. Me and", G[random.randint(0, 4)], "go there all the time! Some say that the one in Ameraca is better but", B[random.randint(0, 4)], " will never compare! You know why? Because they make the best ", C[random.randint(0, 4)]," there! The guy at the counter at  ", F[random.randint(0, 4)], " always greets you with a ", H[random.randint(0, 4)], " in ", D[random.randint(0, 4)], " he always knows what I want and serves me", C[random.randint(0, 4)], " nice and hot!", "Make sure to ask him for ", E[random.randint(0, 4)], " he will know what im talking about!")
print("\n---Random---\n")


#initialize a number
num = 0
#loop to change number for index
for Latter in range(0,5):
  print('Once apon a time in the city of', A[num], "the city of fun they call it. Me and", G[num], "go there all the time!Some say that the one in Ameraca is better but", B[num], " will never compare! You know why? Because they make the best ", C[num]," there! The guy at the counter at  ", F[num], " always greets you with a ", H[num], " in ", D[num], " he always knows what I want and serves me", C[num], " nice and hot!", "Make sure to ask him for ", E[num], " he will know what im talking about!")
  num = num + 1
  print("\n--",num,"--\n")