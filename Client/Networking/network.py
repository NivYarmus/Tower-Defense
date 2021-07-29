import socket
import Networking.constants as constants


class Network:
    def __init__(self):
        """
        None -> None
        """
        self._client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.addr = (constants.IP, constants.PORT)

    def connect(self):
        """
        Connect to the server
        None -> None
        """
        self._client.connect(self.addr)

    def close(self):
        """
        Close the connection to the server
        None -> None
        """
        self._client.close()

    def send(self, data):
        """
        Send data to the server
        bytes -> None
        """
        length = str(len(data)).zfill(constants.LENGTH_SIZE).encode('utf-8')
        self.__send_on_loop(length + data)

    def receive(self):
        """
        Receive data from the server
        None -> bytes
        """
        length = self.__receive_on_loop(constants.LENGTH_SIZE)
        if length:
            return self.__receive_on_loop(int(length.decode()))
        return length

    def __send_on_loop(self, data):
        """
        Make sure all of the data is sent to the client
        bytes -> None
        """
        length = len(data)
        sent = 0
        while sent < length:
            size = self._client.send(data[sent:])
            sent += size

    def __receive_on_loop(self, size):
        """
        Make sure all of the data is received from the server
        int -> bytes
        """
        data = b''
        try:
            while len(data) < size:
                data += self._client.recv(size - len(data))
        except:
            pass
        return data
