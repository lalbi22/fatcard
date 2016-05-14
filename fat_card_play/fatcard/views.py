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
from django.core.context_processors import csrf
from django.views.decorators.csrf import csrf_protect
import json
import datetime
from django.shortcuts import render

card = hungaryCard.GetCards()
list_digit = card.get_list_digits()
list_tuple = card.get_list_tuple()
aplayer = card.aplayer
bplayer = card.bplayer
#assets = hungaryCard.ASSETS

def ajax(request):
    now = datetime.datetime.now()
    html = "<html><body>It is now %s.</body></html>" % now
    return HttpResponse(html)

def index(request):
	list_tuple = tuple(hungaryCard.HungaryCard)
	s1 = str(list_tuple[1].value[0])
	s2 = str(list_tuple[1].value[1])
	s3 = s1 + "....." + s2
	return HttpResponse(s3)

@csrf_protect
def cardpages(request):
 	# list_tuple = tuple(hungaryCard.HungaryCard)
 	# list_digit = []
 	# for index in reversed(range(32)):
 	# 	list_digit.append(index)
 	content = {'l_tuple':list_tuple, 'l_digit':list_digit, 'cardclass':card, 'aplay':aplayer, 'bplay':bplayer}#, 'sets':assets}
 	return render(request, "fatcard/base.html", content)	
 	#return render_to_response("fatcard/base.html", {'l_tuple':list_tuple})

def listdigits(request):
 	# g = hungaryCard.GetCards()
 	# list_digit = g.get_list_digits()
 	# list_tuple = g.get_list_tuple()
 	# list_digit = []
 	# for index in reversed(range(32)):
 	# 	list_digit.append(index) 	
 	content = {'l_tuple':list_tuple, 'l_digit':list_digit, 'cardclass':card}#, 'sets':assets#}
 	return render_to_response("fatcard/base.html", content)	
 	#return render_to_response("fatcard/base.html", {'l_digit':list_digit})
	
 # print(hungaryCard.HungaryCard)
 # g = hungaryCard.GetCards()
 # t = g.get_list_tuple()
 # d = g.get_list_digits()
 # print(t)
 # random.shuffle(d)
 # print(d)
 # list_tuple = tuple(hungaryCard.HungaryCard)
 # print(list_tuple[1].value[0], "....", list_tuple[1].value[1])