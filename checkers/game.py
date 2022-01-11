# Handles who's turn it is, if a piece is selected, etc.
import pygame
from .constants import BLUE, RED, SQUARE_SIZE, WHITE
from .board import Board

class Game:
	def __init__(self, win):
		self._init()
		self.win = win

	def winner(self):
		return self.board.winner()

	def update(self):
		self.board.draw(self.win)
		self.draw_valid_moves(self.valid_moves)
		pygame.display.update()

	def _init(self): # _ = Makes def private.
		self.selected    = None
		self.board       = Board()
		self.turn        = RED
		self.valid_moves = {}

	def reset(self):
		self._init()

	def select(self, row, col):
		if self.selected:
			result = self._move(row, col)

			if not result:
				self.selected = None
				self.select(row, col)

		piece = self.board.get_piece(row, col)

		if piece != 0 and piece.color == self.turn:
			self.selected    = piece
			self.valid_moves = self.board.get_valid_moves(piece)
			return True
			
		return False

	def _move(self, row, col): # Moves the pieces around.
		piece = self.board.get_piece(row, col)

		if self.selected and piece == 0 and (row, col) in self.valid_moves:
			self.board.move(self.selected, row, col)
			skipped = self.valid_moves[(row, col)]

			if skipped:
				self.board.remove(skipped)

			self.change_turn()
		else:
			return False

		return True

	def draw_valid_moves(self, moves):
		for move in moves:
			row, col = move
			pygame.draw.circle(self.win, BLUE, (col * SQUARE_SIZE + SQUARE_SIZE // 2, row * SQUARE_SIZE + SQUARE_SIZE // 2), 15)

	def change_turn(self): # Changes turns when the piece is moved.
		self.valid_moves = {}

		if self.turn == RED:
			self.turn = WHITE
			print("White's Turn")
		else:
			self.turn = RED
			print("Red's Turn")

	def get_board(self):
		return self.board

	def ai_move(self, board):
		self.board = board
		self.change_turn()