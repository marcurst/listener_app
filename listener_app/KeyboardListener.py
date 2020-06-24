from pynput.keyboard import Listener as keyboard
from listener_app.backend import Database

db = Database("Keyboards.db")


keys = {
    "Key.esc": 0,
    "Key.f1": 0,
    "Key.f2": 0,
    "Key.f3": 0,
    "Key.f4": 0,
    "Key.f5": 0,
    "Key.f6": 0,
    "Key.f7": 0,
    "Key.f8": 0,
    "Key.f9": 0,
    "Key.f10": 0,
    "Key.f11": 0,
    "Key.f12": 0,
    "Key.print_screen": 0,
    "Key.scroll_lock": 0,
    "Key.pause": 0,
    "'`'": 0,
    "'1'": 0,
    "'2'": 0,
    "'3'": 0,
    "'4'": 0,
    "'5'": 0,
    "'6'": 0,
    "'7'": 0,
    "'8'": 0,
    "'9'": 0,
    "'0'": 0,
    "'='": 0,
    "Key.backspace": 0,
    "Key.tab": 0,
    "'q'": 0,
    "'w'": 0,
    "'e'": 0,
    "'r'": 0,
    "'t'": 0,
    "'y'": 0,
    "'u'": 0,
    "'i'": 0,
    "'o'": 0,
    "'p'": 0,
    "'['": 0,
    "']'": 0,
    "'\\'": 0,
    "'a'": 0,
    "'s'": 0,
    "'d'": 0,
    "'f'": 0,
    "'g'": 0,
    "'h'": 0,
    "'j'": 0,
    "'k'": 0,
    "l'": 0,
    "';'": 0,
    "\"\'\"": 0,
    "Key.shift_r": 0,
    "Key.enter": 0,
    "Key.shift": 0,
    "'z'": 0,
    "'x'": 0,
    "'c'": 0,
    "'v'": 0,
    "'b'": 0,
    "'n'": 0,
    "'m'": 0,
    "','": 0,
    "'.'": 0,
    "Key.ctrl_l": 0,
    "Key.cmd": 0,
    "Key.alt_l": 0,
    "Key.space": 0,
    "Key.alt_r": 0,
    "Key.cmd_r": 0,
    "Key.menu": 0,
    "Key.ctrl_r": 0,
    "Key.insert": 0,
    "Key.home": 0,
    "Key.page_up": 0,
    "Key.end": 0,
    "Key.page_down": 0,
    "Key.left": 0,
    "Key.up": 0,
    "Key.right": 0,
    "Key.down": 0,
    "Key.num_lock": 0,
    "'/'": 0,
    "'*'": 0,
    "'-'": 0,
    "'+'": 0,
    "<12>": 0,
    "Key.delete": 0,
    "clicked": 0,
}

def WriteToFile(key):
    print(key)

keyboard(on_release=WriteToFile).start()