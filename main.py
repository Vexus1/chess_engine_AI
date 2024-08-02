import chess

from min_max_algorithm import ChessAi

board = chess.Board()
chess_ai = ChessAi(board)

def run_game() -> None:
    while True:
        chess_ai.move()
        if chess_ai.board.is_game_over():
            print('Game over')
            break   

if __name__ == '__main__':
    run_game()
