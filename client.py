from os import fdopen
import socket
import pickle

from tic_tac_toe import TicTacToe

HOST = '192.168.43.220'  
PORT = 5015
win=0
draw=0
lose=0

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))
print(f"\nConnected to {s.getsockname()}!")

player_o = TicTacToe("O")

rematch = True

while rematch == True:
    print(f"\n\n T I C - T A C - T O E ")

    player_o.draw_grid()

    print(f"\nWaiting for other player...")
    x_symbol_list = s.recv(1024)
    x_symbol_list = pickle.loads(x_symbol_list)
    player_o.update_symbol_list(x_symbol_list)

    while player_o.did_win("O") == False and player_o.did_win("X") == False and player_o.is_draw() == False:
        print(f"\n       Your turn!")
        player_o.draw_grid()
        player_coord = input(f"Enter coordinate: ")

        player_o.edit_square(player_coord)

        player_o.draw_grid()

        o_symbol_list = pickle.dumps(player_o.symbol_list)
        s.send(o_symbol_list)

        if player_o.did_win("O") == True or player_o.is_draw() == True:
            break

        print(f"\nWaiting for other player...")
        x_symbol_list = s.recv(1024)
        x_symbol_list = pickle.loads(x_symbol_list)
        player_o.update_symbol_list(x_symbol_list)
    if player_o.did_win("O") == True:
        print(f"Congrats, you won!")
        f = open("scores.txt", "a")
        f.write("client won\n")
        fin = open('scores.txt', 'r')
        print("========YOUR HISTORY========")
        for element in fin:   
            print(element)     
        f.close()
    elif player_o.is_draw() == True:
        print(f"It's a draw!")
        f = open("scores.txt", "a")
        f.write("draw\n")
        fin = open('scores.txt', 'r')
        print("=====YOUR HISTORY======")
        for element in fin:   
            print(element)        
        f.close()        
    else:
        print(f"Sorry, the host won.")
        f = open("scores.txt", "a")
        f.write("client lost\n")
        fin = open('scores.txt', 'r')
        print("====YOUR HISTORY======")
        for element in fin:   
            print(element)
        f.close()
    # if player_o.did_win("O") == True:
    #     print(f"Congrats, you won!")
    #     f = open("scores.txt", "a")
        
    #     # content = f.read()
    #     # print(content)
    #     # fin = open('scores.txt', 'r')
    #     # for element in fin:

    #     #     if element=='1':
    #     #         win=win+1
            
    #     #     elif element=='2':
    #     #         lose=lose+1
            
    #     #     else:
    #     #         draw=draw+1
            
    #     # f.close()
    #     print(win, 'matches won')
    #     # print(lose, 'matches lost')
    #     # print(draw, 'matches drawn')

    # elif player_o.is_draw() == True:
    #     print(f"It's a draw!")
    #     # f = open("scores.txt", "a")
    #     # f.write("3\n")
    #     # fin = open('scores.txt', 'r')
    #     # for element in fin:

    #     #     if element=='1':
    #     #         win=win+1
            
    #     #     elif element=='2':
    #     #         lose=lose+1
            
    #     #     else:
    #     #         draw=draw+1
            
    #     # f.close()
    #     print(win, 'matches won')
    #     # print(lose, 'matches lost')
    #     # print(draw, 'matches drawn')
     
    # else:
    #     print(f"Sorry, the host won.")
    #     # f = open("scores.txt", "a")
    #     # f.write("2\n")
    #     # fin = open('scores.txt', 'r')
    #     # for element in fin:

    #     #     if element=='1':
    #     #         win=win+1
            
    #     #     elif element=='2':
    #     #         lose=lose+1
            
    #     #     else:
    #     #         draw=draw+1
            
    #     # f.close()
    #     print(win, 'matches won')
    #     # print(lose, 'matches lost')
    #     # print(draw, 'matches drawn')
 
    client_response = "N"

    if True:
        print(f"\nWould you like a rematch??")
        client_response = input("(Y/N): ")
        client_response = client_response.capitalize()
        temp_client_resp = client_response

        client_response = pickle.dumps(client_response)
        s.send(client_response)

        if temp_client_resp == "Y":
            player_o.restart()

        else:
            rematch = False

    else:
        print(f"\nThe host does not want a rematch.")
        rematch = False

spacer = input(f"\nThank you for playing!\nPress enter to quit...\n")

s.close()