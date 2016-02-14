#from hungaryCard import HungaryCard, GetCards
#from hungaryCard import hungaryCard
from fatcard.hungaryCard import hungaryCard
#import hungaryCard
from enum import Enum
import os,sys
from PIL import Image
from random import shuffle
import random 
from django.http import HttpResponse
from django.shortcuts import render_to_response


def index(request):
	list_tuple = tuple(hungaryCard.HungaryCard)
	s1 = str(list_tuple[1].value[0])
	s2 = str(list_tuple[1].value[1])
	s3 = s1 + "...." + s2
	return HttpResponse(s3)

def cardpages(request):
	list_tuple = tuple(hungaryCard.HungaryCard)
	return render_to_response("fatcard/base.html", {'list_tupl':list_tuple})
	
 # print(hungaryCard.HungaryCard)
 # g = hungaryCard.GetCards()
 # t = g.get_list_tuple()
 # d = g.get_list_digits()
 # print(t)
 # random.shuffle(d)
 # print(d)
 # list_tuple = tuple(hungaryCard.HungaryCard)
 # print(list_tuple[1].value[0], "....", list_tuple[1].value[1])