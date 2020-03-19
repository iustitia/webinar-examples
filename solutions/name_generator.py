from random import randint, choice

######

first_names = ['Anna', 'Maria', 'Katarzyna', 'Małgorzata', 'Agnieszka', 'Krystyna', 'Barbara', 'Ewa',
               'Jan', 'Andrzej', 'Piotr', 'Krzysztof', 'Tomasz', 'Paweł', 'Józef', 'Marcin', 'Marek']
cities = ['Warszawy', 'Krakowa', 'Kielc', 'Poznania', 'Gdańska', 'Wrocławia', 'Płocka', 'Katowic', 'Leszna']

# Jan z Gdańska wygrywa właśnie nagrodę 1000 zł!
title = '{} z {} wygrywa właśnie nagrodę {} zł!'



######

name = choice(first_names)
city = choice(cities)
prize = randint(1, 10) * 1000

print(title.format(name, city, prize))
