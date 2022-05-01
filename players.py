class Player:
    def __init__(self, inputV = 1, inputH = 1, board=None):
        if board is None:
            board = []
        self.inputV = inputV
        self.inputH = inputH
        self.board = board


    def set_player1(self):
        if self.board[self.inputV][self.inputH] == " . ":
            self.board[self.inputV][self.inputH] = " X "

    def set_player2(self):
        if self.board[self.inputV][self.inputH] == " . ":
            self.board[self.inputV][self.inputH] = " O "


