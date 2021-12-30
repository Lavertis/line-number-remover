import string
import os

import keyboard
import pyperclip
from datetime import datetime


def process_text(text):
    lines = text.split('\n')
    text = ""
    for line in lines:
        text += line.lstrip(string.digits + '.').strip(' ') + '\n'
    text.rstrip('\n')
    return text


def cls():
    os.system('cls' if os.name == 'nt' else 'clear')


def show_console_info():
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    cls()
    print("Last used: ", current_time)


def callback():
    text = pyperclip.paste()
    text = process_text(text)
    pyperclip.copy(text)
    show_console_info()


def main():
    keyboard.add_hotkey("ctrl+shift", callback)
    try:
        keyboard.wait()
    except KeyboardInterrupt:
        pass


if __name__ == '__main__':
    main()
