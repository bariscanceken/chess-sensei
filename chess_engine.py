#Chess Engine

class game_state():
    def __init__(self):
        self.board = [ 
            ["bR","bN","bB","bQ","bK","bB","bN","bR"],
            ["bp","bp","bp","bp","bp","bp","bp","bp"],
            ["--","--","--","--","--","--","--","--"],
            ["--","--","--","--","--","--","--","--"],
            ["--","--","--","--","--","--","--","--"],
            ["--","--","--","--","--","--","--","--"],
            ["wp","wp","wp","wp","wp","wp","wp","wp"],
            ["wR","wN","wB","wQ","wK","wB","wN","wR"]]
        self.whiteToMove = True
        self.moveLog = []

    def valid_moves(self,r,c):
        material = self.board[r][c]
        valid_moves = []

        if material == "wp":

            if self.board[r-1][c] == "--":
                valid_moves.append((r-1,c))
            if r == 6 and self.board[r-2][c] == "--":
                if self.board[r-1][c] == "--":
                    valid_moves.append((r-2,c))
            if c > 0 :
                if self.board[r-1][c-1] in ["bp","bB","bN","bR","bQ","bK"]:
                    valid_moves.append((r-1,c-1)) 
            if c < 7:
                if self.board[r-1][c+1] in ["bp","bB","bN","bR","bQ","bK"]:
                    valid_moves.append((r-1,c+1))

        
                

        if material == "bp":

            if self.board[r+1][c] == "--":
                valid_moves.append((r+1, c))
            if r == 1 and self.board[r+2][c] == "--":
                if self.board[r+1][c] == "--":
                    valid_moves.append((r+2, c))
            if c > 0:
                if self.board[r+1][c-1] in ["wp", "wB", "wN", "wR", "wQ", "wK"]:
                    valid_moves.append((r+1, c-1))
            if c < 7:
                if self.board[r+1][c+1] in ["wp", "wB", "wN", "wR", "wQ", "wK"]:
                    valid_moves.append((r+1, c+1))
                    

        if material == "wR":
            for i in range(r-1,-1,-1):
                if self.board[i][c] == "--":
                    valid_moves.append((i,c))
                elif self.board[i][c] in ["bp","bB","bN","bR","bQ","bK"]:
                    valid_moves.append((i,c))
                    break                    
                else:
                    break
            for i in range(r+1,8):
                if self.board[i][c] == "--":
                    valid_moves.append((i,c))
                elif self.board[i][c] in ["bp","bB","bN","bR","bQ","bK"]:
                    valid_moves.append((i,c))
                    break                    
                else:
                    break
            for i in range(c-1,-1,-1):
                if self.board[r][i] == "--":
                    valid_moves.append((r,i))
                elif self.board[r][i] in ["bp","bB","bN","bR","bQ","bK"]:
                    valid_moves.append((r,i))
                    break                    
                else:
                    break
            for i in range(c+1,8):
                if self.board[r][i] == "--":
                    valid_moves.append((r,i))
                elif self.board[r][i] in ["bp","bB","bN","bR","bQ","bK"]:
                    valid_moves.append((r,i))
                    break                    
                else:
                    break

        if material == "bR":

            for i in range(r-1,-1,-1):
                if self.board[i][c] == "--":
                    valid_moves.append((i,c))
                elif self.board[i][c] in ["wp","wB","wN","wR","wQ","wK"]:
                    valid_moves.append((i,c))
                    break                    
                else:
                    break
            for i in range(r+1,8):
                if self.board[i][c] == "--":
                    valid_moves.append((i,c))
                elif self.board[i][c] in ["wp","wB","wN","wR","wQ","wK"]:
                    valid_moves.append((i,c))
                    break                    
                else:
                    break
            for i in range(c-1,-1,-1):
                if self.board[r][i] == "--":
                    valid_moves.append((r,i))
                elif self.board[r][i] in ["wp","wB","wN","wR","wQ","wK"]:
                    valid_moves.append((r,i))
                    break                    
                else:
                    break
            for i in range(c+1,8):
                if self.board[r][i] == "--":
                    valid_moves.append((r,i))
                elif self.board[r][i] in ["wp","wB","wN","wR","wQ","wK"]:
                    valid_moves.append((r,i))
                    break                    
                else:
                    break

        if material == "wN":
            possible_moves = [
            (r - 2, c - 1), (r - 2, c + 1),
            (r - 1, c - 2), (r - 1, c + 2),
            (r + 1, c - 2), (r + 1, c + 2),
            (r + 2, c - 1), (r + 2, c + 1)]

            for row,col in possible_moves:
                if 0 <= row <= 7 and 0 <= col <= 7:
                    target_square = self.board[row][col]
                    if target_square == "--" or target_square[0] == 'b':
                        valid_moves.append((row,col))

        if material == "bN":
            possible_moves = [
            (r - 2, c - 1), (r - 2, c + 1),
            (r - 1, c - 2), (r - 1, c + 2),
            (r + 1, c - 2), (r + 1, c + 2),
            (r + 2, c - 1), (r + 2, c + 1)]

            for row,col in possible_moves:
                if 0 <= row <= 7 and 0 <= col <= 7:
                    target_square = self.board[row][col]
                    if target_square == "--" or target_square[0] == 'w':
                        valid_moves.append((row,col))


        if material == "wB":
            possible_moves = []
            directions = [(-1, -1), (-1, 1), (1, -1), (1, 1)]
            
            for direction in directions:
                row, col = r, c
                while True:
                    row += direction[0]
                    col += direction[1]
                    
                    if 0 <= row <= 7 and 0 <= col <= 7:
                        target_square = self.board[row][col]
                        
                        if target_square == "--":
                            possible_moves.append((row, col))
                        elif target_square[0] == "b":
                            possible_moves.append((row, col))
                            break
                        else:
                            break
                    else:
                        break

            for move in possible_moves:
                row, col = move
                valid_moves.append((row, col))
        
        if material == "bB":
            possible_moves = []
            directions = [(-1, -1), (-1, 1), (1, -1), (1, 1)]
            
            for direction in directions:
                row, col = r, c
                while True:
                    row += direction[0]
                    col += direction[1]
                    
                    if 0 <= row <= 7 and 0 <= col <= 7:
                        target_square = self.board[row][col]
                        
                        if target_square == "--":
                            possible_moves.append((row, col))
                        elif target_square[0] == "w":
                            possible_moves.append((row, col))
                            break
                        else:
                            break
                    else:
                        break

            for move in possible_moves:
                row, col = move
                valid_moves.append((row, col))

        if material == "wQ":
            possible_moves = []
            directions = [(-1, -1), (-1, 1), (1, -1), (1, 1)]
            
            for direction in directions:
                row, col = r, c
                while True:
                    row += direction[0]
                    col += direction[1]
                    
                    if 0 <= row <= 7 and 0 <= col <= 7:
                        target_square = self.board[row][col]
                        
                        if target_square == "--":
                            possible_moves.append((row, col))
                        elif target_square[0] == "b":
                            possible_moves.append((row, col))
                            break
                        else:
                            break
                    else:
                        break

            for move in possible_moves:
                row, col = move
                valid_moves.append((row, col))

            for i in range(r-1,-1,-1):
                if self.board[i][c] == "--":
                    valid_moves.append((i,c))
                elif self.board[i][c] in ["bp","bB","bN","bR","bQ","bK"]:
                    valid_moves.append((i,c))
                    break                    
                else:
                    break
            for i in range(r+1,8):
                if self.board[i][c] == "--":
                    valid_moves.append((i,c))
                elif self.board[i][c] in ["bp","bB","bN","bR","bQ","bK"]:
                    valid_moves.append((i,c))
                    break                    
                else:
                    break
            for i in range(c-1,-1,-1):
                if self.board[r][i] == "--":
                    valid_moves.append((r,i))
                elif self.board[r][i] in ["bp","bB","bN","bR","bQ","bK"]:
                    valid_moves.append((r,i))
                    break                    
                else:
                    break
            for i in range(c+1,8):
                if self.board[r][i] == "--":
                    valid_moves.append((r,i))
                elif self.board[r][i] in ["bp","bB","bN","bR","bQ","bK"]:
                    valid_moves.append((r,i))
                    break                    
                else:
                    break
        
        if material == "bQ":
            possible_moves = []
            directions = [(-1, -1), (-1, 1), (1, -1), (1, 1)]
            
            for direction in directions:
                row, col = r, c
                while True:
                    row += direction[0]
                    col += direction[1]
                    
                    if 0 <= row <= 7 and 0 <= col <= 7:
                        target_square = self.board[row][col]
                        
                        if target_square == "--":
                            possible_moves.append((row, col))
                        elif target_square[0] == "w":
                            possible_moves.append((row, col))
                            break
                        else:
                            break
                    else:
                        break

            for move in possible_moves:
                row, col = move
                valid_moves.append((row, col))

            for i in range(r-1,-1,-1):
                if self.board[i][c] == "--":
                    valid_moves.append((i,c))
                elif self.board[i][c] in ["wp","wB","wN","wR","wQ","wK"]:
                    valid_moves.append((i,c))
                    break                    
                else:
                    break
            for i in range(r+1,8):
                if self.board[i][c] == "--":
                    valid_moves.append((i,c))
                elif self.board[i][c] in ["wp","wB","wN","wR","wQ","wK"]:
                    valid_moves.append((i,c))
                    break                    
                else:
                    break
            for i in range(c-1,-1,-1):
                if self.board[r][i] == "--":
                    valid_moves.append((r,i))
                elif self.board[r][i] in ["wp","wB","wN","wR","wQ","wK"]:
                    valid_moves.append((r,i))
                    break                    
                else:
                    break
            for i in range(c+1,8):
                if self.board[r][i] == "--":
                    valid_moves.append((r,i))
                elif self.board[r][i] in ["wp","wB","wN","wR","wQ","wK"]:
                    valid_moves.append((r,i))
                    break                    
                else:
                    break
        

        if material == "wK":
            possible_moves = [
                (r+1,c-1),(r+1,c),(r+1,c+1),
                (r,c-1),(r,c+1),
                (r-1,c-1),(r-1,c),(r-1,c+1)
            ]

            for r,c in possible_moves:
                 if 0 <= r <= 7 and 0 <= c <= 7:
                    target_square = self.board[r][c]
                    if self.board[r][c] == "--":
                        valid_moves.append((r,c))
                    elif self.board[r][c] in ["bp","bB","bN","bR","bQ","bK"]:
                        valid_moves.append((r,c))

        if material == "bK":
            possible_moves = [
                (r+1,c-1),(r+1,c),(r+1,c+1),
                (r,c-1),(r,c+1),
                (r-1,c-1),(r-1,c),(r-1,c+1)
            ]

            for r,c in possible_moves:
                 if 0 <= r <= 7 and 0 <= c <= 7:
                    target_square = self.board[r][c]
                    if self.board[r][c] == "--":
                        valid_moves.append((r,c))
                    elif self.board[r][c] in ["wp","wB","wN","wR","wQ","wK"]:
                        valid_moves.append((r,c))




        return valid_moves
    
    def makemove(self,move):
        valid_moves = self.valid_moves(move.startrow, move.startcol)
        if (move.endrow, move.endcol) in valid_moves:
            self.board[move.startrow][move.startcol] = "--"
            self.board[move.endrow][move.endcol] = move.piece_moved
            self.moveLog.append(move)
            self.whiteToMove = not self.whiteToMove
            print(move.getchessnotation())
            self.whiteToMove = False
        else:
            print("geçersiz hamle")

        if move.ispawnpromotion:
            promote_to = input("Promote to (Q, R, B, N): ").upper()
            self.board[move.endrow][move.endcol] = move.piece_moved[0] + promote_to

        


class move():
    rankstorows = {"1" : 7, "2" : 6, "3" : 5, "4" : 4, "5" : 3, "6" : 2, "7" : 1, "8" : 0}
    rowstoranks = {v: k for k, v in rankstorows.items()}
    filestocols = {"a" : 0, "b" : 1, "c" : 2, "d" : 3, "e" : 4, "f" : 5, "g" : 6, "h" : 7}
    colstofiles = {v: k for k, v in filestocols.items()}
    
    def __init__(self, startsq, endsq, board):
        self.startrow = startsq[0]
        self.startcol = startsq[1]
        self.endrow = endsq[0]
        self.endcol = endsq[1]
        self.piece_moved = board[self.startrow][self.startcol]
        self.piece_captured = board[self.endrow][self.endcol]
        self.ispawnpromotion = False
        if (self.piece_moved == "wp" and self.endrow == 0) or (self.piece_moved == "bp" and self.endrow == 7):
            self.ispawnpromotion = True  
        self.isenpassant = False
    
    

    def getchessnotation(self):
        return self.getrankfile(self.startrow,self.startcol) + self.getrankfile(self.endrow,self.endcol)
    
    def getrankfile(self , r ,c):
        return self.colstofiles[c] + self.rowstoranks[r]