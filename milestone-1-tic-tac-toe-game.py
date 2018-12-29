import random
from IPython.display import clear_output

board = [0,1,2,3,4,5,6,7,8,9,10]
draw = [0,1,2,3,4,5,6,7,8,9]
player_one = ('X')
player_two = ('O')

def display_board(board): 
    
    print('     |     | ')
    print(' ', draw[7],' | ',draw[8],' | ',draw[9])
    print('     |     | ')
    print('----------------')
    print('     |     | ')
    print(' ', draw[4],' | ',draw[5],' | ',draw[6])
    print('     |     | ')
    print('----------------')
    print('     |     | ')
    print(' ', draw[1],' | ',draw[2],' | ',draw[3])
    print('     |     | ')
    
def player_input():

    players_rand = random.randint(0,1)

    for number in board:

        if number == 0:
            print('Welcome to Tic Tac Toe!')

                    
                    
        else:
            if players_rand == 0:

                def Player_1_lucky():

                    if number%2 != 0 and number != 10:
                        def Player_1_turn():
                            answer1 = int(input('Player 1, assign the marker: X, to the board using a number from 1 to 9: '))
                                        
                            if answer1 == 1 and draw[1] == ('X'):
                                print('You cannot use this place because it is already taken. Please pick another number.')
                                Player_1_turn()
                            elif answer1 == 1 and draw[1] == ('O'):
                                print('You cannot use this place because it is already taken. Please pick another number.')
                                Player_1_turn()
                            elif answer1 == board[1]:#
                                draw[1] = ('X')
                                display_board(board)
                            if answer1 == 2 and draw[2] == ('X'):
                                print('You cannot use this place because it is already taken. Please pick another number.')
                                Player_1_turn()
                            elif answer1 == 2 and draw[2] == ('O'): 
                                print('You cannot use this place because it is already taken. Please pick another number.')
                                Player_1_turn()
                            elif answer1 == board[2]:#
                                draw[2] = ('X')
                                display_board(board)
                            if answer1 == 3 and draw[3] == ('X'):
                                print('You cannot use this place because it is already taken. Please pick another number.')
                                Player_1_turn()
                            elif answer1 == 3 and draw[3] == ('O'): 
                                print('You cannot use this place because it is already taken. Please pick another number.')
                                Player_1_turn()
                            elif answer1 == board[3]:#
                                draw[3] = ('X')
                                display_board(board)
                            if answer1 == 4 and draw[4] == ('X'):
                                print('You cannot use this place because it is already taken. Please pick another number.')
                                Player_1_turn()
                            elif answer1 == 4 and draw[4] == ('O'): 
                                print('You cannot use this place because it is already taken. Please pick another number.')
                                Player_1_turn()
                            elif answer1 == board[4]:#
                                draw[4] = ('X')
                                display_board(board)
                            if answer1 == 5 and draw[5] == ('X'):
                                 print('You cannot use this place because it is already taken. Please pick another number.')
                                 Player_1_turn()
                            elif answer1 == 5 and draw[5] == ('O'): 
                                print('You cannot use this place because it is already taken. Please pick another number.')
                                Player_1_turn()
                            elif answer1 == board[5]:#
                                draw[5] = ('X')
                                display_board(board)
                            if answer1 == 6 and draw[6] == ('X'):
                                print('You cannot use this place because it is already taken. Please pick another number.')
                                Player_1_turn()
                            elif answer1 == 6 and draw[6] == ('O'): 
                                print('You cannot use this place because it is already taken. Please pick another number.')
                                Player_1_turn()
                            elif answer1 == board[6]:#
                                draw[6] = ('X')
                                display_board(board)
                            if answer1 == 7 and draw[7] == ('X'):
                                print('You cannot use this place because it is already taken. Please pick another number.')
                                Player_1_turn()
                            elif answer1 == 7 and draw[7] == ('O'): 
                                print('You cannot use this place because it is already taken. Please pick another number.')
                                player_1_turn()
                            elif answer1 == board[7]:#
                                draw[7] = ('X')
                                display_board(board)
                            if answer1 == 8 and draw[8] == ('X'):
                                print('You cannot use this place because it is already taken. Please pick another number.')
                                Player_1_turn()
                            elif answer1 == 8 and draw[8] == ('O'): 
                                print('You cannot use this place because it is already taken. Please pick another number.')
                                Player_1_turn()
                            elif answer1 == board[8]:#
                                draw[8] = ('X')
                                display_board(board)
                            if answer1 == 9 and draw[9] == ('X'):
                                print('You cannot use this place because it is already taken. Please pick another number.')
                                Player_1_turn()
                            elif answer1 == 9 and draw[9] == ('O'): 
                                print('You cannot use this place because it is already taken. Please pick another number.')
                                Player_1_turn()
                            elif answer1 == board[9]:#
                                draw[9] = ('X')
                                display_board(board)
                            #winning statements 
                            if draw[1] == draw[2] == draw[3] or draw[1] == draw[4] == draw[7] or draw[9] == draw[8] == draw[7] or draw[9] == draw[6] == draw[3] or draw[3] == draw[5] == draw[7] or draw[1] == draw[5] == draw[9] or draw[2] == draw[5] ==draw[8]:
                                print('Player 1, You have won the game!')
                                choice = input('Would you like to play again? [Y/N]')
                                if choice == ('Y'):
                                    draw[:] = [0,1,2,3,4,5,6,7,8,9] #This code can reset the draw string list
                                    display_board(board)
                                    player_input()
                                elif choice == ('N'):
                                    quit()

                        Player_1_turn()
                        
                                    
                    elif number%2 == 0 and number != 10:

                        def Player_2_turn():
                            answer2 = int(input('Player 2, assign the marker: O, to the board using a number from 1 to 9: '))
                                        
                            if answer2 == 1 and draw[1] == ('X'):
                                print('You cannot use this place because it is already taken. Please pick another number.')
                                Player_2_turn()
                            elif answer2 == 1 and draw[1] == ('O'): 
                                print('You cannot use this place because it is already taken. Please pick another number.')
                                Player_2_turn()
                            elif answer2 == board[1]:#
                                draw[1] = ('O')
                                display_board(board)
                            if answer2 == 2 and draw[2] == ('X'):
                                print('You cannot use this place because it is already taken. Please pick another number.')
                                Player_2_turn()
                            elif answer2 == 2 and draw[2] == ('O'): 
                                print('You cannot use this place because it is already taken. Please pick another number.')
                                Player_2_turn()
                            elif answer2 == board[2]:#
                                draw[2] = ('O')
                                display_board(board)
                            if answer2 == 3 and draw[3] == ('X'):
                                print('You cannot use this place because it is already taken. Please pick another number.')
                                Player_2_turn()
                            elif answer2 == 3 and draw[3] == ('O'): 
                                print('You cannot use this place because it is already taken. Please pick another number.')
                                Player_2_turn()
                            elif answer2 == board[3]:#
                                draw[3] = ('O')
                                display_board(board)
                            if answer2 == 4 and draw[4] == ('X'):
                                print('You cannot use this place because it is already taken. Please pick another number.')
                                Player_2_turn()
                            elif answer2 == 4 and draw[4] == ('O'): 
                                print('You cannot use this place because it is already taken. Please pick another number.')
                                Player_2_turn()
                            elif answer2 == board[4]:#
                                draw[4] = ('O')
                                display_board(board)
                            if answer2 == 5 and draw[5] == ('X'):
                                print('You cannot use this place because it is already taken. Please pick another number.')
                                Player_2_turn()
                            elif answer2 == 5 and draw[5] == ('O'): 
                                print('You cannot use this place because it is already taken. Please pick another number.')
                                Player_2_turn()
                            elif answer2 == board[5]:#
                                draw[5] = ('O')
                                display_board(board)
                            if answer2 == 6 and draw[6] == ('X'):
                                print('You cannot use this place because it is already taken. Please pick another number.')
                                Player_2_turn()
                            elif answer2 == 6 and draw[6] == ('O'): 
                                print('You cannot use this place because it is already taken. Please pick another number.')
                                Player_2_turn()
                            elif answer2 == board[6]:#
                                draw[6] = ('O')
                                display_board(board)
                            if answer2 == 7 and draw[7] == ('X'):
                                print('You cannot use this place because it is already taken. Please pick another number.')
                                Player_2_turn()
                            elif answer2 == 7 and draw[7] == ('O'): 
                                print('You cannot use this place because it is already taken. Please pick another number.')
                                Player_2_turn()
                            elif answer2 == board[7]:#
                                draw[7] = ('O')
                                display_board(board)
                            if answer2 == 8 and draw[8] == ('X'):
                                print('You cannot use this place because it is already taken. Please pick another number.')
                                Player_2_turn()
                            elif answer2 == 8 and draw[8] == ('O'): 
                                print('You cannot use this place because it is already taken. Please pick another number.')
                                Player_2_turn()
                            elif answer2 == board[8]:#
                                draw[8] = ('O')
                                display_board(board)
                            if answer2 == 9 and draw[9] == ('X'):
                                print('You cannot use this place because it is already taken. Please pick another number.')
                                Player_2_turn()
                            elif answer2 == 9 and draw[9] == ('O'): 
                                print('You cannot use this place because it is already taken. Please pick another number.')
                                Player_2_turn()
                            elif answer2 == board[9]:#
                                draw[9] = ('O')
                                display_board(board)
                            #winning statements
                            if draw[1] == draw[2] == draw[3] or draw[1] == draw[4] == draw[7] or draw[9] == draw[8] == draw[7] or draw[9] == draw[6] == draw[3] or draw[3] == draw[5] == draw[7] or draw[1] == draw[5] == draw[9] or draw[2] == draw[5] ==draw[8]:
                                print('Player 2, You have won the game!')
                                choice = input('Would you like to play again? [Y/N]')
                                if choice == ('Y'):
                                    draw[:] = [0,1,2,3,4,5,6,7,8,9] #This code can reset the draw string list
                                    display_board(board)
                                    player_input()
                                elif choice == ('N'):
                                    quit() 
           
                        Player_2_turn()

                Player_1_lucky()

            if players_rand == 1:
                def Player_2_lucky():

                    if number%2 == 0 and number != 10:
                        def Player_1_turn():
                            answer1 = int(input('Player 1, assign the marker: X, to the board using a number from 1 to 9: '))
                                        
                            if answer1 == 1 and draw[1] == ('X'):
                                print('You cannot use this place because it is already taken. Please pick another number.')
                                Player_1_turn()
                            elif answer1 == 1 and draw[1] == ('O'):
                                print('You cannot use this place because it is already taken. Please pick another number.')
                                Player_1_turn()
                            elif answer1 == board[1]:#
                                draw[1] = ('X')
                                display_board(board)
                            if answer1 == 2 and draw[2] == ('X'):
                                print('You cannot use this place because it is already taken. Please pick another number.')
                                Player_1_turn()
                            elif answer1 == 2 and draw[2] == ('O'): 
                                print('You cannot use this place because it is already taken. Please pick another number.')
                                Player_1_turn()
                            elif answer1 == board[2]:#
                                draw[2] = ('X')
                                display_board(board)
                            if answer1 == 3 and draw[3] == ('X'):
                                print('You cannot use this place because it is already taken. Please pick another number.')
                                Player_1_turn()
                            elif answer1 == 3 and draw[3] == ('O'): 
                                print('You cannot use this place because it is already taken. Please pick another number.')
                                Player_1_turn()
                            elif answer1 == board[3]:#
                                draw[3] = ('X')
                                display_board(board)
                            if answer1 == 4 and draw[4] == ('X'):
                                print('You cannot use this place because it is already taken. Please pick another number.')
                                Player_1_turn()
                            elif answer1 == 4 and draw[4] == ('O'): 
                                print('You cannot use this place because it is already taken. Please pick another number.')
                                Player_1_turn()
                            elif answer1 == board[4]:#
                                draw[4] = ('X')
                                display_board(board)
                            if answer1 == 5 and draw[5] == ('X'):
                                print('You cannot use this place because it is already taken. Please pick another number.')
                                Player_1_turn()
                            elif answer1 == 5 and draw[5] == ('O'): 
                                print('You cannot use this place because it is already taken. Please pick another number.')
                                Player_1_turn()
                            elif answer1 == board[5]:#
                                draw[5] = ('X')
                                display_board(board)
                            if answer1 == 6 and draw[6] == ('X'):
                                print('You cannot use this place because it is already taken. Please pick another number.')
                                Player_1_turn()
                            elif answer1 == 6 and draw[6] == ('O'): 
                                print('You cannot use this place because it is already taken. Please pick another number.')
                                Player_1_turn()
                            elif answer1 == board[6]:#
                                draw[6] = ('X')
                                display_board(board)
                            if answer1 == 7 and draw[7] == ('X'):
                                print('You cannot use this place because it is already taken. Please pick another number.')
                                Player_1_turn()
                            elif answer1 == 7 and draw[7] == ('O'): 
                                print('You cannot use this place because it is already taken. Please pick another number.')
                                player_1_turn()
                            elif answer1 == board[7]:#
                                draw[7] = ('X')
                                display_board(board)
                            if answer1 == 8 and draw[8] == ('X'):
                                print('You cannot use this place because it is already taken. Please pick another number.')
                                Player_1_turn()
                            elif answer1 == 8 and draw[8] == ('O'): 
                                print('You cannot use this place because it is already taken. Please pick another number.')
                                Player_1_turn()
                            elif answer1 == board[8]:#
                                draw[8] = ('X')
                                display_board(board)
                            if answer1 == 9 and draw[9] == ('X'):
                                print('You cannot use this place because it is already taken. Please pick another number.')
                                Player_1_turn()
                            elif answer1 == 9 and draw[9] == ('O'): 
                                print('You cannot use this place because it is already taken. Please pick another number.')
                                Player_1_turn()
                            elif answer1 == board[9]:#
                                draw[9] = ('X')
                                display_board(board)
                            #winning statements 
                            if draw[1] == draw[2] == draw[3] or draw[1] == draw[4] == draw[7] or draw[9] == draw[8] == draw[7] or draw[9] == draw[6] == draw[3] or draw[3] == draw[5] == draw[7] or draw[1] == draw[5] == draw[9] or draw[2] == draw[5] ==draw[8]:
                                print('Player 1, You have won the game!')
                                choice = input('Would you like to play again? [Y/N]')
                                if choice == ('Y'):
                                    draw[:] = [0,1,2,3,4,5,6,7,8,9] #This code can reset the draw string list
                                    display_board(board)
                                    player_input()
                                elif choice == ('N'):
                                    quit()


                        Player_1_turn()
                                    
                    elif number%2 != 0 and number != 10:

                        def Player_2_turn():
                            answer2 = int(input('Player 2, assign the marker: O, to the board using a number from 1 to 9: '))
                                                            
                            if answer2 == 1 and draw[1] == ('X'):
                                print('You cannot use this place because it is already taken. Please pick another number.')
                                Player_2_turn()
                            elif answer2 == 1 and draw[1] == ('O'): 
                                print('You cannot use this place because it is already taken. Please pick another number.')
                                Player_2_turn()
                            elif answer2 == board[1]:#
                                draw[1] = ('O')
                                display_board(board)
                            if answer2 == 2 and draw[2] == ('X'):
                                print('You cannot use this place because it is already taken. Please pick another number.')
                                Player_2_turn()
                            elif answer2 == 2 and draw[2] == ('O'): 
                                print('You cannot use this place because it is already taken. Please pick another number.')
                                Player_2_turn()
                            elif answer2 == board[2]:#
                                draw[2] = ('O')
                                display_board(board)
                            if answer2 == 3 and draw[3] == ('X'):
                                print('You  use this place because it is already taken. Please pick another number.')
                                Player_2_turn()
                            elif answer2 == 3 and draw[3] == ('O'): 
                                print('You cannot use this place because it is already taken. Please pick another number.')
                                Player_2_turn()
                            elif answer2 == board[3]:#
                                draw[3] = ('O')
                                display_board(board)
                            if answer2 == 4 and draw[4] == ('X'):
                                print('You cannot use this place because it is already taken. Please pick another number.')
                                Player_2_turn()
                            elif answer2 == 4 and draw[4] == ('O'): 
                                print('You cannot use this place because it is already taken. Please pick another number.')
                                Player_2_turn()
                            elif answer2 == board[4]:#
                                draw[4] = ('O')
                                display_board(board)
                            if answer2 == 5 and draw[5] == ('X'):
                                print('You cannot use this place because it is already taken. Please pick another number.')
                                Player_2_turn()
                            elif answer2 == 5 and draw[5] == ('O'): 
                                print('You cannot use this place because it is already taken. Please pick another number.')
                                Player_2_turn()
                            elif answer2 == board[5]:#
                                draw[5] = ('O')
                                display_board(board)
                            if answer2 == 6 and draw[6] == ('X'):
                                print('You cannot use this place because it is already taken. Please pick another number.')
                                Player_2_turn()
                            elif answer2 == 6 and draw[6] == ('O'): 
                                print('You cannot use this place because it is already taken. Please pick another number.')
                                Player_2_turn()
                            elif answer2 == board[6]:#
                                draw[6] = ('O')
                                display_board(board)
                            if answer2 == 7 and draw[7] == ('X'):
                                print('You cannot use this place because it is already taken. Please pick another number.')
                                Player_2_turn()
                            elif answer2 == 7 and draw[7] == ('O'): 
                                print('You cannot use this place because it is already taken. Please pick another number.')
                                Player_2_turn()
                            elif answer2 == board[7]:#
                                draw[7] = ('O')
                                display_board(board)
                            if answer2 == 8 and draw[8] == ('X'):
                                print('You cannot use this place because it is already taken. Please pick another number.')
                                Player_2_turn()
                            elif answer2 == 8 and draw[8] == ('O'): 
                                print('You cannot use this place because it is already taken. Please pick another number.')
                                Player_2_turn()
                            elif answer2 == board[8]:#
                                draw[8] = ('O')
                                display_board(board)
                            if answer2 == 9 and draw[9] == ('X'):
                                print('You cannot use this place because it is already taken. Please pick another number.')
                                Player_2_turn()
                            elif answer2 == 9 and draw[9] == ('O'): 
                                print('You cannot use this place because it is already taken. Please pick another number.')
                                Player_2_turn()
                            elif answer2 == board[9]:#
                                draw[9] = ('O')
                                display_board(board)
                            #winning statements 
                            if draw[1] == draw[2] == draw[3] or draw[1] == draw[4] == draw[7] or draw[9] == draw[8] == draw[7] or draw[9] == draw[6] == draw[3] or draw[3] == draw[5] == draw[7] or draw[1] == draw[5] == draw[9] or draw[2] == draw[5] ==draw[8]:
                                print('Player 2, You have won the game!')
                                choice = input('Would you like to play again? [Y/N]')
                                if choice == ('Y'):
                                    draw[:] = [0,1,2,3,4,5,6,7,8,9] #This code can reset the draw string list
                                    display_board(board)
                                    player_input()
                                elif choice == ('N'):
                                    quit()


                        Player_2_turn()

                Player_2_lucky()

            elif number == 10:
                finalchoice = input('It seems nobody has won the game. Would you like to play again? [Y/N]')

                if finalchoice == ('Y'):
                    draw[:] = [0,1,2,3,4,5,6,7,8,9] #This code can reset the draw string list
                    display_board(board)
                    player_input()
                elif choice == ('N'):
                    quit()  

display_board(board)
player_input()
        
