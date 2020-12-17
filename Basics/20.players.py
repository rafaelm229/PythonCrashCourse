
players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[0:3])

#para fazer um subset de uma lista nesse exemplo: martina, michael, florence, eli
print(players[1:4])

#para omitir items da lista
print(players[:4])

#loop com slices

print("\nHere are the first three players on my team:")
for player in players[:3]:
    print(player.title())

