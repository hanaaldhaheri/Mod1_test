board = ["1","2","3","4","5","6","7","8","9"]
#assign the 9 grid board
players=["X","O"]
# players will be either X or O
player_turn=0

# to create infinite loop
while True:
    print(board[0],board[1],board[2])
    print(board[3],board[4],board[5])
    print(board[6],board[7],board[8])
    

    move = int(input(f"{players[player_turn]} Choose:"))- 1
    board[move]= players[player_turn]
# move is asking an interger from the players so when player is choosing 1 it will put in 0.

    if (
        board[0]==board[1]==board[2] or board[3]==board[4]==board[5] or board[6]== board[7]== board[8] or
        board[0]==board[3]==board[6] or board[1]==board[4]==board[7] or board[2]== board[5]== board[8] or
        board[0]==board[4]==board[8] or board[2]==board[4]==board[6]
    ):
        print(f"players{player_turn + 1}({players[player_turn]}),wins!")
        break

    if all(pos in players for pos in board):
        print("It's a draw!")
        break
    player_turn = (player_turn + 1) % 2


    # I added the winning combination , also added print if any of the player win it will display 1 or 2.
    # If all the position is filled then it will be draw.
    


