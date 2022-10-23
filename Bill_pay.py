import random

names_string = input("Give me everybody's names, separated by a comma: ")
names = names_string.split(", ")

num = len(names)
num1= num-1

random1 = random.randint(0,num1)
treat= str(names[random1])

print("Today's bill will be given by:" + treat)
