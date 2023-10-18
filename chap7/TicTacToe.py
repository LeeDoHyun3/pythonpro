


def display_instruct():
    print("\n\tWelcome to the greatest intellectual chalenge of all time: Tic-Tac-Toe.")
    print("\tThis will be a showdown between your human brain and my silicon processor.\n")
    print("\tYou will make your move known by entering a number, a bumber, 0 - 8. The number")
    print("\twill correspond to the board position as illustrated:")
    print("\t\t0 | 1 | 2")
    print("\t\t---------")
    print("\t\t3 | 4 | 5")
    print("\t\t---------")
    print("\t\t6 | 7 | 8")
    print("\tPrepare yourself, human. The ultimate battle is about to begin.\n")
    gobal X = ask_yes_no("Do you require the first move? <y/n>: ")
    

def ask_yes_no(question):
    while(true):
        a = input(question)
        if a == y:
            return 1
        elif a == n:
            return 0
        else
            print("plese y or n")

def pieces():

def new_borad():
    
    
def display_board(board):
    i = 0, j = 0
    l = int(len(board))
    while i < l :
        for x in board[i] :
            print("\t", x, "|")
        if i < 3:
            print("---------")
        i += 1


def legal_moves(board):

def winner(board):

def human_move(board, human):

def computer_move(board, computer, human):

def next_turn(turn):

def comgrat_winner(the_winner, computer, human)


display_instruct()
computer, human = pieces()
turn = X
board = new_board()
display_board(board)
while not winner(board):
    if turn == human:
        move = human_move(board, human)
        board[move] = human
    else:
        move = cmptr_mv(brd, hmn, cmptr)
        board[move] = computer
    display_board(board)
    turn = next_turn(turn)
    winner = winner(board)
    congrat_winner(winner, human, computer)




