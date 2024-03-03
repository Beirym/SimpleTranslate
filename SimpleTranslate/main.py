import time
import keyboard
import pyperclip
from win10toast import ToastNotifier
import alphabets

lang = alphabets.eng_to_rus
toast = ToastNotifier()


def translate():
    clipboard_obj = pyperclip.paste()

    translated_letters = []
    for letter in list(clipboard_obj):
        if (letter in lang.keys()):
            translated_letters.append(lang[letter])

    pyperclip.copy(''.join(translated_letters))
    last_clipboard_obj = clipboard_obj

    toast.show_toast(
        "The text has been translated",
        "The text from the clipboard has been translated into your chosen language and copied!",
        duration = 10,
    )


if __name__ == '__main__':
    while True:
        keyboard.wait('CTRL+T')
        translate()

