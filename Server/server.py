from threading import Thread, Lock

from Networking.network import Network
from Protocol.protocol_handle import break_message, handle_client_message, create_message
from Protocol.constants import CLIENT_QUIT_PROTOCOL
from Protocol.game_generator import create_game


network = Network()
thread_lock = Lock()
games = {}
open_key = '0'
queue = []


def thread_loop(game_key, player_id):
    global network
    global games

    thread_lock.acquire()
    socket1, game1 = games[game_key][player_id]
    socket2, game2 = games[game_key][2 if player_id == 1 else 1]
    network.send(socket1, create_message((game1, game2))) # send the play the starting game position
    thread_lock.release()

    while game1.health > 0 and game2.health > 0:
        thread_lock.acquire()
        if not game1.wave.balloons and not game2.wave.balloons: # if both players cleared thier waves summon a new wave
            game1.wave.next_wave(game1)
            game2.wave.next_wave(game2)
        thread_lock.release()

        try:
            data = network.receive(socket1)
            if not data or data == CLIENT_QUIT_PROTOCOL:
                game1.health = 0
                break

            thread_lock.acquire()
            protocol, data = break_message(data)
            handle_client_message(game1, protocol, data)
            network.send(socket1, create_message((game1, game2)))
            thread_lock.release()
        except:
            break
    
    thread_lock.acquire()
    try:
        network.send(socket1, create_message((game1, game2)))
    except:
        pass
    finally:
        print('PLAYER DISCONNECTED')
        game1.stop_game()
        game1.running = False
        socket1.close()
        if not game2.running:
            games.pop(game_key)
            print(f'Closing game #{game_key}')
    thread_lock.release()


def create_new_game():
    global network
    global queue
    global games
    global open_key

    print(f'Creating game #{open_key}')
    game1, game2 = create_game()
    player1, player2 = queue.pop(0), queue.pop(0)
    player1_thread, player2_thread = Thread(target=thread_loop, args=(open_key, 1)), Thread(target=thread_loop, args=(open_key, 2))
    games[open_key] = {1: (player1, game1), 2: (player2, game2)}
    open_key = str(int(open_key) + 1) # mark the current key as taken and switch to a not taken key
    player1_thread.start()
    player2_thread.start()


def main():
    global network
    global thread_lock
    global games
    global queue
    
    try:
        network.init() # start the server
        print('SERVER STARTED')
        while True:
            skt = network.accept()[0] # accept a connection
            print('PLAYER CONNECTED')
            queue.append(skt) # add the socket to a list of sockets waiting for an opponent

            thread_lock.acquire()
            if len(queue) >= 2:
                create_new_game()
            thread_lock.release()
    except Exception as e:
        print(e)


if __name__ == '__main__':
    main()
