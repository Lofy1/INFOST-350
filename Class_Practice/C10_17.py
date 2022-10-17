# Python program showing
# a use of input()

inputs = []
  
val = input("Enter your value: ")
print(val)
inputs.append(val)

val = input("Enter your value: ")
print(val)
inputs.append(val)

print(inputs)

nums = []
for i in range(3):
    nums.append([])
    for j in range(1, 4):
        nums[i].append(j)
print("3X3 grid with numbers:")
print("",nums[0],"\n",nums[1],"\n",nums[2])