cars = ['bmw', 'audi', 'toyota', 'subaru']

# ordenar alfabeticamente
cars.sort()
print(cars)

# para ordenar inversamente alfabeticamente
cars.sort(reverse = True)
print(cars)

#para ordenar temporariamente pode usar o metodo sort dentro do metodo print
print("\n")
print("the Original List ")
print(cars)

print("\n")
print("the sorted List ")
print(sorted(cars))


print("\n")
print("the Original List again ")
print(cars)

#ordenar inversamente a sua lista ( nao alfabetica )
print("\n reverse sorted")
cars.reverse()
print(cars)

# comprimento da lista 
print("O comprimeto da lista  é de " + str(len(cars)) + " Carros")
len(cars)