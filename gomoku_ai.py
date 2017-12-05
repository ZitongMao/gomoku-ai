import random
from boardstate import *


class gomokuAI(object):
	def __init__(self, gomoku, currentState, depth):
		self.__gomoku = gomoku
		self.__currentState = currentState
		self.__depth = depth
		self.__currentI = -1
		self.__currentJ = -1

	def one_step(self):
		i = random.randrange(0,15,1)
		j = random.randrange(0,15,1)

		if not i is None and not j is None:
			if self.__gomoku.get_chessboard_state(i, j) != BoardState.EMPTY:
				self.one_step()
			else:
				self.__gomoku.set_chessboard_state(i, j, self.__currentState)
				return True
		return False

    def evaluate(self):
        vectors = []

        for i in xrange(N):
            vectors.append(self.__gomoku.get_chessMap()[i])
            
        for j in xrange(N):
            vectors.append([self.__gomoku.get_chessMap()[i][j] for i in range(N)])

        vectors.append([self.__gomoku.get_chessMap()[x][x] for x in range(N)])
        for i in xrange(1, N-4):
            v = [self.__gomoku.get_chessMap()[x][x-i] for x in range(i, N)]
            vectors.append(v)
            v = [self.__gomoku.get_chessMap()[y-i][y] for y in range(i, N)]
            vectors.append(v)

        vectors.append([self.__gomoku.get_chessMap()[x][N-x-1] for x in range(N)])
        for i in xrange(4, N-1):
            v = [self.__gomoku.get_chessMap()[x][i-x] for x in xrange(i, -1, -1)]
            vectors.append(v)
            v = [self.__gomoku.get_chessMap()[x][N-x+N-i-2] for x in xrange(N-i-1, N)]
            vectors.append(v)

        board_score = 0

        for v in vectors:
        	score = evaluate_vector(v)
        	if self.__currentState == BoardState.WHITE:
        		board_score += score['white'] - score['black']
        	else:
        		board_score += score['black'] - score['white']

        return board_score
