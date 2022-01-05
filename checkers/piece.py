# Draws the pieces.
import pygame
from .constants import RED, WHITE, SQUARE_SIZE, GREY, CROWN

class Piece:
	PADDING = 15
	OUTLINE = 2

	def __init__(self, row, col, color):
		self.row       = row
		self.col       = col
		self.color     = color
		self.king      = False
		self.x         = 0
		self.y         = 0
		self.calc_pos()

	def calc_pos(self):
		self.x = SQUARE_SIZE * self.col + SQUARE_SIZE // 2 # Right in the middle of the square.
		self.y = SQUARE_SIZE * self.row + SQUARE_SIZE // 2

	def make_king(self):
		self.king = True

	def draw(self, win):
		radius = SQUARE_SIZE // 2 - self.PADDING
		pygame.draw.circle(win, GREY, (self.x, self.y), radius + self.OUTLINE)
		pygame.draw.circle(win, self.color, (self.x, self.y), radius)

		if self.king:
			win.blit(CROWN, (self.x - CROWN.get_width() // 2, self.y - CROWN.get_height() // 2)) # Centers the crown image in the checker piece.

	def move(self, row, col):
		self.row = row
		self.col = col
		self.calc_pos() # X/Y position.

	def __repr__(self): # Internal representation of an object.
		return str(self.color)