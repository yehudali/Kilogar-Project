import manager
import time


def Main():
    while True:
        man = manager.Manager()
        man.start()
        time.sleep(20)

if __name__ == "__main__":
    Main()






