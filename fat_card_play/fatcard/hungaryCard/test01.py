from hungaryCard import HungaryCard, GetCards
import os,sys
from PIL import Image
from random import shuffle
import random

for card in reversed(HungaryCard):	
	print(card)

x = [[i] for i in range(10)]
shuffle(x)
print(x)

#shuffle(HungaryCard)
#print(HungaryCard.value)

list1=[]

for card in HungaryCard:
	list1.append(card)

random.shuffle(list1)
print(list1)

list_tuple = tuple(HungaryCard)

print(type(list_tuple), list_tuple[31].name)

list2 = []

for index in reversed(range(32)):
	list2.append(index)

print(list2)

list3 = list(list2)
list.sort(list3)
print(list3)

print(list_tuple[1].value[0], "....", list_tuple[1].value[1])

print(HungaryCard.ACENUT.value[0])
j=Image.open(HungaryCard.ACENUT.value[1])
j.show()
c=open("test.txt")
for line in c:
	print(line.strip())
c.close()
j.close()

g = GetCards()
t = g.get_list_tuple()
d = g.get_list_digits()
print(t)
random.shuffle(d)
print(d)