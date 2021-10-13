# Author: Andrew Blair
# Date: 3-3-2021
# Description: This file contains classes for a Janggi board game and all of the
# pieces that are part of the game. Janggi has two players (blue and red) who each
# control pieces on a board. Different types of pieces can move and behave in different
# ways to capture the other players pieces. The goal of the game is to put the opposing
# player's general piece into checkmate.

class JanggiGame:
    """Class represents the abstract board game Janggi. JanggiGame will keep track
    of the 9x10 game board, the positions of pieces on the game board, the current
    state of the game, and which players turn it is currently. There are also methods
    which allow players to make moves on the board when it is their turn, and to
    determine if a player is currently in check. JanggiGame will need to communicate
    with all class objects representing Pieces on the game board: Generals, Guards,
    Horses, Elephants, Chariots, Cannons, and Soldiers. These Piece objects will inform
    JanggiGame which player they belong to and if they are capable of making a certain
    move on the board."""

    def __init__(self):
        """Initializes private data members for JanggiGame. Private data members
        include a representation of the game board and the pieces that are on it,
        current state of the game, which players turn it is currently, and the squares
        where the blue and red Generals are located."""
        self._game_state = 'UNFINISHED'
        self._player_turn = 'blue'
        self._blue_gen_square = 'e9'
        self._red_gen_square = 'e2'

        # create empty game board (columns a-i, rows 1-10)
        self._game_board = {
            'a1': None, 'a2': None, 'a3': None, 'a4': None, 'a5': None,
            'a6': None, 'a7': None, 'a8': None, 'a9': None, 'a10': None,
            'b1': None, 'b2': None, 'b3': None, 'b4': None, 'b5': None,
            'b6': None, 'b7': None, 'b8': None, 'b9': None, 'b10': None,
            'c1': None, 'c2': None, 'c3': None, 'c4': None, 'c5': None,
            'c6': None, 'c7': None, 'c8': None, 'c9': None, 'c10': None,
            'd1': None, 'd2': None, 'd3': None, 'd4': None, 'd5': None,
            'd6': None, 'd7': None, 'd8': None, 'd9': None, 'd10': None,
            'e1': None, 'e2': None, 'e3': None, 'e4': None, 'e5': None,
            'e6': None, 'e7': None, 'e8': None, 'e9': None, 'e10': None,
            'f1': None, 'f2': None, 'f3': None, 'f4': None, 'f5': None,
            'f6': None, 'f7': None, 'f8': None, 'f9': None, 'f10': None,
            'g1': None, 'g2': None, 'g3': None, 'g4': None, 'g5': None,
            'g6': None, 'g7': None, 'g8': None, 'g9': None, 'g10': None,
            'h1': None, 'h2': None, 'h3': None, 'h4': None, 'h5': None,
            'h6': None, 'h7': None, 'h8': None, 'h9': None, 'h10': None,
            'i1': None, 'i2': None, 'i3': None, 'i4': None, 'i5': None,
            'i6': None, 'i7': None, 'i8': None, 'i9': None, 'i10': None,
        }

        # create blue pieces
        b_ch1 = Chariot('blue')
        b_el1 = Elephant('blue')
        b_ho1 = Horse('blue')
        b_gu1 = Guard('blue')
        b_gu2 = Guard('blue')
        b_ho2 = Horse('blue')
        b_el2 = Elephant('blue')
        b_ch2 = Chariot('blue')
        b_gen = General('blue')
        b_ca1 = Cannon('blue')
        b_ca2 = Cannon('blue')
        b_so1 = Soldier('blue')
        b_so2 = Soldier('blue')
        b_so3 = Soldier('blue')
        b_so4 = Soldier('blue')
        b_so5 = Soldier('blue')

        # place blue pieces on starting squares
        self._game_board['a10'] = b_ch1
        self._game_board['b10'] = b_el1
        self._game_board['c10'] = b_ho1
        self._game_board['d10'] = b_gu1
        self._game_board['f10'] = b_gu2
        self._game_board['g10'] = b_el2
        self._game_board['h10'] = b_ho2
        self._game_board['i10'] = b_ch2
        self._game_board['e9'] = b_gen
        self._game_board['b8'] = b_ca1
        self._game_board['h8'] = b_ca2
        self._game_board['a7'] = b_so1
        self._game_board['c7'] = b_so2
        self._game_board['e7'] = b_so3
        self._game_board['g7'] = b_so4
        self._game_board['i7'] = b_so5

        # create red pieces
        r_ch1 = Chariot('red')
        r_el1 = Elephant('red')
        r_ho1 = Horse('red')
        r_gu1 = Guard('red')
        r_gu2 = Guard('red')
        r_ho2 = Horse('red')
        r_el2 = Elephant('red')
        r_ch2 = Chariot('red')
        r_gen = General('red')
        r_ca1 = Cannon('red')
        r_ca2 = Cannon('red')
        r_so1 = Soldier('red')
        r_so2 = Soldier('red')
        r_so3 = Soldier('red')
        r_so4 = Soldier('red')
        r_so5 = Soldier('red')

        # place red pieces on starting squares
        self._game_board['a1'] = r_ch1
        self._game_board['b1'] = r_el1
        self._game_board['c1'] = r_ho1
        self._game_board['d1'] = r_gu1
        self._game_board['f1'] = r_gu2
        self._game_board['g1'] = r_el2
        self._game_board['h1'] = r_ho2
        self._game_board['i1'] = r_ch2
        self._game_board['e2'] = r_gen
        self._game_board['b3'] = r_ca1
        self._game_board['h3'] = r_ca2
        self._game_board['a4'] = r_so1
        self._game_board['c4'] = r_so2
        self._game_board['e4'] = r_so3
        self._game_board['g4'] = r_so4
        self._game_board['i4'] = r_so5

    def get_game_state(self):
        """Method takes no parameters and returns the state of the game. Possible
        states are UNFINISHED, RED_WON, or BLUE_WON."""
        return self._game_state

    def set_game_state(self, new_state):
        """Method takes a new game state (string) as a parameter and sets the
        _game_state private data member to the new state. This only happens when a
        player wins."""
        self._game_state = new_state

    def get_player_turn(self):
        """Method takes no parameters and returns the color of the current player
        whose turn it is. Players are either red or blue."""
        return self._player_turn

    def set_player_turn(self, player):
        """Method takes the color of a player (string) as a parameter and sets the
        _player_turn private data member to that player. Players alternate taking turns,
        so this occurs everytime a player completes a valid turn."""
        self._player_turn = player

    def get_square(self, square):
        """Method takes as a parameter a square on the game board (string) and if a
        Piece is occupying the square, it will return the Piece object. Otherwise,
        it will return None."""
        return self._game_board[square]

    def set_square(self, square, piece=None):
        """Method will take as parameters a square on the game board (string) and a
        Piece for a specified player (optional parameter). If included, the Piece for
        that player will be placed onto the specified square. If the Piece parameter is
        not included, the square will be set to contain None."""
        self._game_board[square] = piece

    def get_gen_square(self, player):
        """Method takes as a parameter a player color and returns the square on
        the game board (string) where that player's General is currently located."""
        if player == 'blue':
            return self._blue_gen_square
        if player == 'red':
            return self._red_gen_square

    def set_gen_square(self, player, new_gen_sq):
        """Method takes as parameters a player color and the new square on the board
        (string) where the General for that player has moved onto. This method only
        updates the private data member for the player's General location, and it does
        not change the game board."""
        if player == 'blue':
            self._blue_gen_square = new_gen_sq
        if player == 'red':
            self._red_gen_square = new_gen_sq

    def get_game_board(self):
        """Method takes no parameters and returns the current state of the game board."""
        return self._game_board

    def is_in_check(self, player):
        """Method takes as a parameter a player color and returns True if that
        player is in check. Otherwise, returns False. Check occurs when a player's
        General could be taken by an opposing player's Piece on it's next move."""
        temp_board = self.get_game_board()
        all_opponent_moves = []
        player_gen_sq = self.get_gen_square(player)

        # create list of all moves the opposing player could make
        for square in temp_board:
            if temp_board[square] is not None:
                if temp_board[square].get_player() != player:
                    opp_moves = temp_board[square].check_move(square, temp_board)
                    all_opponent_moves = all_opponent_moves + opp_moves

        # check if current player's general could be attacked by an opponent piece
        if player_gen_sq in all_opponent_moves:
            return True
        else:
            return False

    def is_checkmate(self, player):
        """Method takes as a parameter a player color and returns True if they
        are in checkmate and have lost the game. Returns false if the player is
        still in check, but a valid move exists to get them out of check."""
        temp_board = self.get_game_board()

        # for each of the current player's pieces, look at all possible moves
        for square in temp_board:
            if temp_board[square] is not None:
                if temp_board[square].get_player() == player:
                    possible_moves = temp_board[square].check_move(square, temp_board)

                    # for each move a piece could make, determine if it would end check
                    for move in possible_moves:
                        if square != move:
                            if self.try_move(square, move) is True:
                                return False

        # no moves exist that could take the player out of check
        return True

    def try_move(self, try_current_sq, try_move_sq):
        """Method takes as parameters a square with a piece to try moving and a
        square to try moving onto. Returns True if the player would no longer be in
        check after trying the move. Returns False if the move would not take the
        player out of check. The method will also restore the game board and Pieces
        to the state they were in prior to the method being called."""
        result = False
        try_move_piece = self.get_square(try_move_sq)
        if try_move_piece is not None:
            try_move_player = try_move_piece.get_player()
        try_current_piece = self.get_square(try_current_sq)
        try_current_player = try_current_piece.get_player()
        try_gen_location = self.get_gen_square(try_current_player)

        # check if a piece of the same color as the player is in the move square
        if try_move_piece is not None:
            if try_move_player == try_current_player:
                return result

        # try making the move
        self.set_square(try_move_sq, try_current_piece)
        self.set_square(try_current_sq)
        if type(try_current_piece) is General:
            self.set_gen_square(try_current_player, try_move_sq)

        # determine if the player is no longer in check and update result
        if self.is_in_check(try_current_player) is False:
            result = True

        # restore the board to previous state and return
        self.set_square(try_current_sq, try_current_piece)
        self.set_square(try_move_sq, try_move_piece)
        if type(try_current_piece) is General:
            self.set_gen_square(try_current_player, try_gen_location)

        return result

    def make_move(self, current_sq, move_sq):
        """Method takes as parameters the square a piece is moving from and the
        square that same piece wants to move onto (in order). If a piece moves to
        the square it is already on, the player will be considered as passing on
        their turn. A valid move to a square where an opponent's Piece is located
        will result in the opponent's Piece being captured and removed from the game
        board, and the moving piece now occupying that square. Invalid moves will
        return False and valid moves will return True. This method will utilize
        JanggiGame get and set methods and Piece subclass methods."""
        current_piece = self.get_square(current_sq)
        current_game_board = self.get_game_board()
        destination_piece = self.get_square(move_sq)

        # check if game is over
        if self.get_game_state() != 'UNFINISHED':
            return False

        # check if the specified square contains a piece
        if current_piece is None:
            return False

        # check if correct player is moving (player turn is same as color of piece moving)
        current_player = current_piece.get_player()
        if current_player != self.get_player_turn():
            return False

        # check if move square is on the game board
        if (int(move_sq[1:])) < 1 or (int(move_sq[1:])) > 10:
            return False
        if (ord(move_sq[0]) - 96) < 1 or (ord(move_sq[0]) - 96) > 9:
            return False

        # check if a piece of the same color as the player is in the move square
        if destination_piece is not None:
            if current_piece != destination_piece:
                destination_player = destination_piece.get_player()
                if destination_player == current_player:
                    return False

        # check if the move is valid for the type of piece being moved
        available_moves = current_piece.check_move(current_sq, current_game_board)
        if move_sq not in available_moves:
            return False

        # if not passing, move the current piece to the move square
        if current_sq != move_sq:
            self.set_square(move_sq, current_piece)

        # if not passing, update the current square (moved from) on the board to be empty
        if current_sq != move_sq:
            self.set_square(current_sq)

        # if moving piece is a general, update general square data member
        # preserve former general square data member (in event move is invalid due to check)
        temp_gen_location = self.get_gen_square(current_player)
        if type(current_piece) is General:
            self.set_gen_square(current_player, move_sq)

        # determine if current player is in check following move (if so, reverse move and return false)
        if self.is_in_check(current_player) is True:
            self.set_square(current_sq, current_piece)
            self.set_square(move_sq, destination_piece)
            if type(current_piece) is General:
                self.set_gen_square(current_player, temp_gen_location)
            return False

        # move was successful, update player turn to next player
        if self.get_player_turn() == 'blue':
            self.set_player_turn('red')
        else:
            self.set_player_turn('blue')

        # determine if opposing player is in check following move
        if current_player == 'blue':
            opponent = 'red'
        else:
            opponent = 'blue'
        if self.is_in_check(opponent) is True:

            # determine if opposing player is in checkmate and update game state as necessary
            if self.is_checkmate(opponent) is True:
                if opponent == 'blue':
                    self.set_game_state('RED_WON')
                else:
                    self.set_game_state('BLUE_WON')

        return True


class Piece:
    """Class represents a Piece on the JanggiGame board. Different subclasses of
    Piece represent different types of game pieces and are able to move and behave
    differently on the board. JanggiGame will need to know which player a Piece
    belongs to and how it can move (defined in subclasses of Piece)."""

    def __init__(self, player):
        """Initializes private data members for a Piece. Private data members
        include the color of the piece, which indicates to which player it belongs."""
        self._player = player
        # create lists of squares in each fortress for move determination
        self._blue_fortress = ['d8', 'd9', 'd10', 'e8', 'e9', 'e10', 'f8', 'f9', 'f10']
        self._red_fortress = ['d1', 'd2', 'd3', 'e1', 'e2', 'e3', 'f1', 'f2', 'f3']

    def get_player(self):
        """Method takes no parameters and returns the color of the piece,
        indicating to which player it belongs."""
        return self._player

    def get_fortress(self, player=None):
        """Method takes an optional parameter of the color of a player (string) and returns the
        list of squares in that player's fortress. If the optional parameter is not passed an
        argument, then the method will return a list of squares in both fortresses."""
        if player == 'blue':
            return self._blue_fortress
        elif player == 'red':
            return self._red_fortress
        else:
            fort_list = self._blue_fortress + self._red_fortress
            return fort_list


class General(Piece):
    """Class represents a General game piece in JanggiGame. A General is a Piece.
    A General will communicate with a JanggiGame to tell which player the General
    belongs to and what possible moves the General can make on the game board."""

    def check_move(self, current_sq, board_state):
        """Method takes as parameters the current square this Piece occupies and
        the current board state. Returns a list of available moves for the Piece."""
        moves_list = []
        potential_moves = []
        current_player = self.get_player()

        # determine valid moves for blue general from current square
        if current_player == 'blue':
            if current_sq == 'd8':
                potential_moves = ['d8', 'd9', 'e8', 'e9']
            if current_sq == 'd9':
                potential_moves = ['d8', 'd9', 'd10', 'e9']
            if current_sq == 'd10':
                potential_moves = ['d9', 'd10', 'e9', 'e10']
            if current_sq == 'e8':
                potential_moves = ['d8', 'e8', 'e9', 'f8']
            if current_sq == 'e9':
                potential_moves = self.get_fortress('blue')
            if current_sq == 'e10':
                potential_moves = ['d10', 'e10', 'e9', 'f10']
            if current_sq == 'f8':
                potential_moves = ['e8', 'e9', 'f8', 'f9']
            if current_sq == 'f9':
                potential_moves = ['e9', 'f8', 'f9', 'f10']
            if current_sq == 'f10':
                potential_moves = ['e9', 'e10', 'f9', 'f10']

        # determine valid moves for red general from current square
        if current_player == 'red':
            if current_sq == 'd1':
                potential_moves = ['d1', 'd2', 'e1', 'e2']
            if current_sq == 'd2':
                potential_moves = ['d1', 'd2', 'd3', 'e2']
            if current_sq == 'd3':
                potential_moves = ['d2', 'd3', 'e2', 'e3']
            if current_sq == 'e1':
                potential_moves = ['d1', 'e1', 'e2', 'f1']
            if current_sq == 'e2':
                potential_moves = self.get_fortress('red')
            if current_sq == 'e3':
                potential_moves = ['d3', 'e3', 'e2', 'f3']
            if current_sq == 'f1':
                potential_moves = ['e1', 'e2', 'f1', 'f2']
            if current_sq == 'f2':
                potential_moves = ['e2', 'f1', 'f2', 'f3']
            if current_sq == 'f3':
                potential_moves = ['e2', 'e3', 'f2', 'f3']

        # remove moves blocked by current player's other pieces
        for square in potential_moves:
            if board_state[square] is None:
                moves_list.append(square)
            elif board_state[square].get_player() != current_player:
                moves_list.append(square)

        # add current square as move for passing turn
        moves_list.append(current_sq)

        return moves_list


class Guard(Piece):
    """Class represents a Guard game piece in JanggiGame. A Guard is a Piece.
    A Guard will communicate with a JanggiGame to tell which player the Guard
    belongs to and what possible moves the Guard can make on the game board."""

    def check_move(self, current_sq, board_state):
        """Method takes as parameters the current square this Piece occupies and
        the current board state. Returns a list of available moves for the Piece."""
        moves_list = []
        potential_moves = []
        current_player = self.get_player()

        # determine valid moves for blue guard from current square
        if current_player == 'blue':
            if current_sq == 'd8':
                potential_moves = ['d8', 'd9', 'e8', 'e9']
            if current_sq == 'd9':
                potential_moves = ['d8', 'd9', 'd10', 'e9']
            if current_sq == 'd10':
                potential_moves = ['d9', 'd10', 'e9', 'e10']
            if current_sq == 'e8':
                potential_moves = ['d8', 'e8', 'e9', 'f8']
            if current_sq == 'e9':
                potential_moves = self.get_fortress('blue')
            if current_sq == 'e10':
                potential_moves = ['d10', 'e10', 'e9', 'f10']
            if current_sq == 'f8':
                potential_moves = ['e8', 'e9', 'f8', 'f9']
            if current_sq == 'f9':
                potential_moves = ['e9', 'f8', 'f9', 'f10']
            if current_sq == 'f10':
                potential_moves = ['e9', 'e10', 'f9', 'f10']

        # determine valid moves for red guard from current square
        if current_player == 'red':
            if current_sq == 'd1':
                potential_moves = ['d1', 'd2', 'e1', 'e2']
            if current_sq == 'd2':
                potential_moves = ['d1', 'd2', 'd3', 'e2']
            if current_sq == 'd3':
                potential_moves = ['d2', 'd3', 'e2', 'e3']
            if current_sq == 'e1':
                potential_moves = ['d1', 'e1', 'e2', 'f1']
            if current_sq == 'e2':
                potential_moves = self.get_fortress('red')
            if current_sq == 'e3':
                potential_moves = ['d3', 'e3', 'e2', 'f3']
            if current_sq == 'f1':
                potential_moves = ['e1', 'e2', 'f1', 'f2']
            if current_sq == 'f2':
                potential_moves = ['e2', 'f1', 'f2', 'f3']
            if current_sq == 'f3':
                potential_moves = ['e2', 'e3', 'f2', 'f3']

        # remove moves blocked by current player's other pieces
        for square in potential_moves:
            if board_state[square] is None:
                moves_list.append(square)
            elif board_state[square].get_player() != current_player:
                moves_list.append(square)

        # add current square as move for passing turn
        moves_list.append(current_sq)

        return moves_list


class Horse(Piece):
    """Class represents a Horse game piece in JanggiGame. A Horse is a Piece.
    A Horse will communicate with a JanggiGame to tell which player the Horse
    belongs to and what possible moves the Horse can make on the game board."""

    def check_move(self, current_sq, board_state):
        """Method takes as parameters the current square this Piece occupies and
        the current board state. Returns a list of available moves for the Piece."""
        current_square = current_sq
        cur_row_num = int(current_square[1:])
        cur_col_num = ord(current_square[0]) - 96
        move_list = []
        current_board = board_state

        # determine possible moves for horse from current position
        up_1 = chr(cur_col_num + 96) + str(cur_row_num - 1)
        down_1 = chr(cur_col_num + 96) + str(cur_row_num + 1)
        left_1 = chr(cur_col_num + 95) + str(cur_row_num)
        right_1 = chr(cur_col_num + 97) + str(cur_row_num)

        # check if first step of horse move is available
        if up_1 in current_board and current_board[up_1] is None:

            # add completed move squares to available moves
            up_2_left_1 = chr(cur_col_num + 95) + str(cur_row_num - 2)
            if up_2_left_1 in current_board:
                move_list.append(up_2_left_1)

            up_2_right_1 = chr(cur_col_num + 97) + str(cur_row_num - 2)
            if up_2_right_1 in current_board:
                move_list.append(up_2_right_1)

        if down_1 in current_board and current_board[down_1] is None:
            down_2_left_1 = chr(cur_col_num + 95) + str(cur_row_num + 2)
            if down_2_left_1 in current_board:
                move_list.append(down_2_left_1)
            down_2_right_1 = chr(cur_col_num + 97) + str(cur_row_num + 2)
            if down_2_right_1 in current_board:
                move_list.append(down_2_right_1)

        if left_1 in current_board and current_board[left_1] is None:
            left_2_up_1 = chr(cur_col_num + 94) + str(cur_row_num - 1)
            if left_2_up_1 in current_board:
                move_list.append(left_2_up_1)
            left_2_down_1 = chr(cur_col_num + 94) + str(cur_row_num + 1)
            if left_2_down_1 in current_board:
                move_list.append(left_2_down_1)

        if right_1 in current_board and current_board[right_1] is None:
            right_2_up_1 = chr(cur_col_num + 98) + str(cur_row_num - 1)
            if right_2_up_1 in current_board:
                move_list.append(right_2_up_1)
            right_2_down_1 = chr(cur_col_num + 98) + str(cur_row_num + 1)
            if right_2_down_1 in current_board:
                move_list.append(right_2_down_1)

        # add current square as move for passing turn
        move_list.append(current_square)

        return move_list


class Elephant(Piece):
    """Class represents a Elephant game piece in JanggiGame. A Elephant is a Piece.
    A Elephant will communicate with a JanggiGame to tell which player the Elephant
    belongs to and what possible moves the Elephant can make on the game board."""

    def check_move(self, current_sq, board_state):
        """Method takes as parameters the current square this Piece occupies and
        the current board state. Returns a list of available moves for the Piece."""
        current_square = current_sq
        cur_row_num = int(current_square[1:])
        cur_col_num = ord(current_square[0]) - 96
        move_list = []
        current_board = board_state

        # determine possible moves for elephant from current position
        up_1 = chr(cur_col_num + 96) + str(cur_row_num - 1)
        down_1 = chr(cur_col_num + 96) + str(cur_row_num + 1)
        left_1 = chr(cur_col_num + 95) + str(cur_row_num)
        right_1 = chr(cur_col_num + 97) + str(cur_row_num)

        # check if first step of elephant move is available
        if up_1 in current_board and current_board[up_1] is None:

            # check if second steps of elephant move are available
            up_2_left_1 = chr(cur_col_num + 95) + str(cur_row_num - 2)
            if up_2_left_1 in current_board and current_board[up_2_left_1] is None:

                # add completed move square to available moves
                up_3_left_2 = chr(cur_col_num + 94) + str(cur_row_num - 3)
                if up_3_left_2 in current_board:
                    move_list.append(up_3_left_2)

            # check if second steps of elephant move are available
            up_2_right_1 = chr(cur_col_num + 97) + str(cur_row_num - 2)
            if up_2_right_1 in current_board and current_board[up_2_right_1] is None:

                # add completed move square to available moves
                up_3_right_2 = chr(cur_col_num + 98) + str(cur_row_num - 3)
                if up_3_right_2 in current_board:
                    move_list.append(up_3_right_2)

        if down_1 in current_board and current_board[down_1] is None:

            down_2_left_1 = chr(cur_col_num + 95) + str(cur_row_num + 2)
            if down_2_left_1 in current_board and current_board[down_2_left_1] is None:
                down_3_left_2 = chr(cur_col_num + 94) + str(cur_row_num + 3)
                if down_3_left_2 in current_board:
                    move_list.append(down_3_left_2)

            down_2_right_1 = chr(cur_col_num + 97) + str(cur_row_num + 2)
            if down_2_right_1 in current_board and current_board[down_2_right_1] is None:
                down_3_right_2 = chr(cur_col_num + 98) + str(cur_row_num + 3)
                if down_3_right_2 in current_board:
                    move_list.append(down_3_right_2)

        if left_1 in current_board and current_board[left_1] is None:

            left_2_up_1 = chr(cur_col_num + 94) + str(cur_row_num - 1)
            if left_2_up_1 in current_board and current_board[left_2_up_1] is None:
                left_3_up_2 = chr(cur_col_num + 93) + str(cur_row_num - 2)
                if left_3_up_2 in current_board:
                    move_list.append(left_3_up_2)

            left_2_down_1 = chr(cur_col_num + 94) + str(cur_row_num + 1)
            if left_2_down_1 in current_board and current_board[left_2_down_1] is None:
                left_3_down_2 = chr(cur_col_num + 93) + str(cur_row_num + 2)
                if left_3_down_2 in current_board:
                    move_list.append(left_3_down_2)

        if right_1 in current_board and current_board[right_1] is None:

            right_2_up_1 = chr(cur_col_num + 98) + str(cur_row_num - 1)
            if right_2_up_1 in current_board and current_board[right_2_up_1] is None:
                right_3_up_2 = chr(cur_col_num + 99) + str(cur_row_num - 2)
                if right_3_up_2 in current_board:
                    move_list.append(right_3_up_2)

            right_2_down_1 = chr(cur_col_num + 98) + str(cur_row_num + 1)
            if right_2_down_1 in current_board and current_board[right_2_down_1] is None:
                right_3_down_2 = chr(cur_col_num + 99) + str(cur_row_num + 2)
                if right_3_down_2 in current_board:
                    move_list.append(right_3_down_2)

        # add current square as move for passing turn
        move_list.append(current_square)

        return move_list


class Chariot(Piece):
    """Class represents a Chariot game piece in JanggiGame. A Chariot is a Piece.
    A Chariot will communicate with a JanggiGame to tell which player the Chariot
    belongs to and what possible moves the Chariot can make on the game board."""

    def check_move(self, current_sq, board_state):
        """Method takes as parameters the current square this Piece occupies and
        the current board state. Returns a list of available moves for the Piece."""
        cur_row_num = int(current_sq[1:])
        cur_col_num = ord(current_sq[0]) - 96
        current_board = board_state

        # determine possible moves for chariot
        up = self.path_up_col(cur_row_num, cur_col_num, current_board)
        down = self.path_down_col(cur_row_num, cur_col_num, current_board)
        left = self.path_left_row(cur_row_num, cur_col_num, current_board)
        right = self.path_right_row(cur_row_num, cur_col_num, current_board)
        move_list = up + down + left + right

        # if chariot is in red fortress, add additional moves
        if current_sq == 'd1':
            if current_board['e2'] is None or current_board['e2'].get_player() != self.get_player():
                move_list.append('e2')
                if current_board['f3'] is None or current_board['f3'].get_player() != self.get_player():
                    move_list.append('f3')

        if current_sq == 'f1':
            if current_board['e2'] is None or current_board['e2'].get_player() != self.get_player():
                move_list.append('e2')
                if current_board['d3'] is None or current_board['d3'].get_player() != self.get_player():
                    move_list.append('d3')

        if current_sq == 'd3':
            if current_board['e2'] is None or current_board['e2'].get_player() != self.get_player():
                move_list.append('e2')
                if current_board['f1'] is None or current_board['f1'].get_player() != self.get_player():
                    move_list.append('f1')

        if current_sq == 'f3':
            if current_board['e2'] is None or current_board['e2'].get_player() != self.get_player():
                move_list.append('e2')
                if current_board['d1'] is None or current_board['d1'].get_player() != self.get_player():
                    move_list.append('d1')

        if current_sq == 'e2':
            if current_board['d1'] is None or current_board['d1'].get_player() != self.get_player():
                move_list.append('d1')
            if current_board['f1'] is None or current_board['f1'].get_player() != self.get_player():
                move_list.append('f1')
            if current_board['d3'] is None or current_board['d3'].get_player() != self.get_player():
                move_list.append('d3')
            if current_board['f3'] is None or current_board['f3'].get_player() != self.get_player():
                move_list.append('f3')

        # if chariot is in blue fortress, add additional moves
        if current_sq == 'd8':
            if current_board['e9'] is None or current_board['e9'].get_player() != self.get_player():
                move_list.append('e9')
                if current_board['f10'] is None or current_board['f10'].get_player() != self.get_player():
                    move_list.append('f10')

        if current_sq == 'f8':
            if current_board['e9'] is None or current_board['e9'].get_player() != self.get_player():
                move_list.append('e9')
                if current_board['d10'] is None or current_board['d10'].get_player() != self.get_player():
                    move_list.append('d10')

        if current_sq == 'd10':
            if current_board['e9'] is None or current_board['e9'].get_player() != self.get_player():
                move_list.append('e9')
                if current_board['f8'] is None or current_board['f8'].get_player() != self.get_player():
                    move_list.append('f8')

        if current_sq == 'f10':
            if current_board['e9'] is None or current_board['e9'].get_player() != self.get_player():
                move_list.append('e9')
                if current_board['d8'] is None or current_board['d8'].get_player() != self.get_player():
                    move_list.append('d8')

        if current_sq == 'e9':
            if current_board['d8'] is None or current_board['d8'].get_player() != self.get_player():
                move_list.append('d8')
            if current_board['f8'] is None or current_board['f8'].get_player() != self.get_player():
                move_list.append('f8')
            if current_board['d10'] is None or current_board['d10'].get_player() != self.get_player():
                move_list.append('d10')
            if current_board['f10'] is None or current_board['f10'].get_player() != self.get_player():
                move_list.append('f10')

        # add current square as move for passing turn
        move_list.append(current_sq)

        return move_list

    def path_up_col(self, cur_row, cur_col, board):
        """Method takes as parameters the row number of the current piece, the
        column number of the current piece, and the current state of the board.
        Returns a list of possible moves upwards in a line on the board."""
        moves_up = []
        look_row = cur_row - 1
        look_col = cur_col
        while look_row > 0:
            look_sq = chr(look_col + 96) + str(look_row)
            if board[look_sq] is None:
                moves_up.append(look_sq)
            if board[look_sq] is not None and board[look_sq].get_player() == self.get_player():
                return moves_up
            if board[look_sq] is not None and board[look_sq].get_player() != self.get_player():
                moves_up.append(look_sq)
                return moves_up
            look_row -= 1
        return moves_up

    def path_down_col(self, cur_row, cur_col, board):
        """Method takes as parameters the row number of the current piece, the
        column number of the current piece, and the current state of the board.
        Returns a list of possible moves downwards in a line on the board."""
        moves_down = []
        look_row = cur_row + 1
        look_col = cur_col
        while look_row < 11:
            look_sq = chr(look_col + 96) + str(look_row)
            if board[look_sq] is None:
                moves_down.append(look_sq)
            if board[look_sq] is not None and board[look_sq].get_player() == self.get_player():
                return moves_down
            if board[look_sq] is not None and board[look_sq].get_player() != self.get_player():
                moves_down.append(look_sq)
                return moves_down
            look_row += 1
        return moves_down

    def path_left_row(self, cur_row, cur_col, board):
        """Method takes as parameters the row number of the current piece, the
        column number of the current piece, and the current state of the board.
        Returns a list of possible moves to the left in a line on the board."""
        moves_left = []
        look_row = cur_row
        look_col = cur_col - 1
        while look_col > 0:
            look_sq = chr(look_col + 96) + str(look_row)
            if board[look_sq] is None:
                moves_left.append(look_sq)
            if board[look_sq] is not None and board[look_sq].get_player() == self.get_player():
                return moves_left
            if board[look_sq] is not None and board[look_sq].get_player() != self.get_player():
                moves_left.append(look_sq)
                return moves_left
            look_col -= 1
        return moves_left

    def path_right_row(self, cur_row, cur_col, board):
        """Method takes as parameters the row number of the current piece, the
        column number of the current piece, and the current state of the board.
        Returns a list of possible moves to the right in a line on the board."""
        moves_right = []
        look_row = cur_row
        look_col = cur_col + 1
        while look_col < 10:
            look_sq = chr(look_col + 96) + str(look_row)
            if board[look_sq] is None:
                moves_right.append(look_sq)
            if board[look_sq] is not None and board[look_sq].get_player() == self.get_player():
                return moves_right
            if board[look_sq] is not None and board[look_sq].get_player() != self.get_player():
                moves_right.append(look_sq)
                return moves_right
            look_col += 1
        return moves_right


class Cannon(Piece):
    """Class represents a Cannon game piece in JanggiGame. A Cannon is a Piece.
    A Cannon will communicate with a JanggiGame to tell which player the Cannon
    belongs to and what possible moves the Cannon can make on the game board."""

    def check_move(self, current_sq, board_state):
        """Method takes as parameters the current square this Piece occupies and
        the current board state. Returns a list of available moves for the Piece."""
        cur_row_num = int(current_sq[1:])
        cur_col_num = ord(current_sq[0]) - 96
        current_board = board_state
        current_square = current_sq

        # determine possible moves for cannon
        up = self.path_up_col(cur_row_num, cur_col_num, current_board)
        down = self.path_down_col(cur_row_num, cur_col_num, current_board)
        left = self.path_left_row(cur_row_num, cur_col_num, current_board)
        right = self.path_right_row(cur_row_num, cur_col_num, current_board)
        move_list = up + down + left + right

        # if cannon is in blue fortress, add additional moves
        if current_square == 'd8':
            if current_board['e9'] is not None and type(current_board['e9']) is not Cannon:
                if current_board['f10'] is None:
                    move_list.append('f10')
                elif current_board['f10'].get_player() != self.get_player():
                    if type(current_board['f10']) is not Cannon:
                        move_list.append('f10')

        if current_square == 'f8':
            if current_board['e9'] is not None and type(current_board['e9']) is not Cannon:
                if current_board['d10'] is None:
                    move_list.append('d10')
                elif current_board['d10'].get_player() != self.get_player():
                    if type(current_board['d10']) is not Cannon:
                        move_list.append('d10')

        if current_square == 'd10':
            if current_board['e9'] is not None and type(current_board['e9']) is not Cannon:
                if current_board['f8'] is None:
                    move_list.append('f8')
                elif current_board['f8'].get_player() != self.get_player():
                    if type(current_board['f8']) is not Cannon:
                        move_list.append('f8')

        if current_square == 'f10':
            if current_board['e9'] is not None and type(current_board['e9']) is not Cannon:
                if current_board['d8'] is None:
                    move_list.append('d8')
                elif current_board['d8'].get_player() != self.get_player():
                    if type(current_board['d8']) is not Cannon:
                        move_list.append('d8')

        # if cannon is in red fortress, add additional moves
        if current_square == 'd1':
            if current_board['e2'] is not None and type(current_board['e9']) is not Cannon:
                if current_board['f3'] is None:
                    move_list.append('f3')
                elif current_board['f3'].get_player() != self.get_player():
                    if type(current_board['f3']) is not Cannon:
                        move_list.append('f3')

        if current_square == 'f1':
            if current_board['e2'] is not None and type(current_board['e9']) is not Cannon:
                if current_board['d3'] is None:
                    move_list.append('d3')
                elif current_board['d3'].get_player() != self.get_player():
                    if type(current_board['d3']) is not Cannon:
                        move_list.append('d3')

        if current_square == 'd3':
            if current_board['e2'] is not None and type(current_board['e9']) is not Cannon:
                if current_board['f1'] is None:
                    move_list.append('f1')
                elif current_board['f1'].get_player() != self.get_player():
                    if type(current_board['f1']) is not Cannon:
                        move_list.append('f1')

        if current_square == 'f3':
            if current_board['e2'] is not None and type(current_board['e9']) is not Cannon:
                if current_board['d1'] is None:
                    move_list.append('d1')
                elif current_board['d1'].get_player() != self.get_player():
                    if type(current_board['d1']) is not Cannon:
                        move_list.append('d1')

        # add current square as move for passing turn
        move_list.append(current_sq)

        return move_list

    def path_up_col(self, cur_row, cur_col, board):
        """Method takes as parameters the row number of the current piece, the
        column number of the current piece, and the current state of the board.
        Returns a list of possible moves upwards in a line on the board."""
        moves_up = []
        jumping = False
        look_row = cur_row - 1
        look_col = cur_col
        while look_row > 0:
            look_sq = chr(look_col + 96) + str(look_row)
            if board[look_sq] is None and jumping is True:
                moves_up.append(look_sq)
            if board[look_sq] is not None and jumping is True:
                if board[look_sq].get_player() == self.get_player():
                    return moves_up
                if board[look_sq].get_player() != self.get_player():
                    if type(board[look_sq]) is Cannon:
                        return moves_up
                    else:
                        moves_up.append(look_sq)
                        return moves_up
            if board[look_sq] is not None and jumping is False:
                if type(board[look_sq]) is Cannon:
                    return moves_up
                jumping = True
            look_row -= 1
        return moves_up

    def path_down_col(self, cur_row, cur_col, board):
        """Method takes as parameters the row number of the current piece, the
        column number of the current piece, and the current state of the board.
        Returns a list of possible moves downwards in a line on the board."""
        moves_down = []
        jumping = False
        look_row = cur_row + 1
        look_col = cur_col
        while look_row < 11:
            look_sq = chr(look_col + 96) + str(look_row)
            if board[look_sq] is None and jumping is True:
                moves_down.append(look_sq)
            if board[look_sq] is not None and jumping is True:
                if board[look_sq].get_player() == self.get_player():
                    return moves_down
                if board[look_sq].get_player() != self.get_player():
                    if type(board[look_sq]) is Cannon:
                        return moves_down
                    else:
                        moves_down.append(look_sq)
                        return moves_down
            if board[look_sq] is not None and jumping is False:
                if type(board[look_sq]) is Cannon:
                    return moves_down
                jumping = True
            look_row += 1
        return moves_down

    def path_left_row(self, cur_row, cur_col, board):
        """Method takes as parameters the row number of the current piece, the
        column number of the current piece, and the current state of the board.
        Returns a list of possible moves to the left in a line on the board."""
        moves_left = []
        jumping = False
        look_row = cur_row
        look_col = cur_col - 1
        while look_col > 0:
            look_sq = chr(look_col + 96) + str(look_row)
            if board[look_sq] is None and jumping is True:
                moves_left.append(look_sq)
            if board[look_sq] is not None and jumping is True:
                if board[look_sq].get_player() == self.get_player():
                    return moves_left
                if board[look_sq].get_player() != self.get_player():
                    if type(board[look_sq]) is Cannon:
                        return moves_left
                    else:
                        moves_left.append(look_sq)
                        return moves_left
            if board[look_sq] is not None and jumping is False:
                if type(board[look_sq]) is Cannon:
                    return moves_left
                jumping = True
            look_col -= 1
        return moves_left

    def path_right_row(self, cur_row, cur_col, board):
        """Method takes as parameters the row number of the current piece, the
        column number of the current piece, and the current state of the board.
        Returns a list of possible moves to the right in a line on the board."""
        moves_right = []
        jumping = False
        look_row = cur_row
        look_col = cur_col + 1
        while look_col < 10:
            look_sq = chr(look_col + 96) + str(look_row)
            if board[look_sq] is None and jumping is True:
                moves_right.append(look_sq)
            if board[look_sq] is not None and jumping is True:
                if board[look_sq].get_player() == self.get_player():
                    return moves_right
                if board[look_sq].get_player() != self.get_player():
                    if type(board[look_sq]) is Cannon:
                        return moves_right
                    else:
                        moves_right.append(look_sq)
                        return moves_right
            if board[look_sq] is not None and jumping is False:
                if type(board[look_sq]) is Cannon:
                    return moves_right
                jumping = True
            look_col += 1
        return moves_right


class Soldier(Piece):
    """Class represents a Soldier game piece in JanggiGame. A Soldier is a Piece.
    A Soldier will communicate with a JanggiGame to tell which player the Soldier
    belongs to and what possible moves the Soldier can make on the game board."""

    def check_move(self, current_sq, board_state):
        """Method takes as parameters the current square this Piece occupies and
        the current board state. Returns a list of available moves for the Piece."""
        cur_row_num = int(current_sq[1:])
        cur_col_num = ord(current_sq[0]) - 96
        potential_moves = []
        move_list = []
        current_board = board_state

        # add standard set of possible soldier moves to moves list
        if self.get_player() == 'blue':

            left_1 = chr(cur_col_num + 95) + str(cur_row_num)
            if left_1 in current_board:
                potential_moves.append(left_1)

            right_1 = chr(cur_col_num + 97) + str(cur_row_num)
            if right_1 in current_board:
                potential_moves.append(right_1)

            up_1 = chr(cur_col_num + 96) + str(cur_row_num - 1)
            if up_1 in current_board:
                potential_moves.append(up_1)

        if self.get_player() == 'red':

            left_1 = chr(cur_col_num + 95) + str(cur_row_num)
            if left_1 in current_board:
                potential_moves.append(left_1)

            right_1 = chr(cur_col_num + 97) + str(cur_row_num)
            if right_1 in current_board:
                potential_moves.append(right_1)

            down_1 = chr(cur_col_num + 96) + str(cur_row_num + 1)
            if down_1 in current_board:
                potential_moves.append(down_1)

        # if the soldier is in the red fortress, include diagonal moves
        if current_sq in self.get_fortress('red'):
            if current_sq == 'd3' or current_sq == 'f3':
                potential_moves.append('e2')
            if current_sq == 'e2':
                potential_moves.append('d1')
                potential_moves.append('f1')

        # if the soldier is in the blue fortress, include diagonal moves
        if current_sq in self.get_fortress('blue'):
            if current_sq == 'd8' or current_sq == 'f8':
                potential_moves.append('e9')
            if current_sq == 'e9':
                potential_moves.append('d10')
                potential_moves.append('f10')

        # remove moves blocked by current player's other pieces
        for square in potential_moves:
            if current_board[square] is None:
                move_list.append(square)
            elif current_board[square].get_player() != self.get_player():
                move_list.append(square)

        # add current square as move for passing turn
        move_list.append(current_sq)

        return move_list
