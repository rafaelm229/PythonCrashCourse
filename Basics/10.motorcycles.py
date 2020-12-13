

motorcycles = ['honda', 'yamaha', 'suzuki']

print(motorcycles)


motorcycles[0] = 'ducati'
print(motorcycles)


# para adicionar items em uma lista basta usar o metodo append()

motorcycles.append('ducati')

print(motorcycles)



#para remover bastar usar o metodo "del"

motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

del motorcycles[0]
print(motorcycles)

# podemos usar o metodo pop() para remover tambem

motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

popped_motorcycle = motorcycles.pop()

print(motorcycles)
print(popped_motorcycle)