import random
import time
import datetime
from players import Player

# TicTacToe Board with assigned values for coordinates
board = [["   ","(1)","(2)","(3)","",""],
         ["[1]"," . "," . "," . ","",""],
         ["[2]"," . "," . "," . ","",""],
         ["[3]"," . "," . "," . ","",""],
         ["","","","","",""],
         ["","","","","",""]]


# first boss move count
boss1_move_count = 0

# elements for second boss
loss = False
progress = 0
boss2_move_counter = 0

# items
inventory = ["items:"]
earthrune = 0

# for gunsmith
life = True

# for fourth boss
boss4_move_counter = 0

# final boss
final_move_counter = 0

# player details
user_name = ""
when_played = datetime.datetime.now()
trials = 0

# keep score
def score_board():
    global trials
    global user_name
    global when_played
    player = []

    # get username
    user_name = input("Give username: ")
    player.append("Username: " + user_name)

    # when played as a string
    player.append("When played: " + str(when_played))

    # score
    player.append("Tries: " + str(trials))

    # seperator for a new line
    player.append("")

    # open file for writing, if does not exist, make a new one
    scoreboard = open("Story scoreboard.txt","a+")

    # append player line by line into scoreboard
    for category in player:
        scoreboard.writelines(category + "\n")
    scoreboard.close()

# story
def story():
    global progress
    if progress == 0:
        print("")
        print("You have woken up in a strange looking town..")
        time.sleep(1)
        print("All you know is that you have a mission, it is yet unclear as to what that mission is though.")
        print("")
        time.sleep(2)
        print("THY SHALL BEGIN THE TRIALS!")
        return ""

    elif progress == 1:
        print("")
        print("You have defeated the younger brother of the gambler, congratulations")
        time.sleep(2)
        print("For now, however, in order to progress you need to defeat the gambler..")
        print("I must warn you, although his moves seem easy, for he has a special power of luck")
        print("Good luck on your journey traveler, may luck be on your side!")
        time.sleep(3)
        print("For a coinflip will decide your faith..")
        time.sleep(5)
        return ""

    elif progress == 2:
        print("")
        print("I see luck was on your side, good!")
        time.sleep(2)
        print("The grounds are not stable ahead..")
        time.sleep(1)
        print("Be careful where you step, you do not want to wake up the giant..")
        time.sleep(2)
        print("Farewell")
        time.sleep(4)
        return ""

    elif progress == 3:
        print("")
        print("You have survived, although the old path is now sunken into the ground..")
        time.sleep(2)
        print("Go to the tavern near the river, there you'll meet the gun smith.")
        print("He has a map for a secret entrance which gets you back on route.")
        time.sleep(2)
        print("Good luck, for he can be unpredictable.")
        time.sleep(4)
        return ""

    elif progress == 4:
        print("")
        print("You have the map I see, come see me where X marks the location.")
        time.sleep(1)
        print("Be careful, however, the one eyed warrior is outside.")
        time.sleep(2)
        print("He has a blind spot, use it for thy advantage.")
        print("")
        time.sleep(2)

        return""
    elif progress == 5:

        return ""

# items used
def items():
    global earthrune
    if earthrune == 1:
        print("")
        print("Once you use the rune, you loose it.")
        time.sleep(2)
        print("If used, it will destroy a random enemy tile and turn it into a free one.")
        time.sleep(2)
        print("Note, it may also destroy other stones.")
        time.sleep(2)
        print("")
        print("Use it wisely.")
        return ""

# Make board look cool
def print_board(board):
    for row in board:
        row_print = ""
        for value in row:
            row_print += str(value) + " "
        print(row_print)
    return ""

# Instructions
def inst():
    instructions = "Input placement instructions: To place X or O, give coordinates. Horizontal axis is from 1-3 and vertical axis 1-3. "
    instructions1 = "First input should be the vertical axis coordinate with [] on the board"
    instructions2 = "Second input should be the horizontal axis coordinate with () on the board"
    print("")
    print(instructions)
    print(instructions1)
    print(instructions2)
    print("")
    return ""

# makes sure there is no stalemate
def nostalemate(board):
    for i in range(1,4):
        for j in range(1,4):
            if board[i][j] == " . ":
                return True

    return False

# Cleans board
def clean_board(board):
    for i in range(1,4):
        for j in range(1,4):
            if board[i][j] != " . ":
                board[i][j] = " . "
                board[0][2] = "(2)"
    return board

# item pouch
def pouch():
    global inventory
    global earthrune
    use = input("Would you like to use an item (type: yes to use, else press enter)? ")

    if use == "yes":
        print(inventory)
        pick = int(input("Select item (first item = 1 and so on): "))
        if pick == 1:
            earth_rune(board)
            earthrune -= 1
            return""
    else:
        return""

# earthquake
def earthquake(board):

    print("")
    print("Ground Shakes...")
    print("")

    time.sleep(2)

    Hor = random.randint(1,3)
    Ver = random.randint(1,3)
    if board[Hor][Ver] != "   ":
        print("A square breaks off!")
        print("")
        time.sleep(1)
        board[Hor][Ver] = "   "
    else:
        print("The shockwave missed the board!")
        print("")
    return print_board(board)

# earthrune
def earth_rune(board):
    global earthrune
    V = random.randint(1,3)
    H = random.randint(1,3)

    if earthrune == 1:
        while board[V][H] != " O ":
            V = random.randint(1, 3)
            H = random.randint(1, 3)
        board[V][H] = " . "
        return print_board(board)
    else:
        return ""

# final battle boulder
def boulder(board):
    V = random.randint(1,3)
    H = random.randint(1,3)

    print("")
    print("Enemy kicks a giant boulder into an empty square!")
    print("")
    time.sleep(2)

    # get rid of old boulder
    for v in range(1,4):
        for h in range(1,4):
            if board[v][h] == "( )":
                board[v][h] = " . "
    # make boulder appear at random free location
    while board[V][H] != " . ":
        V = random.randint(1, 3)
        H = random.randint(1, 3)
    board[V][H] = "( )"
    return print_board(board)

# Ways to win, None = No Win
def win(board):
    global loss
    if board[1][1] == " X " and board[1][2] == " X " and board[1][3] == " X ":
        return True
    elif board[2][1] == " X " and board[2][2] == " X " and board[2][3] == " X ":
        return True
    elif board[3][1] == " X " and board[3][2] == " X " and board[3][3] == " X ":
        return True
    elif board[1][1] == " X " and board[2][1] == " X " and board[3][1] == " X ":
        return True
    elif board[1][2] == " X " and board[2][2] == " X " and board[3][2] == " X ":
        return True
    elif board[1][3] == " X " and board[2][3] == " X " and board[3][3] == " X ":
        return True
    elif board[1][1] == " X " and board[2][2] == " X " and board[3][3] == " X ":
        return True
    elif board[1][3] == " X " and board[2][2] == " X " and board[3][1] == " X ":
        return True

    elif board[1][1] == " O " and board[1][2] == " O " and board[1][3] == " O ":
        return False
    elif board[2][1] == " O " and board[2][2] == " O " and board[2][3] == " O ":
        return False
    elif board[3][1] == " O " and board[3][2] == " O " and board[3][3] == " O ":
        return False
    elif board[1][1] == " O " and board[2][1] == " O " and board[3][1] == " O ":
        return False
    elif board[1][2] == " O " and board[2][2] == " O " and board[3][2] == " O ":
        return False
    elif board[1][3] == " O " and board[2][3] == " O " and board[3][3] == " O ":
        return False
    elif board[1][1] == " O " and board[2][2] == " O " and board[3][3] == " O ":
        return False
    elif board[1][3] == " O " and board[2][2] == " O " and board[3][1] == " O ":
        return False

    elif loss == True:
        return True

    else:
        return None

# first boss
def first_boss(board, play1H, play1V):
    global boss1_move_count

    if boss1_move_count <= 1:
        if board[play1H + 1][play1V + 1] == " . ":
            board[play1H + 1][play1V + 1] = " O "
        elif board[play1H - 1][play1V - 1] == " . ":
            board[play1H - 1][play1V - 1] = " O "
        elif board[play1H + 1][play1V] == " . ":
            board[play1H + 1][play1V] = " O "
        elif board[play1H - 1][play1V] == " . ":
            board[play1H - 1][play1V] = " O "
        elif board[play1H][play1V + 1] == " . ":
            board[play1H][play1V + 1] = " O "
        elif board[play1H][play1V - 1] == " . ":
            board[play1H][play1V - 1] = " O "
        elif board[play1H + 2][play1V + 2] == " . ":
            board[play1H + 2][play1V + 2] = " O "
        elif board[play1H - 2][play1V - 2] == " . ":
            board[play1H - 2][play1V - 2] = " O "
        elif board[play1H + 2][play1V] == " . ":
            board[play1H + 2][play1V] = " O "
        elif board[play1H - 2][play1V] == " . ":
            board[play1H - 2][play1V] = " O "
        elif board[play1H][play1V + 2] == " . ":
            board[play1H][play1V + 2] = " O "
        elif board[play1H][play1V - 2] == " . ":
            board[play1H][play1V - 2] = " O "

        return print_board(board)
    elif boss1_move_count > 2:
        H = random.randint(1, 3)
        V = random.randint(1, 3)

        while board[H][V] != " . ":
            H = random.randint(1, 3)
            V = random.randint(1, 3)

        board[H][V] = " O "

        return print_board(board)

# second boss
def second_boss(board):
    global loss
    global boss2_move_counter
    coin_flip = random.randint(1,2)

    #coinflip conditions
    if coin_flip == 1:
        coin_flip = "heads"
    elif coin_flip == 2:
        coin_flip = "tails"

    if boss2_move_counter == 0:
        if board[3][3] == " . ":
            board[3][3] = " O "
            boss2_move_counter += 1
            return print_board(board)
        else:
            board[1][1] = " O "
            boss2_move_counter += 1
            return print_board(board)

    if boss2_move_counter == 1:

        print("")
        print("Let's make this interesting, a simple coin flip to decide the game!")
        time.sleep(2)
        print("")
        print("Heads or tails?")
        time.sleep(2)
        choice = input("Pick heads or tails (type: heads or type: tails): ")
        print("")

        #timer countdown here
        time.sleep(5)

        print(coin_flip)
        #another timer countdown here
        time.sleep(5)

        #bot wins
        if coin_flip != choice and board[3][3] == " O ":
            if board[2][3] == " . " and board[1][3] == " . ":
                board[2][3] = " O "
                board[1][3] = " O "

            elif board[3][2] == " . " and board[3][1] == " . ":
                board[3][2] = " O "
                board[3][1] = " O "

            elif board[2][2] == " . " and board[1][1] == " . ":
                board[2][2] = " O "
                board[1][1] = " O "
            return print_board(board)

        elif coin_flip != choice and board[1][1] == " O ":
            if board[2][1] == " . " and board[3][1] == " . ":
                board[2][1] = " O "
                board[3][1] = " O "

            elif board[1][2] == " . " and board[1][3] == " . ":
                board[1][2] = " O "
                board[1][3] = " O "

            elif board[2][2] == " . " and board[3][3] == " . ":
                board[2][2] = " O "
                board[3][3] = " O "
            return print_board(board)
        #bot gives up
        #starting position 3, 3
        elif coin_flip == choice:
            #Gives up for loosing, unlucky
            print("You have won....")
            time.sleep(2)
            print("So this is what defeat feels like....")
            time.sleep(2)
            print("I am sorry to have let you down master, for I have lost....")
            print("")
            #build suspense
            time.sleep(5)
            loss = True

# third boss
def third_boss(board):
    H = random.randint(1,3)
    V = random.randint(1,3)

    while board[H][V] != " . ":
        H = random.randint(1,3)
        V = random.randint(1,3)

    board[H][V] = " O "

    return print_board(board)

# fourth boss
def fourth_boss(board):
    global boss4_move_counter

    if boss4_move_counter == 0:
        H = random.randint(1, 3)
        V = random.randint(1, 3)

        while board[H][V] != " . ":
            H = random.randint(1, 3)
            V = random.randint(1, 3)
        if H == 2 and V == 2:
            print("Enemy 4: That was a shot in the dark!")

        board[H][V] = " O "
        return print_board(board)

    elif boss4_move_counter > 0:
        for list in range(1,4):
            # reset count for each row
            count_enemy = 0
            for item in range(1,4):
                # find enemy
                if board[list][item] == " X ":
                    count_enemy += 1
                    if count_enemy == 2:
                        # if enemy is a threat, stop threat
                        for space in range(1,4):
                            if board[list][space] == " . ":
                                board[list][space] = " O "
                                return print_board(board)

            if list == 3 and count_enemy < 2:
                for item1 in range(1,4):
                    count_enemy1 = 0
                    for list1 in range(1,4):
                        if board[list1][item1] == " X ":
                            count_enemy1 += 1
                            if count_enemy1 == 2:
                                for space1 in range(1,4):
                                    if board[space1][item1] == " . ":
                                        board[space1][item1] = " O "
                                        return print_board(board)

                    if item1 == 3 and count_enemy1 < 2:
                        H = random.randint(1,3)
                        V = random.randint(1,3)

                        while board[H][V] != " . ":
                            H = random.randint(1,3)
                            V = random.randint(1,3)
                        if H == 2 and V == 2:
                            print("Enemy 4: That was a shot in the dark!")

                        board[H][V] = " O "
                        return print_board(board)

# final boss
def final_boss(board):
    global final_move_counter
    decide_to_attack = False

    if final_move_counter == 0:
        H = random.randint(1, 3)
        V = random.randint(1, 3)

        while board[H][V] != " . ":
            H = random.randint(1, 3)
            V = random.randint(1, 3)

        board[H][V] = " O "
        return print_board(board)

    elif final_move_counter > 0:
        for list in range(1,4):
            # reset count for each row
            count_enemy = 0
            for item in range(1,4):
                # find enemy
                if board[list][item] == " X ":
                    count_enemy += 1
                    if count_enemy == 2:
                        # if enemy is a threat, stop threat
                        for space in range(1,4):
                            if board[list][space] == " . ":
                                board[list][space] = " O "
                                return print_board(board)

            if list == 3 and count_enemy < 2:
                for item1 in range(1,4):
                    count_enemy1 = 0
                    for list1 in range(1,4):
                        if board[list1][item1] == " X ":
                            count_enemy1 += 1
                            if count_enemy1 == 2:
                                for space1 in range(1,4):
                                    if board[space1][item1] == " . ":
                                        board[space1][item1] = " O "
                                        return print_board(board)
                    # check for slash lines
                    if item1 == 3 and count_enemy1 < 2:
                        if board[1][1] == " X " and board[2][2] == " X " and board[3][3] == " . ":
                            board[3][3] = " O "
                            return print_board(board)
                        elif board[1][1] == " X " and board[3][3] == " X " and board[2][2] == " . ":
                            board[2][2] = " O "
                            return print_board(board)
                        elif board[2][2] == " X " and board[3][3] == " X " and board[1][1] == " . ":
                            board[1][1] = " O "
                            return print_board(board)
                        elif board[1][3] == " X " and board[2][2] == " X " and board[3][1] == " . ":
                            board[3][1] = " O "
                            return print_board(board)
                        elif board[1][3] == " X " and board[3][1] == " X " and board[2][2] == " . ":
                            board[2][2] = " O "
                            return print_board(board)
                        elif board[3][1] == " X " and board[2][2] == " X " and board[1][3] == " . ":
                            board[1][3] = " O "
                            return print_board(board)
                        else:
                            decide_to_attack = True

                            # turn into offensive battle
                            if decide_to_attack == True:
                                for list in range(1, 4):
                                    # reset count for each row
                                    count_self = 0
                                    for item in range(1, 4):
                                        # find self
                                        if board[list][item] == " O ":
                                            count_self += 1
                                            if count_self == 1:
                                                # if self can fit into row, put self there
                                                for space in range(1, 4):
                                                    if board[list][space] == " . ":
                                                        board[list][space] = " O "
                                                        return print_board(board)
                                # check for self in vertical space
                                    if list == 3 and count_self < 2:
                                        for item1 in range(1, 4):
                                            count_self1 = 0
                                            for list1 in range(1, 4):
                                                if board[list1][item1] == " O ":
                                                    count_self1 += 1
                                                    if count_self == 1:
                                                        for space1 in range(1, 4):
                                                            if board[space1][item1] == " . ":
                                                                board[space1][item1] = " O "
                                                                return print_board(board)

# player vs 1st bot function
def play1vboss1(board):
    global progress
    global boss1_move_count
    boss1_move_count = 0

    while win(board) == None:
        if nostalemate(board) == True:
            play1H = int(input("Location of X vertical axis: "))
            play1V = int(input("Location of X horizontal axis: "))
            player1 = Player(play1H,play1V,board)
            # Anticheat
            if board[play1H][play1V] == " O ":
                player1.set_player2()
                print(print_board(board))
                print("")
                print("Enemy 1: No Cheating!!")
                print("")
            else:
                player1.set_player1()
                print(print_board(board))
            if nostalemate(board) == True:
                first_boss(board, play1H, play1V)
                boss1_move_count += 1
        else:
            break

    if win(board) == True:
        time.sleep(2)
        print("Enemy 1: WHAT?")
        time.sleep(1)
        print("Enemy 1: You have defeated me...")
        time.sleep(2)
        progress += 1
        return "WIN Player 1"

    elif win(board) == False:
        time.sleep(1)
        print("Enemy 1: You have lost my friend!")
        return "WIN Player 2"
    elif nostalemate(board) == False:
        time.sleep(2)
        print("Enemy 1: Two equally great warriors, you have my respect.")
        return "Stalemate"

# player v 2nd boss
def play1vboss2(board):
    global progress
    global loss
    global boss2_move_counter
    boss2_move_counter = 0
    time.sleep(1)

    print("")
    print("Enemy 2: My fallen brother... You were not ready...")

    time.sleep(1)

    print("Enemy 2: Now you play against me! The apprentice of the master of this kingdom. Thy shall loose today!")
    time.sleep(2)
    print("Enemy 2: For I am always the lucky one!")
    print("")

    time.sleep(4)

    print(print_board(board))

    while win(board) == None:
        if nostalemate(board) == True:

            play1H = int(input("Location of X vertical axis: "))
            play1V = int(input("Location of X horizontal axis: "))
            player1 = Player(play1H,play1V,board)
            # Anticheat
            if board[play1H][play1V] == " O ":
                player1.set_player2()
                print(print_board(board))
                print("Enemy 2: Thy have no honour, you make me sick..")
            else:
                player1.set_player1()
                print(print_board(board))
                second_boss(board)
        else:
            break


    if win(board) == True:
        progress += 1
        return "WIN Player 1"
    elif win(board) == False:
        time.sleep(1)
        print("Enemy 2: Better luck next time my friend!")
        return "WIN Player 2"
    elif nostalemate(board) == False:
        time.sleep(2)
        print("Enemy 2: Impossible, it is a draw...")
        time.sleep(1)
        print("Enemy 2: You have my respect warrior..")
        return "Stalemate"

# player v 3rd boss
def play1vboss3(board):
    global progress
    global earthrune
    global inventory

    # get rid of last games scenario
    global loss
    loss = False


    time.sleep(3)
    print("Enemy 3: I see you have defeated the gambler.")
    time.sleep(2)
    print("Enemy 3: It is time for you to face me..")
    time.sleep(1)
    print("Enemy 3: THE EARTH GIANT!")
    time.sleep(1)
    print("")
    print("The ground shakes..")
    print("")
    print("The board breaks!")
    print("")
    time.sleep(2)

    # board break
    board[0][2] = "  "
    print(print_board(board))


    while win(board) == None:
        if nostalemate(board) == True:

            play1H = int(input("Location of X vertical axis: "))
            play1V = int(input("Location of X horizontal axis: "))
            player1 = Player(play1H,play1V,board)
            # Anticheat
            if board[play1H][play1V] == " O ":
                player1.set_player2()
                print(print_board(board))
                print("Enemy 3: How I imagined you would play!")
            else:
                player1.set_player1()
                print(print_board(board))
                third_boss(board)
                if win(board) == None and nostalemate(board) == True:
                    earthquake(board)
        else:
            break

    if win(board) == True:
        time.sleep(2)
        print("Enemy 3: I shall return back to the earth...")
        time.sleep(2)
        print("Enemy 3: Good luck..")
        progress += 1
        if earthrune == 0:
            print("")
            print("You have received an earth rune")
            earthrune += 1
            inventory.append("Earth Rune")
            print(items())
        return "WIN Player 1"
    elif win(board) == False:
        time.sleep(1)
        print("Enemy 3: Defeated by earth!")
        return "WIN Player 2"
    elif nostalemate(board) == False:
        time.sleep(2)
        print("Enemy 3: I am yet to be defeated!")
        time.sleep(1)
        print("Enemy 3: Thy shall go back to training")
        return "Stalemate"

# gunsmith cutscene
def gunsmith():
    global progress
    global life
    life = True
    print("Owner: Welcome to the tavern!")
    print("Owner: I heard you were looking for the gunsmith, he is at the table far end of the floor.")
    print("")
    time.sleep(3)
    print("Gunsmith: Heard you were looking for me.")
    time.sleep(1)
    print("Gunsmith: You may have your map..")
    print("")
    print("")
    time.sleep(1)
    print("Gunsmith: If..")
    print("")
    time.sleep(1)
    print("Gunsmith: You beat me at Russian Roulette.")
    time.sleep(2)
    print("")

    shot = random.randint(1,6)
    click = 6
    turn = 0

    if shot == 6:
        print("Gunsmith: I will go.")
        print("")
        time.sleep(1)
        print("click")
        print("")
        print("BANG")
        time.sleep(2)
        print("")
        print("You Have Received The Secret Map")
        progress += 1
        return ""

    while life == True:
        if click != shot:
            print("Gunsmith: I will go.")
            print("")
            time.sleep(1)
            print("click")
            print("")
            turn += 1
            click -= 1
        elif click == shot:
            break
        if click != shot:
            time.sleep(1)
            print("Gunsmith: Your turn, here you go.")
            print("")
            time.sleep(1)
            print("click")
            turn += 1
            click -= 1
            time.sleep(1)
            print("")
        elif click == shot:
            life = False

    if turn % 2 == 1:
        progress += 1
        print("BANG")
        print("")
        time.sleep(2)
        print("You Have Received The Secret Map")
        return ""
    elif turn % 2 == 0:
        progress += 1
        print("The gun is jammed!")
        time.sleep(1)
        print("")
        print("Gunsmith: I guess luck was on your side, here have the map my friend")
        print("")
        print("You Have Received The Secret Map")
        time.sleep(1)

        return ""

# player v 4th boss
def play1vboss4(board):
    global progress
    global boss4_move_counter

    print("")
    print("I shall challenge you to a duel!")
    time.sleep(1)
    print("I have been thirsty to duel again, ever since I lost my other eye to the king..")
    time.sleep(2)
    print("")

    boss4_move_counter = 0

    print(print_board(board))
    while win(board) == None:
        if nostalemate(board) == True:

            pouch()
            play1H = int(input("Location of X vertical axis: "))
            play1V = int(input("Location of X horizontal axis: "))
            player1 = Player(play1H,play1V,board)
            # Anticheat
            if board[play1H][play1V] == " O ":
                player1.set_player2()
                print(print_board(board))
                print("Enemy 4: I may be blind on my other eye but I can still see you cheating!")
            else:
                player1.set_player1()
                print(print_board(board))
                fourth_boss(board)
                boss4_move_counter += 1
        else:
            break

    if win(board) == True:
        progress += 1
        print("")
        time.sleep(2)
        print("Enemy 4: A defeat! You have my respect, fellow warrior.")
        print("")
        print("Enemy 4: Good luck finding the secret path, for without it you can't pass the mountains.")
        time.sleep(2)
        print("")
        return "WIN Player 1"
    elif win(board) == False:
        time.sleep(1)
        print("Enemy 4: Be more careful with your placements next time, HA HA HA!")
        print("")
        return "WIN Player 2"
    elif nostalemate(board) == False:
        time.sleep(2)
        print("Enemy 4: Wonderful, a stalemate!")
        time.sleep(1)
        print("Enemy 4: Good battle.")
        print("")
        return "Stalemate"

# player v final boss
def play1vfinal(board):
    global progress
    global final_move_counter
    # story
    time.sleep(3)
    print("King: Finally we meet!")
    time.sleep(2)
    print("King: I have guided you the way, where X marks the location")
    time.sleep(2)
    print("")
    print("May our battle begin!")
    print("")

    final_move_counter = 0

    print(print_board(board))

    while win(board) == None:
        if nostalemate(board) == True:
            boulder(board)
            pouch()
            play1H = int(input("Location of X vertical axis: "))
            play1V = int(input("Location of X horizontal axis: "))
            player1 = Player(play1H, play1V, board)
            # Anticheat
            if board[play1H][play1V] == " O ":
                player1.set_player2()
                print(print_board(board))
                print("King: Cheating is punishable by death!")
            else:
                player1.set_player1()
                print(print_board(board))
                final_boss(board)
                final_move_counter += 1
        else:
            break

    if win(board) == True:
        progress += 1
        print("")
        time.sleep(2)
        print("King: Your purpose has been fulfilled..")
        print("")
        print("King: Thy have provided to be worthy of replacing this throne.")
        time.sleep(2)
        print("")
        return "WIN Player 1"
    elif win(board) == False:
        time.sleep(1)
        print("King: Maybe I was wrong about you..")
        time.sleep(4)
        print("")
        return "WIN Player 2"
    elif nostalemate(board) == False:
        time.sleep(2)
        print("King: A draw, thy are still not good enough..")
        time.sleep(1)
        print("")
        return "Stalemate"

# Main function
def play1v1():
    # Gives instructions in the start
    inst()
    print_board(board)

    # to check best of three
    X_wins = 0
    O_wins = 0

    print("")
    print("This is a game of best to three, good luck!")
    print("")

    # Loop to make turns in the game
    while X_wins < 2 or O_wins < 2:

        if win(board) == True and X_wins < 2:
            X_wins += 1
            clean_board(board)
            print_board(board)
        elif win(board) == False and O_wins < 2:
            O_wins += 1
            clean_board(board)
            print_board(board)

        print("Score:")
        print("X - O")
        print(X_wins,"-",O_wins)
        print("")

        if X_wins == 2:
            print("WIN Player 1")
            return""
        elif O_wins == 2:
            print("WIN Player 2")
            return""

        while win(board) == None:
            # Counter if statement in case of a stalemate

            if nostalemate(board) == True:
                #player 1 turn
                play1H = int(input("Location of X vertical axis: "))
                play1V = int(input("Location of X horizontal axis: "))
                print("")
                player1 = Player(play1H, play1V, board)
                # Anti cheat system
                if board[play1H][play1V] == " O ":
                    player1.set_player2()
                    print(print_board(board))
                    print("No Cheating!!")
                    print("")
                else:
                    player1.set_player1()
                    print(print_board(board))

                if win(board) == None:
                    if nostalemate(board) == True:
                        # player 2 turn
                        play2H = int(input("Location of O vertical axis: "))
                        play2V = int(input("Location of O horizontal axis: "))
                        print("")
                        player2 = Player(play2H, play2V, board)

                        if board[play2H][play2V] == " X ":
                            player2.set_player1()
                            print(print_board(board))
                            print("No Cheating!!")
                            print("")
                        else:
                            player2.set_player2()
                            print(print_board(board))


                    else:
                        print("Stalemate")
                        print("")
                        clean_board(board)
                        print_board(board)
            else:
                print("Stalemate")
                print("")
                clean_board(board)
                print_board(board)
    return ""

# Play function
def play():
    global trials
    global progress
    global earthrune

    game = True
    while game == True:
        print("")
        gametype = input("To play story mode, type 1. To play PvP, press 2. To close game, press 3: ")
        if gametype == "1":
            print(story())
            print(inst())
            print(print_board(board))
            while progress == 0:
                trials += 1
                play1vboss1(board)
                print("Progress Saved")
            while progress == 1:
                trials += 1
                print(story())
                # empties board for new game
                clean_board(board)
                # begins second boss
                play1vboss2(board)
                print("Progress Saved")
            while progress == 2:
                trials += 1
                print(story())
                # clean
                clean_board(board)
                # 3rd boss
                play1vboss3(board)
                print("Progress Saved")
            while progress == 3:
                print(story())
                gunsmith()
                print("Progress Saved")
            while progress == 4:
                trials += 1
                clean_board(board)
                print(story())
                play1vboss4(board)
                print("Progress saved")
            while progress == 5:
                trials += 1
                clean_board(board)
                print(story())
                play1vfinal(board)
                print("Progress Saved")

            score_board()
            clean_board(board)
            trials = 0
            progress = 0
            earthrune = 0



        elif gametype == "2":
            play1v1()
        elif gametype == "3":
            print("")
            print("Game Closed")
            game = False
            return""

play()