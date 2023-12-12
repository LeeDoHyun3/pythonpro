
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
    

def ask_yes_no(question):
    while(True):
        a = input(question)
        if a == 'y':
            return 1
        elif a == 'n':
            return 2
        else:
            print("y or n")

def pieces():
    global X
    global O
    X = 1
    O = 2
    t = ask_yes_no("Do you require the first move? <y/n>: ")
    if t == X:
        return O, X
    else:
        return X, O
    

def new_board():
    board = [[0, 0, 0],
             [0, 0, 0],
             [0, 0, 0]]
    return board
    
def display_board(board): 
    i = 0
    for b in board:
        j = 0
        print("\t", end = "")
        for bb in b:
            print("", end = "")
            if bb == X:
                print("X", end = "")
            elif bb == O:
                print("O", end = "")
            else:
                print(" ", end = "")
            if j < 2:
                print(" | ", end = "")
                j += 1
        if i < 2:
            print("\n\t---------")
            i += 1
    print("")



def legal_moves(board):
    return 0

def winner(board):
    for i in board:
        for j in i:
            if j == 0:
                return False
            else:
                print(j)
    i = 0
    while i < 3:
        if board[i][0] == board[i][1] == board[i][2]:
            return True
        elif board[0][i] == board[1][i] == board[2][i]:
           return True
        i += 1
    if board[0][0] == board[1][1] == borad[2][2]:
        return True
    elif board[0][2] == board[1][1] == board[2][0]:
        return True
    else:
        return False

def human_move(board, human):
    n = int(input("Where will you move? <0 - 8>:"))
    n1 = int(n / 3)
    n = n % 3
    board[n1][n] = human
    


def computer_move(board, computer, human):
    i = 0
    
    i = computer_move_A(board, computer, computer)
    if i == 1:
        return 0
    i = computer_move_A(board, human, computer)
    if i == 1:
        return 0
    i = computer_move_B(board, human, computer)
    if i == 1:
        return 0
    i = computer_move_c(board, human, computer)
    if i == 1:
        return 0


    


def computer_move_A(board, user, computer):
    i = 0
    while (i < 3):
        if (board[i][0] == user and board[i][1] == user):
            if board[i][2] == 0:
                board[i][2] = computer
                return 1
        elif (board[i][0] == user and board[i][2] == user):
            if board[i][1] == 0:
                board[i][1] = computer
                return 1
        elif (board[i][1] == user and board[i][2] == user):
            if board[i][0] == 0:
                board[i][0] = computer
                return 1
        elif (board[0][i] == user and board[1][i] == user):
            if board[2][i] == 0:
                board[2][i] = computer
                return 1
        elif (board[1][i] == user and board[2][i] == user):
            if board[1][i] == 0:
                board[1][i] = computer
                return 1
        elif (board[1][i] == user and board[2][i] == user):
            if board[0][i] == 0:
                board[0][i] = computer
                return 1
        i += 1


    if (board[0][0] == user and board[1][1] == user):
        if board[i][2] == 0:
            board[2][2] = copmuter
            return 1
    elif (board[1][1] == user and board[2][2] == user):
        if board[0][0] == 0:
            board[0][0] = computer
            return 1
    elif (board[0][0] == user and board[2][2] == user):
        if board[1][1] == 0:
            board[1][1] = computer
            return 1
    elif (board[0][2] == user and board[1][1] == user):
        if board[2][0] == 0:
            board[2][0] = copmuter
            return 1
    elif (board[1][1] == user and board[2][0] == user):
        if board[0][2] == 0:
            board[0][2] = computer
            return 1
    elif (board[2][0] == user and board[0][2] == user):
        if board[1][1] == 0:
            board[1][1] = computer
            return 1

def computer_move_B(board, human, computer):
    if board[1][1] == 0:
        board[1][1] = computer
        return 1
    elif board[0][0] == human and board[2][2] == human and board[0][1] == 0:
        board[0][1] = computer
        return 1
    elif board[2][0] == human and board[0][2] == human and board[0][1] == 0:
        board[0][1] = computer
        return 1


def computer_move_C (board, human, computer):
    if board[0][0] == human and board[1][2] == human:
        if (board[0][1] != computer and board[0][2] != computer and board[2][2] != computer):
            board[0][1] = computer
            return 1
    if (board[0][0] == human and board[2][1] == human):
        if (board[1][0] != computer and board[2][0] != computer and board[2][2] != computer):
            board[1][0] = computer
            return 1
    if board[0][2] == human and board[1][0] == human:
        if (board[0][0] != computer and board[0][1] != computer and board[2][0] != computer):
            board[0][1] = computer
            return 1
    if (board[0][2] == human and board[2][0] == human):
        if (board[1][2] != computer and board[2][2] != computer and board[2][0] != computer):
            board[1][2] = computer
            return 1
    if board[2][0] == human and board[0][1] == human:
        if (board[0][0] != computer and board[0][2] != computer and board[1][0] != computer):
            board[1][0] = computer
            return 1
    if (board[2][0] == human and board[1][2] == human):
        if (board[2][1] != computer and board[2][2] != computer and board[0][2] != computer):
            board[2][1] = computer
            return 1
    if board[2][2] == human and board[0][1] == human:
        if (board[0][0] != computer and board[0][2] != computer and board[1][2] != computer):
            board[1][2] = computer
            return 1
    if (board[2][2] == human and board[1][0] == human):
        if (board[0][0] != computer and board[0][2] != computer and board[2][1] != computer):
            board[2][1] = computer
            return 1
     
 
 


    else:
        for i in board:
            for j in i:
                if j == 0:
                    j = computer
        


def next_turn(turn):
    if turn == 1:
        return 0
    else:
        return 1

def congrat_winner(the_winner, computer, human):
    if the_winner:
        if winner(True):
            print("O won!\n")
            print("As I predicted, human, I am triumphant once more.")
            print("Proof that computers are superior to humans in all regards.\n")
        elif winner():
            print("X won!\n")
            print("No, no! It cannot be!  Somehow you tricged me, human.")
            print("But never again! I, the computer, so wears it!\n")


display_instruct()
computer, human = pieces()
turn = X
board = new_board()
display_board(board)
while not winner(board):
    if turn == human:
        human_move(board, human)
    else:
        cmptr_mv(brd, hmn, cmptr)
    display_board(board)
    turn = next_turn(turn)
    winner = winner(board)
    congrat_winner(winner, human, computer)



