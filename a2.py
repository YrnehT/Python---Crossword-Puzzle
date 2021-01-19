#Name: Doan Huy Tran
#Le Minh Khoa Tran contributed in developing this code

def printboard(board):
    print(' ', end='')
    for i in range(len(board[0])):
        print(i % 10, end='')
    print()
    print(' ' + '_' * len(board[0]))

    for row in range(len(board)):
        print('|', end='')
        for col in range(len(board[row])):
            print(board[row][col], end='')
        print('|' + str(row))

    print(' ', end='')
    print('_' * len(board[0]))
    print(' ', end='')

    for i in range(len(board[0])):
        print(i % 10, end='')
    print()

def addFirstWord(board, word):
    word_list = list(word)
    word_length = len(word)
    if len(board[0]) < word_length:
        print('[ERROR] Word is to big to be inserted at the board horizontally')
        return False

    row = int(len(board) / 2)
    # half of the board - half of the word length
    col = int(len(board[0]) / 2) - int(word_length / 2)
    board[row][col:col + word_length] = word
# def addFirstWord(board, L):
#     for i in range(len(L)):
#         word_length = len(L[i])
#         if len(board[0]) < word_length:
#             print('[ERROR] ' + L[i] + ' is to big to be inserted to the board horizontally')
#         i += 1
#         if len(board[0]) < word_length:
#             firstword = L[i]
#             break
#     row = int(len(board) / 2)
#     # half of the board - half of the word length
#     col = int(len(board[0]) / 2) - int(word_length / 2)
#     board[row][col:col + word_length] = firstword

def checkvertical(board, word, row, col):
    #Check intersect
    listInterVer = []
    intersections = 0
    for letter in range(len(word)):
        if word[letter] == board[row][col]:
            intersections += 1
            listInterVer.append(letter)
    if intersections == 0:
        # print('[ERROR] Word ' + word + ' doesn\'t intersect vertically with any other word in the board')
        return False


    headRow = row - listInterVer[0]
    tailRow = headRow + (len(word)-1)

    #Check out of bounds:
    if headRow < 0 or tailRow > (len(board)-1):
        return False

    # Cannot change any letters != ' '
    for character in range(len(word)):
        rowChar = headRow + character
        if board[rowChar][col] != ' ' and board[rowChar][col] != word[character]:
            return False

    #Check left and right:
        if character not in listInterVer:
            if col - 1 > 0 or col + 1 < len(board[0]):
                if board[rowChar][col-1] != ' ' or board[rowChar][col+1] != ' ':
                    return False

    #Check top and bottom:
    if (headRow - 1) > 0 or tailRow < len(board[0]):
        if board[headRow - 1][col] != ' ' or board[tailRow + 1][col] != ' ':
            return False
    return True

def addvertical(board, word):
    for row in range(len(board)):
        for col in range(len(board[0])):
            # print(i, j)
            if checkvertical(board, word, row, col):
                # print('Working')
                index = None
                for letter in range(len(word)):
                    if word[letter] == board[row][col]:
                        index = letter
                        break
                headRow = row - index
                for char in range(len(word)):
                    board[headRow+char][col] = word[char]
                return True
    return False

def checkhorizontal(board, word, row, col):
    #Check intersect
    listInterHor = []
    intersections = 0
    for letter in range(len(word)):
        if word[letter] == board[row][col]:
            intersections += 1
            listInterHor.append(letter)
    if intersections == 0:
        # print('[ERROR] Word ' + word + ' doesn\'t intersect horizontally with any other word in the board')
        return False

    headCol = col - listInterHor[0]
    tailCol = headCol + (len(word) - 1)

    #Check out of bounds:
    if headCol < 0 or tailCol > (len(board[0])-1):
        return False

    # Cannot change any letters != ' '
    for character in range(len(word)):
        colChar = headCol + character
        if board[row][colChar] != ' ' and board[row][colChar] != word[character]:
            return False

    # Check top and bottom:
        if character != listInterHor[0]:
            if col - 1 > 0 or col + 1 < len(board):
                if board[row-1][colChar] != ' ' or board[row + 1][colChar] != ' ':
                    return False

    # Check left and right:
    if (headCol - 1) > 0 or tailCol < len(board[0]):
        if board[row][headCol - 1] != ' ' or board[row][tailCol + 1] != ' ':
            return False
    return True

def addhorizontal(board, word):
    for row in range(len(board)):
        for col in range(len(board[0])):
            if checkhorizontal(board, word, row, col):
                index = None
                for letter in range(len(word)):
                    if word[letter] == board[row][col]:
                        index = letter
                        break
                headCol = col - index
                for char in range(len(word)):
                    board[row][headCol+char] = word[char]
                return True
    return False

def addwords(board, L):
    remain = []
    addFirstWord(board, L[0])
    for word in L[1:]:
        if addvertical(board, word) == False and addhorizontal(board, word) == False:
            remain.append(word)
    for word in remain:
        if addvertical(board, word) == False and addhorizontal(board, word) == False:
            print(word + ' cannot be added to the board')


def crossword(L):
    board = [[' '] * 20 for i in range(20)]
    addwords(board, L)
    printboard(board)
    print('')
L0 = ['hippopotamus', 'horse', 'loon', 'snake', 'cat', 'rattlesnake', 'dinosaur']
L1 = ['addle', 'apple', 'clowning', 'incline', 'plan', 'burr']
L2 = ['clowning', 'not', 'ghost', 'game', 'hotel', 'south', 'north', 'east', 'west']
# L = ["abcdefghijklmnopqrst", "fffffggg", "ttttttttttuuuuuuuuuz", "yyyz", "qqqqqqqqqqqqqqy", "xxxxxxxxxaaaaaaa", "aaaaggg", "xxwwww", "wwwwvvvvve","vvvvvvvvvvvvq", "mat", "mat", "make", "make", "maker", "remake", "hat"]
# L = ["abcdefghijklmnopqrst",'fffffggg', "ttttttttttuuuuuuuuuz", "yyyz", "qqqqqqqqqqqqqqy",  "xxxxxxxxxaaaaaaa","aaaaggg"]

crossword(L0)
crossword(L1)
crossword(L2)