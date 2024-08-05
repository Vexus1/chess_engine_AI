import chess

from negamax_algorithm import ChessAi, sum_time
# from game_statistic import time_multiple_games, games_time, GAMES_PLAYED

# @time_multiple_games # to rework, if not testing set GAMES_PLAYED = 1
def run_game() -> None:  
    board = chess.Board()
    chess_ai = ChessAi(board)
    while True:
        chess_ai.move()
        if chess_ai.board.is_game_over():
            print(f'Depth of negamax alogrithm: {chess_ai.decision_tree_depth}')
            print(f'Sum of times taken for AI move: {sum(sum_time):.4f} '
                  f'seconds in {len(sum_time)} moves')
            print(f'Avarage time for AI move: {sum(sum_time)/len(sum_time):.4f} seconds')
            print('Game over')
            break   

if __name__ == '__main__':
    run_game()
    # print(f'Avarage time for {GAMES_PLAYED} games: '
    #       f'{sum(games_time)/GAMES_PLAYED:.4f} seconds')
