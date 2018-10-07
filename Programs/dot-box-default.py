class GameBoard:
    def __init__(self, width=5, height=5):
        """Initializes a rectangular gameboard."""
        self.width, self.height = width, height
        assert 2 <= self.width and 2 <= self.height,\
               "Game can't be played on this board's dimension."
        self.board = {}
        self.squares = {}
        self.player = 0


    def isGameOver(self):
        """Returns true if no more moves can be made.

        The maximum number of moves is equal to the number of possible
        lines between adjacent dots.  I'm calculating this to be
        $2*w*h - h - w$; I think that's right.  *grin*
        """
        w, h = self.width, self.height
        return len(list(self.board.keys())) == 2*w*h - h - w



    def _isSquareMove(self, move):
        """Returns a true value if a particular move will create a
        square.  In particular, returns a list of the the lower left
        corners of the squares captured by a move.

        (Note: I had forgotten about double crossed moves.  Gregor
        Lingl reported the bug; I'd better fix it now!  *grin*) """
        b = self.board
        mmove = self._makeMove       ## just to make typing easier
        ((x1, y1), (x2, y2)) = move
        captured_squares = []
        if self._isHorizontal(move):
            for j in [-1, 1]:
                if (mmove((x1, y1), (x1, y1-j)) in b
                    and mmove((x1, y1-j), (x1+1, y1-j)) in b
                    and mmove((x1+1, y1-j), (x2, y2)) in b):
                    captured_squares.append(min([(x1, y1), (x1, y1-j),
                                                 (x1+1, y1-j), (x2, y2)]))
        else:
            for j in [-1, 1]:
                if (mmove((x1, y1), (x1-j, y1)) in b
                    and mmove((x1-j, y1), (x1-j, y1+1)) in b
                    and mmove((x1-j, y1+1), (x2, y2)) in b):
                    captured_squares.append(min([(x1, y1), (x1-j, y1),
                                                 (x1-j, y1+1), (x2, y2)]))
        return captured_squares



    def _isHorizontal(self, move):
        "Return true if the move is in horizontal orientation."
        return abs(move[0][0] - move[1][0]) == 1


    def _isVertical(self, move):
        "Return true if the move is in vertical orientation."
        return not self.isHorizontal(self, move)


    def play(self, move):
        """Place a particular move on the board.  If any wackiness
        occurs, raise an AssertionError.  Returns a list of
        bottom-left corners of squares captured after a move."""
        assert (self._isGoodCoord(move[0]) and
                self._isGoodCoord(move[1])),\
                "Bad coordinates, out of bounds of the board."
        move = self._makeMove(move[0], move[1])
        assert(not move in self.board),\
                   "Bad move, line already occupied."
        self.board[move] = self.player
        ## Check if a square is completed.
        square_corners = self._isSquareMove(move)
        if square_corners:
            for corner in square_corners:
                self.squares[corner] = self.player
        else:
            self._switchPlayer()
        return square_corners


    def _switchPlayer(self):
        self.player = (self.player + 1) % 2


    def getPlayer(self): return self.player


    def getSquares(self):
        """Returns a dictionary of squares captured.  Returns
        a dict of lower left corner keys marked with the
        player who captured them."""
        return self.squares


    def __str__(self):
        """Return a nice string representation of the board."""
        buffer = []
        
        ## do the top line
        for i in range(self.width-1):
            if ((i, self.height-1), (i+1, self.height-1)) in self.board:
                buffer.append("0 * ")
            else: buffer.append("0   ")
        buffer.append("0\n")

        ## and now do alternating vertical/horizontal passes
        for j in range(self.height-2, -1, -1):
            ## vertical:
            for i in range(self.width):
                if ((i, j), (i, j+1)) in self.board:
                    buffer.append("  *")
                else:
                    buffer.append(" ")
                if (i, j) in self.squares:
                    buffer.append("%s " % self.squares[i,j])
                else:
                    buffer.append("  ")
            buffer.append("\n")

            ## horizontal
            for i in range(self.width-1):
                if ((i, j), (i+1, j)) in self.board:
                    buffer.append("0 * ")
                else: buffer.append("0   ")
            buffer.append("0\n")

        return ''.join(buffer)



    def _makeMove(self, coord1, coord2):
        """Return a new "move", and ensure it's in canonical form.
        (That is, force it so that it's an ordered tuple of tuples.)
        """
        ## TODO: do the Flyweight thing here to reduce object creation
        xdelta, ydelta = coord2[0] - coord1[0], coord2[1] - coord1[1]
        assert ((abs(xdelta) == 1 and abs(ydelta) == 0) or
                (abs(xdelta) == 0 and abs(ydelta) == 1)),\
                "Bad coordinates, not adjacent points."
        if coord1 < coord2:
            return (coord1, coord2)
        else:
            return (tuple(coord2), tuple(coord1))


    def _isGoodCoord(self, coord):
        """Returns true if the given coordinate is good.

        A coordinate is "good" if it's within the boundaries of the
        game board, and if the coordinates are integers."""
        return (0 <= coord[0] < self.width
                and 0 <= coord[1] < self.height
                and isinstance(coord[0], int)
                and isinstance(coord[1], int))
    


def _test(width, height):
    """A small driver to make sure that the board works.  It's not
    safe to use this test function in production, because it uses
    input()."""
    board = GameBoard(width, height)
    turn = 1
    scores = [0, 0]

    array = [ ((0, 0), (1, 0)), ((2, 2), (1, 2)), ((2, 2), (2, 1)), ((1, 3), (0, 3)), ((1, 0), (2, 0)) ]

    for x in range(5):
        squares_completed = board.play( array[x] )
    print(board)


if __name__ == "__main__":
    """If we're provided arguments, try using them as the
    width/height of the game board."""
    import sys
    if len(sys.argv[1:]) == 2:
        _test(int(sys.argv[1]), int(sys.argv[2]))
    elif len(sys.argv[1:]) == 1:
        _test(int(sys.argv[1]), int(sys.argv[1]))
    else:
        _test(4, 4)