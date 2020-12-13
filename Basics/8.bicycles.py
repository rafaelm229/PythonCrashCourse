
# dessa forma você acessara todos os itens da lista 
bicycles = ['trek', 'cannodale', 'redline', 'specialized',]
print(bicycles)

#para acessar idividualmente podemos usar vetores informando a posição no index
#lembrando que em python se conta aprtir de 0.
print(bicycles[2])


#tambem podemos usar os metodos de strings como o title() para formatar o texto.

print(bicycles[2].title())

message = "My first bicycle was a " + bicycles[2].title() + "."

print(message)