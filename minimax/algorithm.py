from copy import deepcopy # Makes a copy of the board multiple times.
import pygame

RED = (255, 0, 0)
WHITE = (255, 255, 255)

def minimax(position, depth, max_player, game):
	if depth == 0 or position.winner() != None:
		return position.evaluate(), position # Evaluation goes with position.

	if max_player:
		maxEval   = float('-inf') # Scores
		best_move = None
		for move in get_all_moves(position, WHITE, game): # Evaluates every move possible to make.
			evaluation = minimax(move, depth - 1, False, game)[0]
			maxEval = max(maxEval, evaluation)

			if maxEval == evaluation: # If the best move is the one currently looked at.
				best_move = move

		return maxEval, best_move
	else:
		minEval   = float('inf') # Scores
		best_move = None
		for move in get_all_moves(position, RED, game): # Evaluates every move possible to make.
			evaluation = minimax(move, depth - 1, True, game)[0]
			minEval = min(minEval, evaluation)

			if minEval == evaluation: # If the best move is the one currently looked at.
				best_move = move

		return minEval, best_move

def simulate_move(piece, move, board, game, skip):
	board.move(piece, move[0], move[1])
	if skip:
		board.remove(skip) # Skipped over a piece.

	return board

def get_all_moves(board, color, game):
	moves = []

	for piece in board.get_all_pieces(color):
		valid_moves = board.get_valid_moves(piece)
		for move, skip in valid_moves.items():
			draw_moves(game, board, piece) # Shows visually what the AI is considering. Comment out to remove.
			temp_board = deepcopy(board)
			temp_piece = temp_board.get_piece(piece.row, piece.col)
			new_board  = simulate_move(temp_piece, move, temp_board, game, skip) # Take the piece, move want to make, make the move, and return the new board.
			moves.append(new_board)

	return moves

def draw_moves(game, board, piece):
	valid_moves = board.get_valid_moves(piece)
	board.draw(game.win)
	pygame.draw.circle(game.win, (0, 255, 0), (piece.x, piece.y), 50, 5) # Highlights the piece with a green rim.
	game.draw_valid_moves(valid_moves.keys())
	pygame.display.update()
	# pygame.time.delay(100) # Delays for 100ms.