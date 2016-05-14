from enum import Enum
import os,sys
from PIL import Image
from random import shuffle
import random

ASSETS = "assets/"
class HungaryCard(Enum):
	LOWERRED=(2, ASSETS+"CardPages/lowerRed.JPG", 0)
	UPPERRED=(3, ASSETS+"CardPages/upperRed.JPG", 1)
	KINGRED=(4, ASSETS+"CardPages/kingRed.JPG", 2)
	SEVENRED=(7, ASSETS+"CardPages/sevenRed.JPG", 3)
	EIGHTRED=(8, ASSETS+"CardPages/eightRed.JPG", 4)
	NINERED=(9, ASSETS+"CardPages/nineRed.JPG", 5)
	TENRED=(10, ASSETS+"CardPages/tenRed.JPG", 6)
	ACERED=(11, ASSETS+"CardPages/aceRed.JPG", 7)
	LOWERGREEN=(2, ASSETS+"CardPages/lowerGreen.JPG", 8)
	UPPERGREEN=(3, ASSETS+"CardPages/upperGreen.JPG", 9)
	KINGGREEN=(4, ASSETS+"CardPages/kingGreen.JPG", 10)
	SEVENGREEN=(7, ASSETS+"CardPages/sevenGreen.JPG", 11)
	EIGHTGREEN=(8, ASSETS+"CardPages/eightGreen.JPG", 12)
	NINEGREEN=(9, ASSETS+"CardPages/nineGreen.JPG", 13)
	TENGREEN=(10, ASSETS+"CardPages/tenGreen.JPG", 14)
	ACEGREEN=(11, ASSETS+"CardPages/aceGreen.JPG", 15)
	LOWERDORK=(2, ASSETS+"CardPages/lowerDork.JPG", 16)
	UPPERDORK=(3, ASSETS+"CardPages/upperDork.JPG", 17)
	KINGDORK=(4, ASSETS+"CardPages/kingDork.JPG", 18)
	SEVENDORK=(7, ASSETS+"CardPages/sevenDork.JPG", 19)
	EIGHTDORK=(8, ASSETS+"CardPages/eightDork.JPG", 20)
	NINEDORK=(9, ASSETS+"CardPages/nineDork.JPG", 21)
	TENDORK=(10, ASSETS+"CardPages/tenDork.JPG", 22)
	ACEDORK=(11, ASSETS+"CardPages/aceDork.JPG", 23)
	LOWERNUT=(2, ASSETS+"CardPages/lowerNut.JPG", 24)
	UPPERNUT=(3, ASSETS+"CardPages/upperNut.JPG", 25)
	KINGNUT=(4, ASSETS+"CardPages/kingNut.JPG", 26)
	SEVENNUT=(7, ASSETS+"CardPages/sevenNut.JPG", 27)
	EIGHTNUT=(8, ASSETS+"CardPages/eightNut.JPG", 28)
	NINENUT=(9, ASSETS+"CardPages/nineNut.JPG", 29)
	TENNUT=(10, ASSETS+"CardPages/tenNut.JPG", 30)
	ACENUT=(11, ASSETS+"CardPages/aceNut.JPG", 31)


class GetCards:

	def __init__(self, list_cards=[], digits=[], aplayer=[], bplayer=[]):
		self.list_cards = list_cards
		self.digits = digits
		self.aplayer = aplayer
		self.bplayer = bplayer

	def get_list_tuple(self):
		#self.list_cards = []
		for card in HungaryCard:
			self.list_cards.append(card)
		return tuple(self.list_cards)

	def get_list_digits(self):
		#self.digits = []
		for index in reversed(range(32)):
			self.digits.append(index)
		random.shuffle(self.digits)
		return self.digits

	def page_devide(self, count=1):
		try:
			for index in range(count):
				del self.digits[len(self.digits)-1]
		except IndexError:
			print("no card")

	def page_devide2(self, count=2):
		try:
			for index in range(count):
				if len(self.aplayer) == len(self.bplayer):
					self.aplayer.append(self.digits[len(self.digits)-1])
				else:
					if len(self.aplayer) > len(self.bplayer):
						self.bplayer.append(self.digits[len(self.digits)-1])
					elif len(self.aplayer) < len(self.bplayer):
						self.aplayer.append(self.digits[len(self.digits)-1])
				del self.digits[len(self.digits)-1]
		except IndexError:
			print("no card")


	# def get_list_tuple(self):
	#   list_cards = []
	#   for card in HungaryCard:
	#       list_cards.append(card)
	#   return tuple(list_cards)

	# def get_list_digits(self):
	#   digits = []
	#   for index in reversed(range(32)):
	#       digits.append(index)
	#   return digits


