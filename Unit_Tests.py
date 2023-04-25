import pytest
import Piece
import chess_engine
from unittest.mock import MagicMock, Mock, patch
import enums

def cycle_values():
    while True:
        values = [lambda row, col: Piece.Rook("rook", row, col, enums.Player.PLAYER_1), lambda row, col: Piece.Rook("rook", row, col, enums.Player.PLAYER_2)]
        for value in values:
            yield value

# write a function that tests "get_valid_piece_takes" function in Piece.py
def test_get_valid_piece_takes():
    # create a mock board with a one knight and a few pawns he can take
    board = MagicMock()
    board.get_piece = lambda row, col: Piece.Rook("rook", row, col, enums.Player.PLAYER_1)
    board.is_valid_piece = MagicMock(return_value=True)


    knight = Piece.Knight("knight", 3, 3, enums.Player.PLAYER_2)
    valid_takes = knight.get_valid_piece_takes(board)
    expected_takes = [(2, 1), (2, 5), (4, 1), (4, 5), (1, 2), (1, 4), (5, 2), (5, 4)]

    assert len(valid_takes) == len(expected_takes)

    for move in valid_takes:
        assert move in expected_takes

    # create a mock board with a one knight and a no pawns he can take

    board.get_piece = lambda row, col: enums.Player.EMPTY
    board.is_valid_piece = MagicMock(return_value=False)

    assert knight.get_valid_piece_takes(board) == []

    # create a mock board with a one knight and a few pawns he can take and a few he can't take

    function = cycle_values()
    board.get_piece = lambda row, col: next(function)(row, col)
    board.is_valid_piece = MagicMock(return_value=True)

    expected_takes = [(2, 1), (4, 1), (1, 2), (5, 4)]

    valid_takes = knight.get_valid_piece_takes(board)


    for move in valid_takes:
        assert move in expected_takes
    assert len(valid_takes) == len(expected_takes)








