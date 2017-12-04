from enum import Enum

#define a board with size N * N
N = 15

class BoardState(Enum):
	#three possible states for a given intersection
    EMPTY = 0
    BLACK = 1
    WHITE = 2