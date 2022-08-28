from plyer import notification
import time

if __name__ := "__main__":
    while True:
        notification.notify( title="Hello, An Important Message",
                             message="Be kind to yourself", timeout=5)
        time.sleep(10)



