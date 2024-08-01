import chess

from min_max_algorithm import ChessAi

board = chess.Board()
chess_ai = ChessAi(board)

if __name__ == '__main__':
    chess_ai.play()
