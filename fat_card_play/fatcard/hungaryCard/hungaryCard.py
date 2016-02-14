from enum import Enum
import os,sys
from PIL import Image
from random import shuffle
import random

class HungaryCard(Enum):
	LOWERRED=(2, "CardPages/lowerRed.JPG")
	UPPERRED=(3, "CardPages/upperRed.JPG")
	KINGRED=(4, "CardPages/kingRed.JPG")
	SEVENRED=(7, "CardPages/sevenRed.JPG")
	EIGHTRED=(8, "CardPages/eightRed.JPG")
	NINERED=(9, "CardPages/nineRed.JPG")
	TENRED=(10, "CardPages/tenRed.JPG")
	ACERED=(11, "CardPages/aceRed.JPG")
	LOWERGREEN=(2, "CardPages/lowerGreen.JPG")
	UPPERGREEN=(3, "CardPages/upperGreen.JPG")
	KINGGREEN=(4, "CardPages/kingGreen.JPG")
	SEVENGREEN=(7, "CardPages/sevenGreen.JPG")
	EIGHTGREEN=(8, "CardPages/eightGreen.JPG")
	NINEGREEN=(9, "CardPages/nineGreen.JPG")
	TENGREEN=(10, "CardPages/tenGreen.JPG")
	ACEGREEN=(11, "CardPages/aceGreen.JPG")
	LOWERDORK=(2, "CardPages/lowerDork.JPG")
	UPPERDORK=(3, "CardPages/upperDork.JPG")
	KINGDORK=(4, "CardPages/kingDork.JPG")
	SEVENDORK=(7, "CardPages/sevenDork.JPG")
	EIGHTDORK=(8, "CardPages/eightDork.JPG")
	NINEDORK=(9, "CardPages/nineDork.JPG")
	TENDORK=(10, "CardPages/tenDork.JPG")
	ACEDORK=(11, "CardPages/aceDork.JPG")
	LOWERNUT=(2, "CardPages/lowerNut.JPG")
	UPPERNUT=(3, "CardPages/upperNut.JPG")
	KINGNUT=(4, "CardPages/kingNut.JPG")
	SEVENNUT=(7, "CardPages/sevenNut.JPG")
	EIGHTNUT=(8, "CardPages/eightNut.JPG")
	NINENUT=(9, "CardPages/nineNut.JPG")
	TENNUT=(10, "CardPages/tenNut.JPG")
	ACENUT=(11, "CardPages/aceNut.JPG")


class GetCards:

	def get_list_tuple(self):
		list_cards = []
		for card in HungaryCard:
		    list_cards.append(card)
		return tuple(list_cards)

	def get_list_digits(self):
		digits = []
		for index in reversed(range(32)):
			digits.append(index)
		return digits


