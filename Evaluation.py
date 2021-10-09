import chess

"""
implemented using this article: https://www.chessprogramming.org/Evaluation
"""

KQRBNP = {"pawn": 1, "knight": 3, "bishop": 3, "rook": 5, "queen": 9, "king": 200}


def materialscore(board, depth_fix):
    w_pawns = len(board.pieces(chess.PAWN, chess.WHITE))
    w_knights = len(board.pieces(chess.KNIGHT, chess.WHITE))
    w_bishops = len(board.pieces(chess.BISHOP, chess.WHITE))
    w_rooks = len(board.pieces(chess.ROOK, chess.WHITE))
    w_queens = len(board.pieces(chess.QUEEN, chess.WHITE))
    w_kings = len(board.pieces(chess.KING, chess.WHITE))

    b_pawns = len(board.pieces(chess.PAWN, chess.BLACK))
    b_knights = len(board.pieces(chess.KNIGHT, chess.BLACK))
    b_bishops = len(board.pieces(chess.BISHOP, chess.BLACK))
    b_rooks = len(board.pieces(chess.ROOK, chess.BLACK))
    b_queens = len(board.pieces(chess.QUEEN, chess.BLACK))
    b_kings = len(board.pieces(chess.KING, chess.BLACK))

    materialscore = (w_pawns - b_pawns) * KQRBNP["pawn"]
    materialscore += (w_knights - b_knights) * KQRBNP["knight"]
    materialscore += (w_bishops - b_bishops) * KQRBNP["bishop"]
    materialscore += (w_rooks - b_rooks) * KQRBNP["rook"]
    materialscore += (w_queens - b_queens) * KQRBNP["queen"]
    materialscore += (w_kings - b_kings) * KQRBNP["king"]

    if board.turn == chess.BLACK:
        materialscore *= -1

    if depth_fix:
        materialscore *= -1

    return materialscore
