list_players = ["Маша", "Петя", "Саша", "Оля", "Кирилл", "Коля"] #исходный список


middle_index = len(list_players) // 2 # индекс середины

first_team = list_players[:middle_index] #первая команда - первая половина
second_team = list_players[middle_index:] #вторая команда - вторая половина

print(first_team)
print(second_team)
