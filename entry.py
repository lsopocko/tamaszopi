"""SSD1351 demo (boundaries)."""
from time import sleep
from ssd1351 import Display, color565
from machine import Pin, SPI

RED = const(0XF800)  # (255, 0, 0)
GREEN = const(0X07E0)  # (0, 255, 0)
WHITE = const(0XFFF)  # (255, 255, 255)

if not Pin(0, Pin.IN, Pin.PULL_UP).value():
    raise SystemExit  # skip main.py

def test():
    
    """Test code."""
    # Baud rate of 14500000 seems about the max 
    spi = SPI(2, baudrate=14500000, sck=Pin(7), mosi=Pin(9))
    display = Display(spi, dc=Pin(2), cs=Pin(1), rst=Pin(3))

    w = display.width
    h = display.height

    display.clear()

    display.draw_rectangle(0, 0, w, h, WHITE)
    sleep(5)

    display.fill_rectangle(0, 0, w, h, GREEN)
    sleep(5)

    display.draw_rectangle(0, 0, w, h, WHITE)

    sleep(10)
    display.cleanup()


test()