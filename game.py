import pygame
from pygame.locals import *
from sys import exit
from boardstate import *
from gomoku import Gomoku
from render import GameRender
from gomoku_ai import *

if __name__ == '__main__': 
    gomoku = Gomoku()
    render = GameRender(gomoku)
    #change the AI here
    ai = gomokuAI(gomoku, BoardState.BLACK, 2)
    ai2 = gomokuAI(gomoku, BoardState.WHITE, 2)

    result = BoardState.EMPTY
    enable_ai = True
    enable_ai2 = True

    ai.first_step()
    result = gomoku.get_chess_result()
    render.change_state()

    while True:

        if enable_ai2:
            ai2.one_step()
            result = gomoku.get_chess_result()
            if result != BoardState.EMPTY:
                print result, "wins"
                break
            if enable_ai:

                ai.one_step()
                result = gomoku.get_chess_result()

                if result != BoardState.EMPTY:
                    print result, "wins"
                    break
            else:
                render.change_state()

        

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

                    ai.one_step()
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