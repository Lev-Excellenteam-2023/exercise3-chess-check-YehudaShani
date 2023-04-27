import pytest
import Piece
import ai_engine
import chess_engine
from unittest.mock import MagicMock, Mock, patch
import enums
import Unit_Tests

def test_get_valid_piece_moves():
    # create a mock board with a one knight and a few pawns he can take
    board = MagicMock()
    function = Unit_Tests.half_empty_board()
    board.get_piece = lambda row, col: next(function)(row, col)
    board.is_valid_piece = MagicMock(return_value=True)
    knight = Piece.Knight("knight", 3, 3, enums.Player.PLAYER_2)
    valid_moves = knight.get_valid_piece_moves(board)
    expected_moves = [(2, 1), (2, 5), (4, 1), (4, 5), (1, 2), (1, 4), (5, 2), (5, 4)]

    assert len(valid_moves) == len(expected_moves)

    for move in valid_moves:
        assert move in expected_moves


def test_evaluate_board():
    board = chess_engine.game_state()
    board.is_valid_piece = MagicMock(return_value=True)
    board.get_piece = MagicMock(return_value = Piece.Pawn("pawn", 3, 3, enums.Player.PLAYER_2))

    evaluation = ai_engine.chess_ai.evaluate_board(board, enums.Player.PLAYER_2)

    assert evaluation == 64

