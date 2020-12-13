"""
4-3. Counting to Twenty: Use a for loop to print the numbers from 1 to 20,
inclusive.

4-4. One Million: Make a list of the numbers from one to one million, and then
use a for loop to print the numbers. (If the output is taking too long, stop it by
pressing ctrl -C or by closing the output window.)

4-5. Summing a Million: Make a list of the numbers from one to one million,
and then use min() and max() to make sure your list actually starts at one and
ends at one million. Also, use the sum() function to see how quickly Python can
add a million numbers.

4-6. Odd Numbers: Use the third argument of the range() function to make a list
of the odd numbers from 1 to 20. Use a for loop to print each number.

4-7. Threes: Make a list of the multiples of 3 from 3 to 30. Use a for loop to
print the numbers in your list.

4-8. Cubes: A number raised to the third power is called a cube. For example,
the cube of 2 is written as 2**3 in Python. Make a list of the first 10 cubes (that
is, the cube of each integer from 1 through 10), and use a for loop to print out
the value of each cube.

4-9. Cube Comprehension: Use a list comprehension to generate a list of the
first 10 cubes.
"""

# 4-3. Counting to Twenty:
print("\n4-3. Counting to Twenty:")

for value in range(1,20):
    print(value)


# 4-4. One Million:
print("\n 4-4. One Million:")

for million in list(range(1, 1000001)):
    print(million)

# 4-5. Summing a Million:


# 4-6. Odd Numbers:
print("\n 4-6. Odd Numbers:")

for odd in list(range(1,20,3)):
    print(odd)

# 4-7. Threes:
print("\n 4-7. Threes:")

for i in list(range(3,30,3)):
    print(1)


# 4-8. Cubes:
print("\n 4-8. Cubes:" )

cubes = []

for value in range(1,11):
    cube = value **3
    cubes.append(cube)

print(cubes)



# 4-9. Cube Comprehension:
print("\n 4-9. Cube Comprehension:")

cubos = [ value **3 for i in range(1,11)]
