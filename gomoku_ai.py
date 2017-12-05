#!/usr/bin/python
# -*- coding: utf-8 -*-

import random
from boardstate import *
from copy import deepcopy
from evaluate import *
from gomoku import Gomoku
import math


class gomokuAI(object):

    def __init__(
        self,
        gomoku,
        currentState,
        depth,
        ):

        self.__gomoku = gomoku
        self.__currentState = currentState
        self.__depth = depth
        self.__currentI = -1
        self.__currentJ = -1

    def set_board(
        self,
        i,
        j,
        state,
        ):

        self.__gomoku.set_chessboard_state(i, j, state)


    def has_neighbor(self, state, i, j):
        directions = [[(-1, 0), (1, 0)], \
              [(0, -1), (0, 1)], \
              [(-1, 1), (1, -1)], \
              [(-1, -1), (1, 1)]]
        for axis in directions:
            for (xdirection, ydirection) in axis:

                if self.__gomoku.get_chessMap()[i+xdirection][j+ydirection] != BoardState.EMPTY:
                	return True
                elif self.__gomoku.get_chessMap()[i+xdirection*2][j+ydirection*2] != BoardState.EMPTY:
                	return True

		return False


    def generate(self):
        for i in xrange(N):
            for j in xrange(N):
                if self.__gomoku.get_chessMap()[i][j] \
                    != BoardState.EMPTY:
                    continue  # only search for available spots
                if not self.has_neighbor(self.__gomoku.get_chessMap()[i][j], i, j):
                	continue
                if self.__currentState == BoardState.WHITE:
                    nextState = BoardState.BLACK
                else:
                    nextState = BoardState.WHITE
                nextPlay = gomokuAI(deepcopy(self.__gomoku), nextState,
                                    self.__depth - 1)
                nextPlay.set_board(i, j, self.__currentState)

                yield (nextPlay, i, j)
    def negate(self):
        return -self.evaluate()
    def evaluate(self):
        vectors = []

        for i in xrange(N):
            vectors.append(self.__gomoku.get_chessMap()[i])

        for j in xrange(N):
            vectors.append([self.__gomoku.get_chessMap()[i][j] for i in
                           range(N)])

        vectors.append([self.__gomoku.get_chessMap()[x][x] for x in
                       range(N)])
        for i in xrange(1, N - 4):
            v = [self.__gomoku.get_chessMap()[x][x - i] for x in
                 range(i, N)]
            vectors.append(v)
            v = [self.__gomoku.get_chessMap()[y - i][y] for y in
                 range(i, N)]
            vectors.append(v)

        vectors.append([self.__gomoku.get_chessMap()[x][N - x - 1]
                       for x in range(N)])
        for i in xrange(4, N - 1):
            v = [self.__gomoku.get_chessMap()[x][i - x] for x in
                 xrange(i, -1, -1)]
            vectors.append(v)
            v = [self.__gomoku.get_chessMap()[x][N - x + N - i - 2]
                 for x in xrange(N - i - 1, N)]
            vectors.append(v)

        board_score = 0

        for v in vectors:
            score = evaluate_vector(v)
            if self.__currentState == BoardState.WHITE:
                board_score += score['black'] - score['white']
            else:
                board_score += score['white'] - score['black']
        print board_score
        return board_score

    def alpha_beta_prune(
        self,
        ai,
        alpha=-10000000,
        beta=10000000,
        ):
        if ai.__depth <= 0:
        	score = ai.negate()
        	return score
        for (nextPlay, i, j) in ai.generate():
            temp_score = -self.alpha_beta_prune(nextPlay, -beta, -alpha)
            if temp_score > beta:
                return beta
            if temp_score > alpha:
                alpha = temp_score
                (ai.__currentI, ai.__currentJ) = (i, j)
        return alpha

    def one_step(self):
        node = gomokuAI(self.__gomoku, self.__currentState,
                        self.__depth)
        score = self.alpha_beta_prune(node)
        print score
        (i, j) = (node.__currentI, node.__currentJ)

        if not i is None and not j is None:
            if self.__gomoku.get_chessboard_state(i, j) \
                != BoardState.EMPTY:
                self.one_step()
            else:
                self.__gomoku.set_chessboard_state(i, j,
                        self.__currentState)
                return True
        return False



			