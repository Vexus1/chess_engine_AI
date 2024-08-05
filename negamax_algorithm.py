from random import choice

import chess
from chess import Piece, Board, Move
from icecream import ic

from ai_timer import time_it, sum_time

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
        return values_map[piece.piece_type]
      
    @property
    def evaluate_board(self) -> int:
        '''Calculates current pieces power from white's perspective'''
        curr_power = []
        for piece in self.board.piece_map().values():
            if piece.color == chess.WHITE:
                curr_power.append(-self.pieces_value(piece))
            else:
                curr_power.append(self.pieces_value(piece))
        return sum(curr_power)
        
    def negamax(self, depth: int, alpha: int, beta: int, color: int) -> int:
        '''This algorithm relies on the fact that: min(a,b) = -max(-b,-a)
           to simplify the implementation of the minimax algorithm'''
        if depth == 0 or self.board.is_game_over():
            return color * self.evaluate_board
        max_eval = float('-inf')
        for move in self.board.legal_moves:
            self.board.push(move)
            eval = -self.negamax(depth - 1, -beta, -alpha, -color)
            self.board.pop()
            max_eval = max(max_eval, eval)
            alpha = max(alpha, eval)
            if alpha >= beta:
                break
        return max_eval

    @time_it
    def decision_function(self, depth: int) -> Move:
        best_move = None
        best_value = float('-inf')
        alpha = float('-inf')
        beta = float('inf')
        for move in self.board.legal_moves:
            self.board.push(move)
            board_value = -self.negamax(depth - 1, -beta, -alpha, -1)
            self.board.pop()
            if board_value > best_value:
                best_value = board_value
                best_move = move
            alpha = max(alpha, board_value)
        return best_move
   
    @property
    def possible_moves(self) -> tuple[str]:
        moves = tuple(map(str, list(self.board.legal_moves)))
        return moves
    
    @property
    def decision_tree_depth(self) -> int:
        '''Determines the depth of the decision tree for the Min-Max algorithm.'''
        return 4  
    
    @property
    def player(self) -> str:
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
    def random_agent(self) -> str:
        move = choice(self.possible_moves)
        print()
        print(f'Random move: {move}')
        print()
        return choice(self.possible_moves)
    
    def move(self) -> None:
        print(self.board)
        print()
        if self.board.turn == chess.WHITE:
            # move = self.player
            move = self.random_agent
            move = chess.Move.from_uci(str(move))
            self.board.push(move)
        else:
            best_move = self.decision_function(self.decision_tree_depth)
            self.board.push(best_move)
            print(f'AI move: {best_move}')
            print()
        