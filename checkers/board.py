# Represents the checker board.
import pygame
from .constants import BLACK, ROWS, RED, SQUARE_SIZE, COLS, WHITE # Relatively importing, from something in the same directory.
from .piece import Piece

class Board:
	def __init__(self):
		self.board          = [[]] # Two dimensional list.
		self.selected_piece = None
		self.red_left       = self.white_left = 12 # Both sides have 12 pieces.
		self.red_kings      = self.white_kings = 0
		self.create_board()

	def draw_squares(self, win):
		win.fill(BLACK)

		for row in range(ROWS):
			for col in range(row % 2, COLS, 2):
				pygame.draw.rect(win, RED, (row * SQUARE_SIZE, col * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE)) # () Draws the board from the top left.

	def move(self, piece, row, col):
		self.board[piece.row][piece.col], self.board[row][col] = self.board[row][col], self.board[piece.row][piece.col] # Swaps positions in the list.
		piece.move(row, col)

		if row == ROWS or row == 0: # Makes the correct checker piece a king.
			piece.make_king()

			if piece.color == WHITE:
				self.white_kings += 1
			else:
				self.red_kings += 1

	def get_piece(self, row, col):
		return self.board[row][col]

	def create_board(self):
		for row in range(ROWS):
			self.board.append([])

			for col in range(COLS):
				if col % 2 == ((row + 1) % 2): # If it's divisible by 2.
					if row < 3:
						self.board[row].append(Piece(row, col, WHITE))
					elif row > 4:
						self.board[row].append(Piece(row, col, RED))
					else:
						self.board[row].append(0) # Blank piece.
				else:
					self.board[row].append(0)

	def draw(self, win):
		self.draw_squares(win)

		for row in range(ROWS):
			for col in range(COLS):
				piece = self.board[row][col]
				if piece != 0:
					piece.draw(win)