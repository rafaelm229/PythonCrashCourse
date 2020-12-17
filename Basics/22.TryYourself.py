"""
4-10. Slices: Using one of the programs you wrote in this chapter, add several
lines to the end of the program that do the following:
• Print the message, The first three items in the list are:. Then use a slice to
print the first three items from that program’s list.
• Print the message, Three items from the middle of the list are:. Use a slice
to print three items from the middle of the list.
• Print the message, The last three items in the list are:. Use a slice to print
the last three items in the list.

4-11. My Pizzas, Your Pizzas: Start with your program from Exercise 4-1
(page 60). Make a copy of the list of pizzas, and call it friend_pizzas .
Then, do the following:
• Add a new pizza to the original list.
• Add a different pizza to the list friend_pizzas .
• Prove that you have two separate lists. Print the message, My favorite
pizzas are:, and then use a for loop to print the first list. Print the message,
My friend’s favorite pizzas are:, and then use a for loop to print the sec-
ond list. Make sure each new pizza is stored in the appropriate list.

4-12. More Loops: All versions of foods.py in this section have avoided using
for loops when printing to save space. Choose a version of foods.py, and
write two for loops to print each list of foods.

"""

# 4-10. Slices:
print("4-10. Slices: \n")

list = ['cake', 'pudin', 'mapple', 'apple', 'chocolate bar']

# first 3 items
print(list[:2])

# 3 in the middle
print(list[1:3])

# last 3    
print(list[2:])



# 4-11. My Pizzas
print("\n 4-11. My Pizzas")


myPizzas = ['Peperone', 'Calabresa', 'Frango',]
friendsPizzas = myPizzas[:]

myPizzas.append("Chiken")
friendsPizzas.append("chocolate")

print("\n My favorite pizzas are:")
for my in myPizzas[:]:
    print(my)



print("\nMy friend’s favorite pizzas are:")

for friend in friendsPizzas[:]:
    print(friend)


# 4-12. More Loops
print("4-12. More Loops:\n")

myFoods = ['Pizza', 'Chocolate Bar', 'Carrot Cake']

myFriendFoods = myFoods[:]

for myfood in myFoods[:]:
    print(myfood)

for friendFood in myFriendFoods[:]:
    print(friendFood)
