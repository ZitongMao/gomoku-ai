# pygame implementation based on xerwin's tutorial and pygame documentation

import pygame
from pygame.locals import *
from boardstate import *
from gomoku import Gomoku

IMAGE_PATH = 'UI/'

WIDTH = 540
HEIGHT = 540
MARGIN = 22
GRID = (WIDTH - 2 * MARGIN) / (N - 1)
PIECE = 32


class GameRender(object):

    def __init__(self, gomoku):
        self.__gomoku = gomoku

        # black starts first

        self.__currentPieceState = BoardState.BLACK

        # initialize pygame

        pygame.init()

        self.__screen = pygame.display.set_mode((WIDTH, HEIGHT), 0, 32)
        pygame.display.set_caption('Gomoku AI')

        # load UI resources

        self.__ui_chessboard = pygame.image.load(IMAGE_PATH
                + 'chessboard.jpg').convert()
        self.__ui_piece_black = pygame.image.load(IMAGE_PATH
                + 'piece_black.png').convert_alpha()
        self.__ui_piece_white = pygame.image.load(IMAGE_PATH
                + 'piece_white.png').convert_alpha()

    def coordinate_transform_map2pixel(self, i, j):

        # transform chessMap coordinates to UI

        return (MARGIN + j * GRID - PIECE / 2, MARGIN + i * GRID
                - PIECE / 2)

    def coordinate_transform_pixel2map(self, x, y):

        # transform UI coordinates to chessMap

        (i, j) = (int(round((y - MARGIN + PIECE / 2) / GRID)),
                  int(round((x - MARGIN + PIECE / 2) / GRID)))

        if i < 0 or i >= N or j < 0 or j >= N:
            return (None, None)
        else:
            return (i, j)

    def draw_chess(self):

        # board

        self.__screen.blit(self.__ui_chessboard, (0, 0))

        # chess piece

        for i in range(0, N):
            for j in range(0, N):
                (x, y) = self.coordinate_transform_map2pixel(i, j)
                state = self.__gomoku.get_chessboard_state(i, j)
                if state == BoardState.BLACK:
                    self.__screen.blit(self.__ui_piece_black, (x, y))
                elif state == BoardState.WHITE:
                    self.__screen.blit(self.__ui_piece_white, (x, y))
                else:

                      # BoardState.EMPTY

                    pass

    def draw_mouse(self):

        # track the mouse pointer

        (x, y) = pygame.mouse.get_pos()

        # chess piece moves with the mouse

        if self.__currentPieceState == BoardState.BLACK:
            self.__screen.blit(self.__ui_piece_black, (x - PIECE / 2, y
                               - PIECE / 2))
        else:
            self.__screen.blit(self.__ui_piece_white, (x - PIECE / 2, y
                               - PIECE / 2))

    def draw_result(self, result):
        font = pygame.font.SysFont('Arial', 55)
        tips = 'Game Over:'
        if result == BoardState.BLACK:
            tips = tips + 'Black Wins'
        elif result == BoardState.WHITE:
            tips = tips + 'White Wins'
        else:
            tips = tips + 'Draw'
        text = font.render(tips, True, (0, 0, 255))
        self.__screen.blit(text, (WIDTH / 2 - 200, HEIGHT / 2 - 50))

    def one_step(self):
        (i, j) = (None, None)

        # mouse click

        mouse_button = pygame.mouse.get_pressed()

        # left click

        if mouse_button[0]:
            (x, y) = pygame.mouse.get_pos()
            (i, j) = self.coordinate_transform_pixel2map(x, y)

        if not i is None and not j is None:

            # overlapped piece

            if self.__gomoku.get_chessboard_state(i, j) \
                != BoardState.EMPTY:
                return False
            else:
                self.__gomoku.set_chessboard_state(i, j,
                        self.__currentPieceState)
                return True

        return False

    def change_state(self):
        if self.__currentPieceState == BoardState.BLACK:
            self.__currentPieceState = BoardState.WHITE
        else:
            self.__currentPieceState = BoardState.BLACK



            