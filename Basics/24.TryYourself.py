""" 
4-13. Buffet: A buffet-style restaurant offers only five basic foods. Think of five
simple foods, and store them in a tuple.
• Use a for loop to print each food the restaurant offers.
• Try to modify one of the items, and make sure that Python rejects the
change.
• The restaurant changes its menu, replacing two of the items with different
foods. Add a block of code that rewrites the tuple, and then use a for
loop to print each of the items on the revised menu.
"""

# 4-13. Buffet:

print("4-13. Buffet:\n")

foods = ('rice', 'beans', 'spaguetti', 'File', 'bacon and eggs')

#for loop

for food in foods:
    print(food)

#error
foods[1] = 'fish'

# change the menu
foods = ('rice', 'fish', 'pizza', 'File', 'bacon and eggs')

for food1 in foods:
    print(food1)

