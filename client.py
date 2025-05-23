import socket
import pickle
from tic_tac_toe import TicTacToe

HOST = '192.168.43.220'
PORT = 5015
SCORES_FILE = "scores.txt"
BUFFER_SIZE = 1024

def get_valid_coordinate(game):
    while True:
        coord = input("Enter coordinate (e.g., A1, B2): ").strip().upper()
        if coord in [f"{r}{c}" for r in "ABC" for c in "123"]:
            row = ord(coord[0]) - ord('A')
            col = int(coord[1]) - 1
            if game.symbol_list[row][col] == " ":
                return coord
            else:
                print("Square already taken. Try again.")
        else:
            print("Invalid format. Use A1, B2, etc.")

def send_data(sock, data):
    try:
        sock.send(pickle.dumps(data))
    except Exception as e:
        print(f"[Network Error] Could not send data: {e}")
        raise

def receive_data(sock):
    try:
        data = sock.recv(BUFFER_SIZE)
        return pickle.loads(data)
    except Exception as e:
        print(f"[Network Error] Could not receive data: {e}")
        raise

def update_scores(result):
    try:
        with open(SCORES_FILE, "a") as f:
            f.write(result + "\n")
    except Exception as e:
        print(f"[File Error] Could not update scores: {e}")

def display_score_history():
    print("======== YOUR HISTORY ========")
    try:
        with open(SCORES_FILE, 'r') as fin:
            for element in fin:
                print(element.strip())
    except FileNotFoundError:
        print("No previous games found.")

def main():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        s.connect((HOST, PORT))
        print(f"\nConnected to server at {HOST}:{PORT}!")
    except Exception as e:
        print(f"[Connection Error] Could not connect to server: {e}")
        return

    win, draw, lose = 0, 0, 0
    rematch = True

    while rematch:
        player_o = TicTacToe("O")
        print(f"\n\n=== T I C - T A C - T O E ===")
        player_o.draw_grid()
        print(f"\nWaiting for the other player...")

        try:
            x_symbol_list = receive_data(s)
            player_o.update_symbol_list(x_symbol_list)
        except Exception:
            print("Connection lost while waiting for opponent.")
            break

        while not player_o.did_win("O") and not player_o.did_win("X") and not player_o.is_draw():
            print(f"\nYour turn!")
            player_o.draw_grid()
            player_coord = get_valid_coordinate(player_o)
            player_o.edit_square(player_coord)
            player_o.draw_grid()
            try:
                send_data(s, player_o.symbol_list)
            except Exception:
                print("Connection lost while sending move.")
                rematch = False
                break
            if player_o.did_win("O") or player_o.is_draw():
                break
            print(f"\nWaiting for the other player...")
            try:
                x_symbol_list = receive_data(s)
                player_o.update_symbol_list(x_symbol_list)
            except Exception:
                print("Connection lost while receiving move.")
                rematch = False
                break

        if player_o.did_win("O"):
            print(f"Congrats, you won!")
            win += 1
            update_scores("client won")
        elif player_o.is_draw():
            print(f"It's a draw!")
            draw += 1
            update_scores("draw")
        else:
            print(f"Sorry, you lost.")
            lose += 1
            update_scores("client lost")

        display_score_history()
        print(f"Score: Won: {win} | Lost: {lose} | Draw: {draw}")

        # Rematch handshake
        while True:
            choice = input("Do you want a rematch? (y/n): ").strip().lower()
            if choice in ("y", "n"):
                try:
                    send_data(s, choice)
                    other_choice = receive_data(s)
                except Exception:
                    print("Connection lost during rematch negotiation.")
                    rematch = False
                    break
                if choice == "y" and other_choice == "y":
                    print("Both players agreed! Starting a new game.")
                    rematch = True
                    break
                else:
                    print("Rematch declined. Exiting.")
                    rematch = False
                    break
            else:
                print("Please enter 'y' or 'n'.")

    s.close()
    input(f"\nThank you for playing!\nPress enter to quit...\n")

if __name__ == "__main__":
    main()
