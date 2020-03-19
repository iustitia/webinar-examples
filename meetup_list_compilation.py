

#######
"""
Na dwóch listach z plików 'meetup_list.csv' i 'meetup_list2.csv' występują powtórki.
Potrzebujemy mieć jedną, spójną listę, posortowaną alfabetycznie dla sprawnego przeprowadzenia rejestracji.
Zaczytaj dane, wyrzuć powtórki, skompiluj w jedną listę i wypisz.
"""

#######

facebook_list = 'data/meetup_list.csv'
meetup_list = 'data/meetup_list2.csv'

s = set()

with open(facebook_list, 'r') as f:
    for line in f.readlines():
        name = line.strip()
        s.add(name)


with open(meetup_list, 'r') as f:
    for line in f.readlines():
        l = line.split('\t')
        s.add(l[0])

print(sorted(s))
