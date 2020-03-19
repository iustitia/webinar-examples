

#######
"""
Na dwóch listach z plików 'meetup_list.csv' i 'meetup_list2.csv' występują powtórki.
Potrzebujemy mieć jedną, spójną listę, posortowaną alfabetycznie dla sprawnego przeprowadzenia rejestracji.
Zaczytaj dane, wyrzuć powtórki, skompiluj w jedną listę i wypisz.
"""

#######

facebook_list = '../data/meetup_list.csv'
meetup_list = '../data/meetup_list2.csv'

final_list = set()
with open(facebook_list, 'r') as f:
    for line in f.readlines():
        name = line.replace('\n', '')
        final_list.add(name)

print(final_list)
print(len(final_list))

with open(meetup_list, 'r') as f:
    for line in f.readlines():
        print(line)
        t = line.split('\t')
        name = t[0]

        final_list.add(name)

print(sorted(final_list))
