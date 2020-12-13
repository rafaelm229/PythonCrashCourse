# Raiz quadrada :)

squares = []

for value in range(1,11):
    square = value **2
    squares.append(square)

print(squares)


## segundo exemplo em listas e possivel utilizar estatistica ex.

digits = [1,2,3,4,5,6,7,8,9,0]

# para obter o menor valor
print(min(digits))

# para obter a maior numero
print(max(digits))

# a soma de todos os valores
print(sum(digits))

# exemplo de raiz quadrada mais 2º versao
squares = [value**2 for value in range(1,11)]
print(squares)

