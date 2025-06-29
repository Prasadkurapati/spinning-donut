import math
import time
from threading import Thread
from pynput import keyboard
from colorama import init, Fore, Style
import shutil
import random

init()

A, B = 0, 0
speed_A = 0.04
speed_B = 0.08
adjust = {"delta": 0.0}
last_output = [' '] * 1760

# Handle arrow keys
def on_press(key):
    try:
        if key == keyboard.Key.up:
            adjust["delta"] += 0.005
        elif key == keyboard.Key.down:
            adjust["delta"] -= 0.005
    except:
        pass

listener = keyboard.Listener(on_press=on_press)
listener.start()

def donut_color_map(char):
    sprinkle_chars = ['*', '@', '!', '$']
    if char in sprinkle_chars:
        return random.choice([
            Fore.RED, Fore.YELLOW, Fore.BLUE, Fore.LIGHTCYAN_EX,
            Fore.LIGHTGREEN_EX, Fore.MAGENTA, Fore.LIGHTMAGENTA_EX
        ])
    pink_frosting = [".", ",", "-", "~", ":", ";", "="]
    if char in pink_frosting:
        return Fore.LIGHTMAGENTA_EX
    if char in ["#", "$"]:
        return Fore.YELLOW
    if char == "@":
        return Fore.WHITE
    return Fore.LIGHTBLACK_EX  # donut body

print('\x1b[2J', end='')  # Clear screen once

while True:
    output = [' '] * 1760
    zbuffer = [0] * 1760

    for j in range(0, 628, 7):  # theta
        for i in range(0, 628, 2):  # phi
            c = math.sin(i / 100)
            d = math.cos(j / 100)
            e = math.sin(A)
            f = math.sin(j / 100)
            g = math.cos(A)
            h = d + 2
            D = 1 / (c * h * e + f * g + 5)
            l = math.cos(i / 100)
            m = math.cos(B)
            n = math.sin(B)
            t = c * h * g - f * e
            x = int(40 + 30 * D * (l * h * m - t * n))
            y = int(12 + 15 * D * (l * h * n + t * m))
            o = int(x + 80 * y)
            N = int(8 * ((f * e - c * d * g) * m - c * d * e - f * g - l * d * n))
            if 1760 > o > 0 and D > zbuffer[o]:
                zbuffer[o] = D
                output[o] = ".,-~:;=!*#$@"[N if N > 0 else 0]

    # Motion trail blending
    final_output = []
    for i in range(1760):
        if output[i] != ' ':
            final_output.append(output[i])
        elif last_output[i] != ' ':
            final_output.append('.')
        else:
            final_output.append(' ')
    last_output = output.copy()

    # Centering
    terminal_width = shutil.get_terminal_size((80, 20)).columns
    padding = max((terminal_width - 80) // 2, 0)
    pad = ' ' * padding

    # Print to screen with color
    print('\x1b[H', end='')  # Move to top-left
    for i in range(0, 1760, 80):
        line = ''.join(final_output[i:i + 80])
        colored_line = ''.join(donut_color_map(c) + c if c.strip() else ' ' for c in line)
        print(pad + colored_line + Style.RESET_ALL)

    # Show speed
    print(pad + Fore.LIGHTBLACK_EX + f"Speed A: {speed_A:.3f} | Speed B: {speed_B:.3f} (⬆️ / ⬇️ to control)" + Style.RESET_ALL)

    # Speed adjustment
    delta = adjust["delta"]
    speed_A = max(0.005, speed_A + delta)
    speed_B = max(0.005, speed_B + delta)
    adjust["delta"] = 0.0

    A += speed_A
    B += speed_B
    time.sleep(0.03)