
import chess_engine

def test_system():
    """
    test the system of the chess game
    :return: True if the black win
    """
    state_of_game = chess_engine.game_state()
    state_of_game.move_piece((1, 2), (2, 2), False)  # white
    state_of_game.move_piece((6, 3), (4, 3), False)  # black
    state_of_game.move_piece((1, 1), (3, 1), False)  # white
    state_of_game.move_piece((7, 4), (3, 0), False)  # black
    # The black should win so x suppose to be 0
    x = state_of_game.checkmate_stalemate_checker()
    assert x == 0