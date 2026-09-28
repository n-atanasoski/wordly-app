import sys
import time
import pyperclip
from pynput import keyboard
import webbrowser
from urllib.parse import quote
from rich.console import Console

wordly_is_activated = True
logo = """                                                                                                                            
▄▄▄▄  ▄▄▄  ▄▄▄▄   ▄▄▄▄▄   ▄▄▄▄▄▄▄   ▄▄▄▄▄▄   ▄▄▄      ▄▄▄   ▄▄▄ 
▀███  ███  ███▀ ▄███████▄ ███▀▀███▄ ███▀▀██▄ ███      ███   ███ 
 ███  ███  ███  ███   ███ ███▄▄███▀ ███  ███ ███      ▀███▄███▀ 
 ███▄▄███▄▄███  ███▄▄▄███ ███▀▀██▄  ███  ███ ███        ▀███▀   
  ▀████▀████▀    ▀█████▀  ███  ▀███ ██████▀  ████████    ███   

------------------- Instant Word Definition -------------------                                                                                                                                                                          
"""

console = Console()

def get_word():
    time.sleep(0.1)
    word = pyperclip.paste().strip()
    if not word:
        return
    return word
def print_copied_word():
    console.print(f"[bold dodger_blue2]{get_word()}[/bold dodger_blue2] was copied")
def get_definition(word):
    if wordly_is_activated == True:
        url = f"https://dictionary.cambridge.org/dictionary/english/{quote(word)}"
        webbrowser.open(url)
    else:
        pass
def copy_word():
    word = get_word()
    if word:
        get_definition(word)
def quit_program():
     sys.exit()
def toggle_wordly():
    global wordly_is_activated
    if wordly_is_activated == True:
        wordly_is_activated = False
        console.print("Wordly has been [bold bright_red]deactivated[/bold bright_red]")
    else:
        wordly_is_activated = True
        console.print("Wordly has been [bold bright_green]activated[/bold bright_green]")

copy_hotkey = keyboard.HotKey(keyboard.HotKey.parse("<ctrl>+c"), copy_word)
toggle_hotkey = keyboard.HotKey(keyboard.HotKey.parse("<ctrl>+q"), toggle_wordly)
quit_hotkey = keyboard.HotKey(keyboard.HotKey.parse("<ctrl>+<shift>+q"), quit_program)
def on_press(key):
    key = listener.canonical(key)
    copy_hotkey.press(key)
    toggle_hotkey.press(key)
    quit_hotkey.press(key)
def on_release(key):
    key = listener.canonical(key)
    copy_hotkey.release(key)
    toggle_hotkey.release(key)
    quit_hotkey.release(key)

if __name__ == "__main__":
    console.print(f"[dodger_blue2]{logo}[/dodger_blue2]")
    console.print("[bold dodger_blue2]Enter[/bold dodger_blue2] to get definition on the last copied word")
    console.print("[bold dodger_blue2]Ctrl + C[/bold dodger_blue2] to copy a new selected word")
    console.print("[bold dodger_blue2]Ctrl + Q[/bold dodger_blue2] to toggle Wordly on and off")
    console.print("[bold dodger_blue2]Esc[/bold dodger_blue2] to quit the app")
    console.print("\n")
    console.print(f"[bold dodger_blue2]{get_word()}[/bold dodger_blue2] was found on your clipboard")
    with keyboard.GlobalHotKeys({"<ctrl>+c":print_copied_word, "<enter>":copy_word,"<ctrl>+q":toggle_wordly, "<esc>":quit_program}) as listener:
        listener.join()