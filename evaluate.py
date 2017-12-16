from boardstate import *

WHITE_6PATTERNS = [['empty', 'white', 'white', 'white', 'white','empty'],
                   ['empty', 'white', 'white', 'white', 'empty','empty'],
                   ['empty', 'empty', 'white', 'white', 'white','empty'],
                   ['empty', 'white', 'white', 'empty', 'white','empty'],
                   ['empty', 'white', 'empty', 'white', 'white','empty'],
                   ['empty', 'empty', 'white', 'white', 'empty','empty'],
                   ['empty', 'empty', 'white', 'empty', 'white','empty'],
                   ['empty', 'white', 'empty', 'white', 'empty','empty'],
                   ['empty', 'empty', 'white', 'empty', 'empty','empty'],
                   ['empty', 'empty', 'empty', 'white', 'empty','empty']]

WHITE_6SCORES = [50000,5000,5000,500,500,100,100,100,10,10]
# WHITE_6SCORES = [8640,720,720,720,720,120,120,120,20,20] #based on Dong (2015)


WHITE_5PATTERNS = [['white', 'white', 'white', 'white', 'white'],
                   ['white', 'white', 'white', 'white', 'empty'],
                   ['empty', 'white', 'white', 'white', 'white'],
                   ['white', 'white', 'empty', 'white', 'white'],
                   ['white', 'empty', 'white', 'white', 'white'],
                   ['white', 'white', 'white', 'empty', 'white']]
WHITE_5SCORES = [1000000,5000,5000,5000,5000,5000]
# WHITE_5SCORES = [50000,720,720,720,720,720] #based on Dong (2015)

BLACK_6PATTERNS = [['empty', 'black', 'black', 'black', 'black','empty'],
                   ['empty', 'black', 'black', 'black', 'empty','empty'],
                   ['empty', 'empty', 'black', 'black', 'black','empty'],
                   ['empty', 'black', 'black', 'empty', 'black','empty'],
                   ['empty', 'black', 'empty', 'black', 'black','empty'],
                   ['empty', 'empty', 'black', 'black', 'empty','empty'],
                   ['empty', 'empty', 'black', 'empty', 'black','empty'],
                   ['empty', 'black', 'empty', 'black', 'empty','empty'],
                   ['empty', 'empty', 'black', 'empty', 'empty','empty'],
                   ['empty', 'empty', 'empty', 'black', 'empty','empty']]
BLACK_6SCORES = [50000,5000,5000,500,500,100,100,100,10,10]
# BLACK_6SCORES = [8640,720,720,720,720,120,120,120,20,20] #based on Dong (2015)


BLACK_5PATTERNS = [['black', 'black', 'black', 'black', 'black'],
                   ['black', 'black', 'black', 'black', 'empty'],
                   ['empty', 'black', 'black', 'black', 'black'],
                   ['black', 'black', 'empty', 'black', 'black'],
                   ['black', 'empty', 'black', 'black', 'black'],
                   ['black', 'black', 'black', 'empty', 'black']]
BLACK_5SCORES = [1000000,5000,5000,5000,5000,5000]
# BLACK_5SCORES = [50000,720,720,720,720,720] #based on Dong (2015)

def sublist(small, big):
    '''
    Return True if small is a sublist of big.
    '''
    for i in xrange(len(big)-len(small)+1):
        for j in xrange(len(small)):
            if big[i+j] != small[j]:
                break
        else:
            return True
    return False

def enum_to_string(vector):
    '''
    Change BoardState.WHITE to 'white'.
    '''
    string_list = []
    for item in vector:
        if item == BoardState.BLACK:
            string_list.append('black')
        elif item == BoardState.WHITE:
            string_list.append('white')
        else:
            string_list.append('empty')
    
    return string_list


def evaluate_vector(vector):
    '''
    Return the score for a vector (line or column or diagonal)
    '''
    string_list = enum_to_string(vector)
    score = {'white': 0, 'black': 0}
    length = len(string_list)

    if length == 5:
        for i in range(len(WHITE_5PATTERNS)):
            if WHITE_5PATTERNS[i] == string_list:
                score['white'] += WHITE_5SCORES[i]
            if BLACK_5PATTERNS[i] == string_list:
                score['black'] += BLACK_5SCORES[i]
        return score

    for i in range(length - 5):
        temp = [string_list[i], string_list[i + 1], string_list[i + 2],
                string_list[i + 3], string_list[i + 4]]
        for i in range(len(WHITE_5PATTERNS)):
            if WHITE_5PATTERNS[i] == temp:
                score['white'] += WHITE_5SCORES[i]
            if BLACK_5PATTERNS[i] == temp:
                score['black'] += BLACK_5SCORES[i]

    for i in range(length - 6):
        temp = [
            string_list[i],
            string_list[i + 1],
            string_list[i + 2],
            string_list[i + 3],
            string_list[i + 4],
            string_list[i + 5],
            ]
        for i in range(len(WHITE_6PATTERNS)):
            if WHITE_6PATTERNS[i] == temp:
                score['white'] += WHITE_6SCORES[i]
            if BLACK_6PATTERNS[i] == temp:
                score['black'] += BLACK_6SCORES[i]
    return score



      

        