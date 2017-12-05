class Node(object):
	def __init__(self, gomoku, depth, boardState):
		self.__gomoku = gomoku
		self.__currentState = boardState
		self.__depth = depth
		self.__currentI = -1
		self.__currentJ = -1

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
        	





