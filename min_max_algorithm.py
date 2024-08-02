from random import choice

import chess
from chess import Piece, Board, Move
from icecream import ic

class ChessAi:
    def __init__(self, board: Board):
        self.board = board

    def pieces_value(self, piece: Piece) -> int:
        values_map = {chess.PAWN: 1,
                      chess.KNIGHT: 3,
                      chess.BISHOP: 3,
                      chess.ROOK: 5,
                      chess.QUEEN: 9,
                      chess.KING: 0}
        if piece.color == chess.WHITE:
            sign = -1
        else:
            sign = 1
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
            board_value = max(best_value, self.min_max(depth - 1, False))
            self.board.pop()
            if board_value > best_value:
                best_value = board_value
                best_move = move
        return best_move
    
    @property
    def possible_moves(self) -> tuple[str]:
        moves = tuple(map(str, list(self.board.legal_moves)))
        return moves
    
    @property
    def decision_tree_depth(self) -> int:
        """
        Determines the depth of the decision tree for the Min-Max algorithm.

        The depth parameter in the Min-Max algorithm represents how many levels ahead
        the algorithm should evaluate possible moves in the game tree. Each level in the
        tree corresponds to a ply, which is a half-move in chess (one move by either player).

        A greater depth allows the algorithm to consider more future possibilities,
        leading to potentially stronger and more strategic moves. However, increasing the
        depth also exponentially increases the number of positions that must be evaluated,
        which requires more computational resources and time.

        For instance, a depth of 3 means the algorithm will look ahead 3 plies (or 1.5 moves)
        into the future, evaluating the consequences of the current move, the opponent's
        response, and the subsequent move by the player. While this provides a moderate level
        of foresight, deeper searches (e.g., 5 or 7 plies) can significantly improve the quality
        of decisions at the cost of increased computational effort.

        It is crucial to balance depth with available computational resources to ensure the AI
        performs optimally without excessive delays, especially in interactive settings.

        Returns:
            int: The depth of the decision tree used by the Min-Max algorithm.
        """
        return 3  # Example fixed depth; in practice, this could be set dynamically
    
    def player_move(self) -> str:
        while True:
            move = input('Enter your move: ')
            if move not in self.possible_moves:
                print('Move is not possible!')
                print()
                print(self.board)
                print()
                print('Possible moves:')
                print()
                print(self.possible_moves)
            else:
                return move
            
    @property
    def random_agent(self):
        move = choice(self.possible_moves)
        print()
        print(f'Random move: {move}')
        print()
        return choice(self.possible_moves)
    
    def move(self) -> None:
        print(self.board)
        print()
        if self.board.turn == chess.WHITE:
            move = self.player_move()
            # move = self.random_agent
            move = chess.Move.from_uci(str(move))
            self.board.push(move)
        else:
            best_move = self.decision_function(self.decision_tree_depth)
            self.board.push(best_move)
            print(f'AI move: {best_move}')
            print()
        