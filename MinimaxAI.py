import chess
from math import inf


class MinimaxAI():
    """
    piade sazi be komake in video dar youtube :https://www.youtube.com/watch?v=l-hh51ncgDI
    """

    def __init__(self,huristic,depth):
        self.depth = depth
        self.huristic = huristic
        self.deep = (depth % 2 == 0)

    def choose_move(self, board):
        positions = list(board.legal_moves)

        final_round = None
        final_value = float('-inf')

        for p in positions:
            board.push(p)
            movement = self.min_chooser(0, board)
            board.pop()

            if movement > final_value:
                final_value = movement
                final_round = p

        print("score is {}".format(final_value))
        print("Movement based on MinimaxAI {} ".format(final_round))
        return final_round

    def max_chooser(self, depth, board):

        if self.gameover(depth, board):
            return self.huristic(board, self.deep)

        maxEval = float('-inf')
        for position in board.legal_moves:
            board.push(position)
            maxEval = max(maxEval, self.min_chooser(depth + 1, board))
            board.pop()

        return maxEval

    def min_chooser(self, depth, board):
        if self.gameover(depth, board):
            return self.huristic(board, self.deep)

        minEval = float('inf')
        for position in board.legal_moves:
            board.push(position)
            minEval = min(minEval, self.max_chooser(depth + 1, board))
            board.pop()

        return minEval

    def gameover(self, depth, board):
        return self.depth <= depth or board.is_game_over()

    def change(self):
        self.deep = (self.depth % 2 == 0)
