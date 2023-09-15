import functools

import chess

m_squares = [chess.A5, chess.B5, chess.C5, chess.D5, chess.E5,
             chess.A4, chess.B4, chess.C4, chess.D4, chess.E4,
             chess.A3, chess.B3, chess.C3, chess.D3, chess.E3,
             chess.A2, chess.B2, chess.C2, chess.D2, chess.E2,
             chess.A1, chess.B1, chess.C1, chess.D1, chess.E1]

m_wpromotion = [chess.A5, chess.B5, chess.C5, chess.D5, chess.E5]

pawnEvalWhite = [
    0, 0, 0, 0, 0, 0, 0, 0,
    5, 10, 10, -20, -20, 10, 10, 5,
    5, -5, -10, 0, 0, -10, -5, 5,
    0, 0, 0, 20, 20, 0, 0, 0,
    5, 5, 10, 25, 25, 10, 5, 5,
    10, 10, 20, 30, 30, 20, 10, 10,
    50, 50, 50, 50, 50, 50, 50, 50,
    0, 0, 0, 0, 0, 0, 0, 0
]
pawnEvalBlack = list(reversed(pawnEvalWhite))

knightEval = [
    -50, -40, -30, -30, -30, -30, -40, -50,
    -40, -20, 0, 0, 0, 0, -20, -40,
    -30, 0, 10, 15, 15, 10, 0, -30,
    -30, 5, 15, 20, 20, 15, 5, -30,
    -30, 0, 15, 20, 20, 15, 0, -30,
    -30, 5, 10, 15, 15, 10, 5, -30,
    -40, -20, 0, 5, 5, 0, -20, -40,
    -50, -40, -30, -30, -30, -30, -40, -50
]

bishopEvalWhite = [
    -20, -10, -10, -10, -10, -10, -10, -20,
    -10, 5, 0, 0, 0, 0, 5, -10,
    -10, 10, 10, 10, 10, 10, 10, -10,
    -10, 0, 10, 10, 10, 10, 0, -10,
    -10, 5, 5, 10, 10, 5, 5, -10,
    -10, 0, 5, 10, 10, 5, 0, -10,
    -10, 0, 0, 0, 0, 0, 0, -10,
    -20, -10, -10, -10, -10, -10, -10, -20
]
bishopEvalBlack = list(reversed(bishopEvalWhite))

rookEvalWhite = [
    0, 0, 0, 5, 5, 0, 0, 0,
    -5, 0, 0, 0, 0, 0, 0, -5,
    -5, 0, 0, 0, 0, 0, 0, -5,
    -5, 0, 0, 0, 0, 0, 0, -5,
    -5, 0, 0, 0, 0, 0, 0, -5,
    -5, 0, 0, 0, 0, 0, 0, -5,
    5, 10, 10, 10, 10, 10, 10, 5,
    0, 0, 0, 0, 0, 0, 0, 0
]
rookEvalBlack = list(reversed(rookEvalWhite))

queenEval = [
    -20, -10, -10, -5, -5, -10, -10, -20,
    -10, 0, 0, 0, 0, 0, 0, -10,
    -10, 0, 5, 5, 5, 5, 0, -10,
    -5, 0, 5, 5, 5, 5, 0, -5,
    0, 0, 5, 5, 5, 5, 0, -5,
    -10, 5, 5, 5, 5, 5, 0, -10,
    -10, 0, 5, 0, 0, 0, 0, -10,
    -20, -10, -10, -5, -5, -10, -10, -20
]

kingEvalWhite = [
    20, 30, 10, 0, 0, 10, 30, 20,
    20, 20, 0, 0, 0, 0, 20, 20,
    -10, -20, -20, -20, -20, -20, -20, -10,
    20, -30, -30, -40, -40, -30, -30, -20,
    -30, -40, -40, -50, -50, -40, -40, -30,
    -30, -40, -40, -50, -50, -40, -40, -30,
    -30, -40, -40, -50, -50, -40, -40, -30,
    -30, -40, -40, -50, -50, -40, -40, -30
]
kingEvalBlack = list(reversed(kingEvalWhite))

kingEvalEndGameWhite = [
    50, -30, -30, -30, -30, -30, -30, -50,
    -30, -30, 0, 0, 0, 0, -30, -30,
    -30, -10, 20, 30, 30, 20, -10, -30,
    -30, -10, 30, 40, 40, 30, -10, -30,
    -30, -10, 30, 40, 40, 30, -10, -30,
    -30, -10, 20, 30, 30, 20, -10, -30,
    -30, -20, -10, 0, 0, -10, -20, -30,
    -50, -40, -30, -20, -20, -30, -40, -50
]
kingEvalEndGameBlack = list(reversed(kingEvalEndGameWhite))


def evaluate_piece_position(piece, square):
    piece_type = piece.piece_type
    mapping = []
    if piece_type == chess.PAWN:
        mapping = pawnEvalWhite if piece.color == chess.WHITE else pawnEvalBlack
    if piece_type == chess.KNIGHT:
        mapping = knightEval
    if piece_type == chess.BISHOP:
        mapping = bishopEvalWhite if piece.color == chess.WHITE else bishopEvalBlack
    if piece_type == chess.ROOK:
        mapping = rookEvalWhite if piece.color == chess.WHITE else rookEvalBlack
    if piece_type == chess.QUEEN:
        mapping = queenEval
    if piece_type == chess.KING:
        return 0
    return mapping[square]


def evaluate_piece(piece):
    if piece:
        piece_type = piece.piece_type
        if piece_type == chess.PAWN:
            return 100
        if piece_type == chess.KNIGHT:
            return 300
        if piece_type == chess.BISHOP:
            return 300
        if piece_type == chess.ROOK:
            return 600
        if piece_type == chess.QUEEN:
            return 900
        if piece_type == chess.KING:
            return 3000
    else:
        return 0


class State:
    def __init__(self, board, color, minichess):
        self.best_move = "0000"
        self.board = board
        self.color = color
        self.counter = 0
        self.minichess = minichess

    def get_ordered_moves(self):
        def orderer(move):
            return self.evaluate_move(move)

        moves = self.get_legal_moves()
        ordered_moves = sorted(moves, key=orderer, reverse=True)

        return ordered_moves

    def get_legal_moves(self):

        l_moves = self.board.legal_moves
        if not self.minichess:
            return l_moves
        else:
            m_moves = set()
            for move in l_moves:
                piece = self.board.piece_at(move.from_square)
                if move.to_square in m_squares and not self.board.is_en_passant(move):
                    if move.promotion is not None and move.promotion != chess.QUEEN:
                        move.promotion = chess.QUEEN
                    if move.to_square in m_wpromotion and piece.piece_type == chess.PAWN and piece.color == chess.WHITE:
                        move.promotion = chess.QUEEN
                    m_moves.add(move)
            return m_moves

    def evaluate_move(self, move) -> float:

        if move.promotion is not None:
            return float("inf")

        piece1 = self.board.piece_at(move.from_square)
        piece2 = self.board.piece_at(move.to_square)
        if piece1 and piece2:
            from_value = evaluate_piece(piece1)
            to_value = evaluate_piece(piece2)
            position_change = to_value - from_value
            return position_change
        elif piece1 and not self.minichess:
            from_value = evaluate_piece_position(piece1, move.from_square)
            to_value = evaluate_piece_position(piece1, move.to_square)
            position_change = to_value - from_value
            return position_change
        else:
            return 0

    def evaluate(self):
        value = 0

        white = self.board.occupied_co[chess.WHITE]
        black = self.board.occupied_co[chess.BLACK]

        whitep = 100 * chess.popcount(white & self.board.pawns) + 300 * chess.popcount(
            white & self.board.knights) + 300 * chess.popcount(white & self.board.bishops) + 500 * chess.popcount(
            white & self.board.rooks) + 900 * chess.popcount(white & self.board.queens)
        blackp = 100 * chess.popcount(black & self.board.pawns) + 300 * chess.popcount(
            black & self.board.knights) + 300 * chess.popcount(black & self.board.bishops) + 500 * chess.popcount(
            black & self.board.rooks) + 900 * chess.popcount(black & self.board.queens)

        if not self.minichess:
            for square in chess.SQUARES:
                piece = self.board.piece_at(square)
                if not piece:
                    continue
                if piece.color == chess.WHITE:
                    whitep = whitep + evaluate_piece_position(piece, square)
                if piece.color == chess.BLACK:
                    blackp = blackp + evaluate_piece_position(piece, square)

        if self.color:
            value = value + (whitep - blackp)

        if not self.color:
            value = value + (blackp - whitep)

        if self.board.is_stalemate() or self.board.is_fivefold_repetition():
            value = 0

        if self.board.is_checkmate():
            if not self.is_opponent_turn():
                value = -1000000
            else:
                value = 1000000
        else:
            if self.minichess and self.board.is_check():
                moves = self.get_legal_moves()
                if len(moves) == 0:
                    if not self.is_opponent_turn():
                        value = -1000000
                    else:
                        value = 1000000

        return value

    def make_best(self):
        self.board.push(self.best_move)

    def is_game_over(self):
        if not self.minichess:
            return self.board.is_game_over()
        else:
            moves = self.get_legal_moves()
            if len(moves) == 0:
                return True

    def is_opponent_turn(self):
        if self.color == self.board.turn:
            return False
        else:
            return True
