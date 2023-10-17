# 17- A Good Example of Inheritance

class InvalidOperationError(Exception):
    pass

class Stream:
    def __init__(self):
        self.opened = False

    def open(self):
        if self.opened:
            raise InvalidOperationError('Stream is already open.')
        self.opened = True

    def close(self):
        if not self.open:
            raise InvalidOperationError('Stream is already closed.')
        self.opened = False

class FileStream(Stream):
    def read(self):
        print('Reading data from file')

class NetworkStream(Stream):
    def read(self):
        print('Reading data from network.')