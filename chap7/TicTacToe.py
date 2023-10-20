
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
    while(true):
        a = input(question)
        if a == y:
            return X
        elif a == n:
            return O
        else
            print("plese y or n")

def pieces():
    global X = 1
    global O = 2
    turn = ask_yes_no("Do you require the first move? <y/n>: ")
    return turn
    

def new_borad():
    borad = [[0, 0, 0],
             [0, 0, 0],
             [0, 0, 0]]
    return borad
    
def display_board(board):
    cnt = 0
    
    for i in borad :
        print("\t")
        for j in borad[i]:
            if j == 0:
                print("   ")
            elif j == 1:
                print(" X ")
            elif j == 2:
                print(" O ")
            print("|")
        if cnt < len(borad):
            print("\t----------")
            cnt += 1



def legal_moves(board):

def winner(board):
    i = 0
    while i < 3:
        if board[i][0] == board[i][1] == board[i][2]:
            return True
        elif board[0][i] == board[1][i] == board[2][i]:
            return True
        i += 1
    if board[0][0] == board[1][1] = borad[2][2]:
        return True
    elif board[0][2] == board[1][1] == board[2][0]:
        return True
    else:
        return False

def human_move(board, human):
    n = input("Where will you move? <0 - 8>:")
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
    

    


def computer_move_A(board, user, computer):
    i = 0
    while (i < 3):
        if (board[i][0] == user && board[i][1] == user):
            board[i][2] = computer
            return 1
        elif (board[i][0] == user && board[i][2] == user):
            board[i][1] = computer
            return 1
        elif (board[i][1] == user && board[i][2] == user):
            board[i][0] = computer
            return 1
        elif (board[0][i] == user && board[1][i] == user):
            board[2][i] = computer
            return 1
        elif (board[0][i] == user && board[2][i] == user):
            board[1][i] = computer
            return 1
        elif (board[1][i] == user && board[2][i] == user):
            board[0][i] = computer
            return 1
        i += 1


    if (board[0][0] == user && board[1][1] == user):
        board[2][2] = copmuter
        return 1
    elif (board[1][1] == user && board[2][2] == user):
        board[0][0] = computer
        return 1
    elif (board[0][0] == user && board[2][2] == user):
        board[1][1] = computer
        return 1

def computer_move_B(board, human, computer):
    if board[1][1] == 0:
        board[1][1] = computer
        return 1
    elif board[0][0] == human && board[2][2] == human && board[0][1] == 0:
        board[0][1] = computer
        return 1
    elif board[2][0] == human && board[0][2] == human && board[0][1] == 0:
        board[0][1] = computer
        return 1


def computer_move_C(board, user, computer:
    i = 0, j = 0
    while i < 3:
        while j < 3:
            cnt = 0
            if board[i][j] == user:
                for 

            j += 1
        i += 1
                
                




        


def next_turn(turn):
    if turn == 1:
        return 0
    else:
        return 1

def comgrat_winner(the_winner, computer, human):
    if the_winner:
        if winner(computer):
            print("O won!\n")
            print("As I predicted, human, I am triumphant once more.")
            print("Proof that computers are superior to humans in all regards.\n")
        elif winner(human):
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




