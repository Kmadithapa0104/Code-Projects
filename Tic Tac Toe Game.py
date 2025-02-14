#Author : Kholofelo Madithapa 
#Date   : 26/04/2023
#Purpose: This program resembles a tic tac toe game whereby a user(O) plays against a computer(X). No form of Artificial Intelligence was used;
#         The computer chooses fields randomly.

from random import randrange

#The computer starts the game by playing at the center of the board.
board = [[1, 2, 3], [4, "X", 6], [7, 8, 9]]

#The function draws the board with numbers denoting empty squares or O and Z denoting moves been played.
#@parameter board - a list that denotes moves been played and square numbers for free squares.
def display_board(board):
    row = 0
    column1 = 0
    column2 = 1
    column3 = 2

    while row < len(board):
        print("+-------+-------+-------+")
        print("|       |       |       |")
        print("|   {}   |   {}   |   {}   |".format(board[row][column1], board[row][column2], board[row][column3]))
        print("|       |       |       |")
        row += 1
    
    print("+-------+-------+-------+")

#The function records moves made by the user.
#The user makes the move by entering the number that represents a particular square to mark with 'O'.
def enter_move(board):
    try:
        move = int(input("Enter your move: "))
        first_row = 0
        second_row = 1
        third_row = 2
        column = 0

        #Checks if the user has entered a number that represents a square to make a move on.
        if move > 0 and move < 10:
            if move in board[first_row]:
                for element in board[first_row]:
                    if element == move:
                        board[first_row][column] = "O"
                        break
                    else:
                        column += 1
            elif move in board[second_row]:
                for element in board[second_row]:
                    if element == move:
                        board[second_row][column] = "O"
                        break
                    else:
                        column += 1
            elif move in board[third_row]:
                for element in board[third_row]:
                    if element == move:
                        board[third_row][column] = "O"
                        break
                    else:
                        column += 1
            else:
                print("Square taken. Play on different square.")
        else:
            print("Please enter number between 0 and 9")
    except ValueError:
        print("Enter only a number")
    except:
        print("Something went wrong")

#Generates a list showing empty squares.
#These squares should only have a square number.
def make_list_of_free_fields(board):
    free_fields_list = list()
    outer = 0

    for row in board:
        inner = 0
        for element in row:
            if element != "O":
                if not element == "X":
                    free_fields_list.append((outer, inner))
            inner += 1
        outer += 1
    return free_fields_list

#The function shows the winner between the computer and the user.
def victory_for(board, sign):
    #Horizontal victories
    if sign == "O":
        if board[0][0] == sign and board[0][1] == sign and board[0][2] == sign:
            return True
        elif board[1][0] == sign and board[1][1] == sign and board[1][2] == sign:
            return True
        elif board[2][0] == sign and board[2][1] == sign and board[2][2] == sign:
            return True
    elif sign == "X":
        if board[0][0] == sign and board[0][1] == sign and board[0][2] == sign:
            return True
        elif board[1][0] == sign and board[1][1] == sign and board[1][2] == sign:
            return True
        elif board[2][0] == sign and board[2][1] == sign and board[2][2] == sign:
            return True
    
    #Vertical victories
    if sign == "O":
        if board[0][0] == sign and board[1][0] == sign and board[2][0] == sign:
            return True
        elif board[0][1] == sign and board[1][1] == sign and board[2][1] == sign:
            return True
        elif board[0][2] == sign and board[1][2] == sign and board[2][2] == sign:
            return True
    elif sign == "X":
        if board[0][0] == sign and board[1][0] == sign and board[2][0] == sign:
            return True
        elif board[0][1] == sign and board[1][1] == sign and board[2][1] == sign:
            return True
        elif board[0][2] == sign and board[1][2] == sign and board[2][2] == sign:
            return True

    #Diagonal victories
    if sign == "O":
        if board[0][0] == sign and board[1][1] == sign and board[2][2] == sign:
            return True
        elif board[0][2] == sign and board[1][1] == sign and board[2][0] == sign:
            return True
    elif sign == "X":
        if board[0][0] == sign and board[1][1] == sign and board[2][2] == sign:
            return True
        elif board[0][2] == sign and board[1][1] == sign and board[2][0] == sign:
            return True
    
#This function records necessary moves made by the computer
def draw_move(board):
    move = randrange(10)
    first_row = 0
    second_row = 1
    third_row = 2
    column = 0
    condition = True

    #Repeats the instructions until the computer randomly chooses a free square
    while condition:
        if move in board[first_row]:
            for element in board[first_row]:
                if move == element:
                    board[first_row][column] = "X"
                    condition = False
                else:
                    column += 1
        elif move in board[second_row]:
            for element in board[second_row]:
                if move == element:
                    board[second_row][column] = "X"
                    condition = False
                else:
                    column += 1
        elif move in board[third_row]:
            for element in board[third_row]:
                if move == element:
                    board[third_row][column] = "X"
                    condition = False
                else:
                    column += 1
        else:
            move = randrange(10)

display_board(board)

#Without any identifiable victory, the game will only allow the user to make their moves four times
#before the game runs into a tie.
for i in range(5):
    if len(make_list_of_free_fields(board)) != 0:
        if victory_for(board, "O") == True:
            print("Congratulations you have won!")
            break
        elif victory_for(board, "X") == True:
            print("Sorry the computer have won!")
            break
        else:
            enter_move(board)
            display_board(board)
            draw_move(board)
            display_board(board)
    else:
        if victory_for(board, "O") == True:
            print("Congratulations you have won!")
            break
        elif victory_for(board, "X") == True:
            print("Sorry the computer have won!")
            break
        else:
            print("It's a tie!") 