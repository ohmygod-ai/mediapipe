#輸出文字：你好
print("你好")
#井字遊戲
board = [' ' for _ in range(9)]  # 使用一個列表來表示井字遊戲的棋盤
def print_board():
    for i in range(3):
        print("|".join(board[i*3:(i+1)*3]))
        if i < 2:
            print("-----")  
def check_winner(player):
    win_conditions = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # 橫向
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # 縱向
        [0, 4, 8], [2, 4, 6]              # 對角線
    ]
    for condition in win_conditions:
        if all(board[i] == player for i in condition):
            return True
    return False            
def is_draw():
    return all(space != ' ' for space in board)     
def tic_tac_toe():
    current_player = 'X'
    while True:
        print_board()
        move = int(input(f"玩家 {current_player}，請輸入你的移動位置 (0-8): "))
        if board[move] == ' ':
            board[move] = current_player
            if check_winner(current_player):
                print_board()
                print(f"玩家 {current_player} 獲勝!")
                break
            if is_draw():
                print_board()
                print("遊戲平局!")
                break
            current_player = 'O' if current_player == 'X' else 'X'
        else:
            print("該位置已被佔用，請選擇其他位置。")
tic_tac_toe()   