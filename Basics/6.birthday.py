

# o python não vai conseguir interpretar pois a var message é uma string, mas a idade está em forma de int 
# para consertar isso podemos usar o metodo str()
age = 24

message = "Happy " + age + "rd Birthday!"

print(message)


# jeito certo 

message =  "Happy " + str(age) + "rd Birthday!"
print(message)