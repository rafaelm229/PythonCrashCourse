
# nessa lista o metodo range utiliza os dois primeiros paramentros para 
# delimitar o limite do valores e o terceiro parametro se utiliza para definir
# o valor que irar pular exemplo abaixo range de 2 a 20 e pulando de 10 em 10 
# ate atingir o valor limite que sera 20 nesse caso

# aqui se obtem uma lista [2,12] pares
evenNumbers = list(range(2,20,10))
print(evenNumbers)

# aqui se obtem um sequencia de numeros impares
for odd in list(range(1,20,3)):
    print(odd)
