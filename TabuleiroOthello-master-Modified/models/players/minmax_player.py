infinity = 1000000

class MinimaxPlayer:
    
    def __init__(self, color):
        self.color = color
        
    def play(self, board):
        return self.minimax(board, 5, self.edge_eval)[1]
    

    def minimax_value(self, board, depth, eval):

        if depth == 0 or not board.ison:
            return eval(board)

        best = 0

        for move in board.valid_moves(self.color):
            g = board.get_clone()
            g.play(move, self.color)

            val = -1 * self.minimax_value(g, depth-1, eval)
            if best is 0 or val > best:
                best = val
        return best

    def minimax(self, board, depth, eval):

        best = 0

        for move in board.valid_moves(self.color):
            g = board.get_clone()
            g.play(move, self.color)

            val = -1 * self.minimax_value(g, depth, eval)

            if best is 0 or val > best[0]:
                best = (val, move)

        return best

    def edge_eval(self, board):
        '''preferencia por cantos'''
        import math
        corners = [[1,1],[1,8], [8,1], [8,8]]

        other_player = board._opponent(self.color)
        score = 0
        for i in range(8):
            for j in range(8):
                delta = 1
                if i == 0 or i == 7:
                    delta += 5
                if j == 0 or j == 7:
                    delta += 5

                if i == 1 or i == 6:
                    delta -= 5
                if j == 1 or j == 6:
                    delta -= 5

                for corner in corners:
                    distX = abs(corner[0] - i)
                    distY = abs(corner[1] - j)
                    dist  = math.sqrt(distX*distX + distY*distY)
                    if dist < 4:
                        delta += 3

                if board.get_square_color(i, j) == self.color:
                    score += delta
                elif board.get_square_color(i, j) == other_player:
                    score -= delta

        return score
