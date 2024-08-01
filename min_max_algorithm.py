import chess
from chess import Piece, Board, Move

class ChessAi:
    def __init__(self, board: Board):
        self.board = board

    def pieces_value(self, piece: Piece) -> int:
        '''sign == 1 -> WHITE, sign == -1 -> BLACK'''
        values_map = {chess.PAWN: 1,
                      chess.KNIGHT: 3,
                      chess.BISHOP: 3,
                      chess.ROOK: 5,
                      chess.QUEEN: 9,
                      chess.KING: 0}
        if piece.color == chess.WHITE:
            sign = 1
        else:
            sign = -1
        return sign * values_map[piece.piece_type]

    @property
    def evaluate_board(self) -> int:
        '''Calculates current pieces power'''
        curr_power = sum([self.pieces_value(piece)
                          for piece in self.board.piece_map().values()])
        return curr_power

    def min_max(self, depth: int, is_maximizing: bool) -> int:
        if depth == 0 or self.board.is_game_over():
            return self.evaluate_board
        if is_maximizing:
            max_eval = float('-inf')
            for move in self.board.legal_moves:
                self.board.push(move)
                eval = self.min_max(depth - 1, False)
                self.board.pop()
                max_eval = max(max_eval, eval)
            return max_eval
        else:
            min_eval = float('inf')
            for move in self.board.legal_moves:
                self.board.push(move)
                eval = self.min_max(depth - 1, True)
                self.board.pop()
                min_eval = min(min_eval, eval)
            return min_eval

    def decision_function(self, depth: int) -> Move:
        best_move = None
        best_value = float('-inf')
        for move in self.board.legal_moves:
            self.board.push(move)
            board_value = self.min_max(depth - 1, False)
            self.board.pop()
            if board_value > best_value:
                best_value = board_value
                best_move = move
        return best_move

    def play(self) -> None:
        while True:
            print(self.board)
            print()
            if self.board.turn == chess.WHITE:
                move = input('Enter your move: ')
                self.board.push_san(move)
            else:
                best_move = self.decision_function(3)
                self.board.push(best_move)
                print(f'AI move: {best_move}')
                print()
            if self.board.is_game_over():
                print('Game over')
                break
