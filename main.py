# pip install pygame
# NOTE 1/5/2022: Cannot move white for some reason.
import pygame
from checkers.constants import WHITE, WIDTH, HEIGHT, SQUARE_SIZE
from checkers.game import Game
from minimax.algorithm import minimax

FPS = 60 # Specific to rendering this game. Not constants.

# Pygame display.
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Checkers')

def get_row_col_from_mouse(pos):
	x, y = pos
	row  = y // SQUARE_SIZE
	col  = x // SQUARE_SIZE
	return row, col

# Runs the game.
def main():
	run   = True
	clock = pygame.time.Clock()
	game = Game(WIN)

	while run:
		clock.tick(FPS)

		if game.turn == WHITE:
			value, new_board = minimax(game.get_board(), 3, WHITE, game) # 4 is the depth: How many boards the AI considers before moving.
			game.ai_move(new_board) # The AI has moved, update the new board.
		
		if game.winner() != None:
			print(game.winner())
			run = False

		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				run = False

			if event.type == pygame.MOUSEBUTTONDOWN:
				pos      = pygame.mouse.get_pos()
				row, col = get_row_col_from_mouse(pos)
				game.select(row, col)

		game.update()

	pygame.quit()

main()