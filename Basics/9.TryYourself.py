"""
Try these short programs to get some firsthand experience with Python’s lists.
You might want to create a new folder for each chapter’s exercises to keep
them organized.

3-1. Names: Store the names of a few of your friends in a list called names . Print
each person’s name by accessing each element in the list, one at a time.

3-2. Greetings: Start with the list you used in Exercise 3-1, but instead of just
printing each person’s name, print a message to them. The text of each mes-
sage should be the same, but each message should be personalized with the
person’s name.

3-3. Your Own List: Think of your favorite mode of transportation, such as a
motorcycle or a car, and make a list that stores several examples. Use your list
to print a series of statements about these items, such as “I would like to own a
Honda motorcycle.”
"""

friends = [ 'jango', 'ray', 'bobba-feet', 'luke']

print(friends[2].title())


# 2º 

Greetings = "May the Force be with You"

print(Greetings + friends[0].title() + "!" )
print(Greetings + friends[1].title() + "!" )
print(Greetings + friends[2].title() + "!" )
print(Greetings + friends[3].title() + "!" )


favorites = ['Civic', 'Camaro', '911', 'f430', 'model 3', 'Raptor', 'model X', 'Rodster']
brands = ['Honda', 'Chevrolet', 'Porsche', 'Ferrari','Tesla', 'Ford']
print("If i have money a buy a " + brands[0].title() + " " + favorites[0].title())
print("If i have money a buy a " + brands[1].title() + " " + favorites[1].title())
print("If i have a good money a buy a " + brands[2].title() + " " + favorites[2].title())
print("If i have money and a job i buy a " + brands[3].title() + " " + favorites[3].title())

#....
