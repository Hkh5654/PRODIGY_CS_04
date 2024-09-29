# PRODIGY_CS_04

Keylogger Script

This script implements a basic keylogger using the pynput library to capture and log keystrokes on a system. It records each key pressed by the user and saves the keystrokes in a text file for logging purposes.

How It Works:

Keystroke Capture:

The script listens for each keypress using the pynput.keyboard.Listener class.

Every key pressed is written to a log file located at a specified path on the system.

Log File:

Keystrokes are logged in the file keylog.txt. Special keys (like space, enter, backspace, shift, control, etc.) are logged with specific labels, while regular characters are logged as they are typed.

Handling Special Keys:

Spaces are logged as ' '.

Enter key presses are logged as a new line.

Backspaces, shifts, control keys, and other special keys are logged with labels like [BACKSPACE], [SHIFT], [CTRL], and [ALT].

Stopping the Logger:

The keylogger runs until the user presses the ESC key, which stops the listener and ends the logging process.

Key Features:

Keystroke Logging: Captures and logs every key pressed, including special keys.

Real-time Logging: Logs the keys in real-time to a text file.

Customizable Log Path: The file path where keystrokes are saved can be easily modified.
Real-time Logging: Logs the keys in real-time to a text file.
Customizable Log Path: The file path where keystrokes are saved can be easily modified.
