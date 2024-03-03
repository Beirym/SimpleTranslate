import time
import keyboard
import pyperclip
import plyer.platforms.win.notification
from plyer import notification
import alphabets

lang = alphabets.eng_to_rus


def translate():
    clipboard_obj = pyperclip.paste()

    translated_letters = []
    for letter in list(clipboard_obj):
        if (letter in lang.keys()):
            translated_letters.append(lang[letter])

    pyperclip.copy(''.join(translated_letters))
    last_clipboard_obj = clipboard_obj

    notification.notify(
        title="The text has been translated",
        message="The text from the clipboard has been translated into your chosen language and copied!",
        timeout = 10,
        app_name="SimpleTranslate",
    )


if __name__ == '__main__':
    while True:
        keyboard.wait('CTRL+T')
        translate()

