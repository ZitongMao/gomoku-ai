# Gomoku logic design based on xerwin's tutorial
# http://www.cnblogs.com/erwin/p/7828956.html

from enum import Enum
from boardstate import *


class Gomoku(object):

    def __init__(self):

        # create a N * N map

        self.__chessMap = [[BoardState.EMPTY for j in range(N)]
                           for i in range(N)]
        self.__currentI = -1
        self.__currentJ = -1
        self.__currentState = BoardState.EMPTY

    def get_chessMap(self):
        return self.__chessMap

    def get_chessboard_state(self, i, j):
        return self.__chessMap[i][j]

    def set_chessboard_state(
        self,
        i,
        j,
        state,
        ):
        self.__chessMap[i][j] = state
        self.__currentI = i
        self.__currentJ = j
        self.__currentState = state

    def get_chess_result(self):
        if self.connected_five(self.__currentI, self.__currentJ,
                               self.__currentState):
            return self.__currentState
        else:
            return BoardState.EMPTY

    def direction_count(
        self,
        i,
        j,
        xdirection,
        ydirection,
        player,
        ):
        count = 0
        for step in range(1, 5):  # look four more steps on a certain direction
            if xdirection != 0 and (j + xdirection * step < 0 or j
                                    + xdirection * step >= N):
                break
            if ydirection != 0 and (i + ydirection * step < 0 or i
                                    + ydirection * step >= N):
                break
            if self.__chessMap[i + ydirection * step][j + xdirection
                    * step] == player:
                count += 1
            else:
                break
        return count

    def connected_five(
        self,
        i,
        j,
        player,
        ):

        # four directions: horizontal, vertical, two diagonals

        directions = [[(-1, 0), (1, 0)], [(0, -1), (0, 1)], [(-1, 1),
                      (1, -1)], [(-1, -1), (1, 1)]]

        for axis in directions:
            axis_count = 1
            for (xdirection, ydirection) in axis:
                axis_count += self.direction_count(i, j, xdirection,
                        ydirection, player)
                if axis_count >= 5:
                    return True

        return False



            