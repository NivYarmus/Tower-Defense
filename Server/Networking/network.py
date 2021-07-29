import socket
import Networking.constants as constants


class Network:
    def __init__(self):
        """
        None -> None
        """
        self._server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.addr = (constants.IP, constants.PORT)

    def init(self):
        """
        Start the server
        None -> None
        """
        self._server.bind(self.addr)
        self._server.listen()

    def close(self):
        """
        Close the server socket
        None -> None
        """
        self._server.close()

    def accept(self):
        """
        Accept a connection to the server
        None -> None
        """
        return self._server.accept()

    def send(self, skt, data):
        """
        Send data to a client
        socket.socket, bytes -> None
        """
        length = str(len(data)).zfill(constants.LENGTH_SIZE).encode()
        self.__send_on_loop(skt, length + data)

    def receive(self, skt):
        """
        Receive data from a client
        socket.socket -> bytes
        """
        skt.settimeout(constants.TIMEOUT)
        length = self.__receive_on_loop(skt, constants.LENGTH_SIZE)
        if length:
            return self.__receive_on_loop(skt, int(length.decode()))
        return b''

    def __send_on_loop(self, skt, data):
        """
        Make sure all of the data is sent to the client
        socket.socket, bytes -> None
        """
        length = len(data)
        sent = 0
        while sent < length:
            size = skt.send(data[sent:])
            sent += size
    
    def __receive_on_loop(self, skt, size):
        """
        Make sure all of the data is received from the client
        socket.socket, int -> bytes
        """
        data = b''
        try:
            while len(data) < size:
                data += skt.recv(size - len(data))
        except:
            pass
        return data
