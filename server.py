import socket
from _thread import *
from player import Player
import pickle

server = "127.0.0.1"
port = 5555

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    s.bind((server, port))
except socket.error as e:
    str(e)

s.listen(2)
print("Server started, waiting for a connection")

players = [Player(200, 600, 50, 50, (255, 0, 0)), Player(600, 200, 50, 50, (0, 255, 0))]


def threaded_client(conn, player):
    conn.send(pickle.dumps(players[player]))
    reply = ""
    while True:
        print(str(players[0].rect.x))
        try:
            data = pickle.loads(conn.recv(2048))
            players[player] = data

            if not data:
                print("Disconnected")
                break
            else:
                if player == 1:
                    reply = players[0]
                else:
                    reply = players[1]

                # print("Received: ", data)
                # print("Sending: ", reply)

            conn.sendall(pickle.dumps(reply))
        except:
            break

    print("Lost Connection")
    conn.close()


current_player = 0
while True:
    conn, addr = s.accept()
    print("Connected to: ", addr)

    start_new_thread(threaded_client, (conn, current_player))
    current_player += 1
