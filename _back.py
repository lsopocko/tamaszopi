"""SSD1351 demo (boundaries)."""
from time import sleep
from ssd1351 import Display, color565
from machine import Pin, SPI

btn_back = Pin(4, Pin.IN, Pin.PULL_UP)
btn_home = Pin(5, Pin.IN, Pin.PULL_UP)
btn_select = Pin(6, Pin.IN, Pin.PULL_UP)

menu_items = ["Feed", "Play", "Sleep", "Poop", "Settings"]
current_index = 0
selected = False

spi = SPI(2, baudrate=14500000, sck=Pin(7), mosi=Pin(9))
display = Display(spi, dc=Pin(2), cs=Pin(1), rst=Pin(3))

if not Pin(0, Pin.IN, Pin.PULL_UP).value():
    raise SystemExit  # skip main.py

def draw_menu():
    display.clear()  # clear screen
    for i, item in enumerate(menu_items):
        prefix = ">" if i == current_index else " "
        display.draw_text8x8(0, i * 12, f"{prefix} {item}", color565(255, 255, 255))  # white text

def handle_input():
    global current_index, selected

    if not btn_back.value():  # back = go up
        current_index = (current_index - 1) % len(menu_items)
        draw_menu()
        sleep(0.2)

    if not btn_home.value():  # home = go down
        current_index = (current_index + 1) % len(menu_items)
        draw_menu()
        sleep(0.2)

    if not btn_select.value():  # select = run
        selected = True
        draw_selected_action()
        sleep(0.5)

def draw_selected_action():
    display.clear()
    display.draw_text8x8(0, 0, f"Selected:", color565(255, 255, 255))
    display.draw_text8x8(0, 12, menu_items[current_index], color565(255, 255, 255))

def main_loop():
    
    
    draw_menu()
    while True:
        handle_input()

main_loop()
