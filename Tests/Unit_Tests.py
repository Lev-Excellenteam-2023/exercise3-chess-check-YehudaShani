import pytest
import Piece
import chess_engine
from unittest.mock import MagicMock, Mock, patch
import enums


def cycle_values():
    while True:
        values = [lambda row, col: Piece.Rook("rook", row, col, enums.Player.PLAYER_1),
                  lambda row, col: Piece.Rook("rook", row, col, enums.Player.PLAYER_2)]
        for value in values:
            yield value


def half_empty_board():
    mock = MagicMock()
    mock.get_player = MagicMock(return_value=enums.Player.PLAYER_1)
    while True:
        values = [lambda row, col:mock,
                  lambda row, col: Piece.Rook("rook", row, col, enums.Player.PLAYER_1)]
        for value in values:
            yield value

def check_valid(row, col):
    return (row, col) in [(2, 1), (4, 1), (1, 4), (5, 4)]


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


def test_get_valid_peaceful_moves1():
    # create a mock board with a one knight and no pieces around him
    board = MagicMock()
    board.get_piece = lambda row, col: enums.Player.EMPTY
    board.is_valid_piece = MagicMock(return_value=True)

    knight = Piece.Knight("knight", 3, 3, enums.Player.PLAYER_2)

    valid_moves = knight.get_valid_peaceful_moves(board)
    expected_moves = [(2, 1), (2, 5), (4, 1), (4, 5), (1, 2), (1, 4), (5, 2), (5, 4)]

    assert len(valid_moves) == len(expected_moves)
    for move in valid_moves:
        assert move in expected_moves


def test_get_valid_peaceful_moves2():
    # create a mock board with a one knight and a pieces on all the places he can move
    function = cycle_values()
    board = MagicMock()
    board.get_piece = lambda row, col: next(function)(row, col)
    board.is_valid_piece = MagicMock(return_value=True)

    knight = Piece.Knight("knight", 3, 3, enums.Player.PLAYER_2)

    valid_moves = knight.get_valid_peaceful_moves(board)

    assert len(valid_moves) == 0


def test_get_valid_peaceful_moves3():
    # create a mock board with a one knight and a pieces on all the places he can move
    function = half_empty_board()
    board = MagicMock()
    board.get_piece = lambda row, col: next(function)(row, col)
    board.is_valid_piece = MagicMock(return_value=True)

    knight = Piece.Knight("knight", 3, 3, enums.Player.PLAYER_2)

    valid_moves = knight.get_valid_peaceful_moves(board)

    expected_moves = [(2, 1),  (4, 1),  (1, 2),  (5, 4)]

    assert len(valid_moves) == len(expected_moves)
    for move in valid_moves:
        assert move in expected_moves

