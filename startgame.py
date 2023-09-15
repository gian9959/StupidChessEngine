import minimax
import chess
import stateClass

MIN_INF = -float('inf')
MAX_INF = float('inf')


def play(state, depth):
    print("STARTING GAME")
    print("ENGINE DEPTH: ", end='')
    print(depth)
    print("------------------------------------------")
    autoplay = False
    while not state.is_game_over():
        print()
        if state.minichess:
            i = 0
            for sq in stateClass.m_squares:
                i = i + 1
                p = state.board.piece_at(sq)
                if p is not None:
                    print(p, end=' ')
                else:
                    print(".", end=' ')
                if i == 5:
                    i = 0
                    print()
        else:
            print(state.board)
        print()
        if state.is_opponent_turn():
            print("player turn")
            if not autoplay:
                print("make a move", end='')
                if state.board.fullmove_number > 1:
                    print("\nor type 'undo' to return to your previous move", end='')
                print(":")
                move_string = input()
            if move_string == "autoplay" or autoplay:
                autoplay = True
                print("Calculating move for player...")
                best_value = MAX_INF
                alpha = MIN_INF
                beta = MAX_INF
                moves = state.get_ordered_moves()
                for move in moves:
                    state.board.push(move)
                    value = minimax.minimax(state, depth, alpha, beta, True)
                    state.board.pop()
                    if value < best_value:
                        best_value = value
                        state.best_move = move
                    if best_value <= alpha:
                        break
                    beta = min(beta, best_value)
                    if beta <= alpha:
                        break
                print("Evaluation: ", end='')
                print(best_value)
                state.make_best()
                print(state.counter, end=' ')
                print("minimax iterations")
                state.counter = 0
                print()
                print(state.best_move)
                if state.board.is_check():
                    print("check!")
            elif move_string == "undo":
                if state.board.fullmove_number > 1:
                    state.board.pop()
                    state.board.pop()
                else:
                    print("Cannot undo move now!")
            else:
                try:
                    move_in = chess.Move.from_uci(move_string)
                    if move_in in state.get_legal_moves():
                        state.board.push(move_in)
                        if state.board.is_check():
                            print("check!")
                    else:
                        raise chess.InvalidMoveError
                except chess.InvalidMoveError:
                    print("Not a valid move!")
            print("------------------------------------------")
        else:
            print("engine turn")
            print("Calculating move...")
            best_value = MIN_INF
            alpha = MIN_INF
            beta = MAX_INF
            moves = state.get_ordered_moves()
            for move in moves:
                state.board.push(move)
                value = minimax.minimax(state, depth, alpha, beta, False)
                state.board.pop()
                if value > best_value:
                    best_value = value
                    state.best_move = move
                if best_value >= beta:
                    break
                alpha = max(alpha, best_value)
                if beta <= alpha:
                    break
            print("Evaluation: ", end='')
            print(best_value)
            state.make_best()
            print(state.counter, end=' ')
            print("minimax iterations")
            state.counter = 0
            print()
            print(state.best_move)
            if state.board.is_check():
                print("check!")
    print()
    if state.minichess:
        i = 0
        for sq in stateClass.m_squares:
            i = i + 1
            p = state.board.piece_at(sq)
            if p is not None:
                print(p, end=' ')
            else:
                print(".", end=' ')
            if i == 5:
                i = 0
                print()
    else:
        print(state.board)
    print()


m_input = input("Are you playing minichess (5x5 board)? y/n\n")
if m_input == "y":
    print("Playing minichess!")
    board = chess.Board("8/8/8/rnbqk3/ppppp3/8/PPPPP3/RNBQK3")
    m = True
else:
    print("Playing standard chess!")
    board = chess.Board()
    m = False

c = input("What side is the engine playing? w/b\n")

if c == "w":
    print("\nEngine playing as white...")
    print("Player playing as black...")
    s = stateClass.State(board, True, m)
elif c == "b":
    print("\nEngine playing as black...")
    print("Player playing as white...")
    s = stateClass.State(board, False, m)
else:
    print("\nNot a valid color! Standard color is white")
    print("\nEngine playing as white...")
    print("Player playing as black...")
    s = stateClass.State(board, True, m)

if m:
    MAX_DEPTH = 6
else:
    MAX_DEPTH = 4

play(s, MAX_DEPTH)
input("Press any key to exit...")
