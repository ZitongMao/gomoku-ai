import pygame
from pygame.locals import *
from sys import exit
from boardstate import *
from gomoku import Gomoku
from render import GameRender
#from gomoku_ai import gomokuAI

if __name__ == '__main__': 
    gomoku = Gomoku()
    render = GameRender(gomoku)
    #save for adding AI later
    #ai = gomokuAI(gomoku, BoardState.WHITE)
    result = BoardState.EMPTY
    enable_ai = False

    while True:
        #pygame event
        for event in pygame.event.get():
            #exit
            if event.type == QUIT:
                exit()
            elif event.type ==  MOUSEBUTTONDOWN:
                #play a step
                if render.one_step():
                    result = gomoku.get_chess_result()
                else:
                    continue
                if result != BoardState.EMPTY:
                    break
                if enable_ai:
                    #ai.one_step()
                    result = gomoku.get_chess_result()
                else:
                    render.change_state()
        
        #draw
        render.draw_chess()
        render.draw_mouse()

        if result != BoardState.EMPTY:
            render.draw_result(result)

        #update
        pygame.display.update()