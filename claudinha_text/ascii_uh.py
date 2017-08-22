#!/usr/bin/env python
# -*- coding: latin-1 -*-

try:
    import unicornhat as unicorn
    
    unicorn.set_layout(unicorn.AUTO)
    unicorn.rotation(270)
    unicorn.brightness(0.5)
except ImportError as identifier:
    pass




def set_pixel(width, height, red, green, blue):
    """
    Exibe os pixels nas posições corretas no display do Unicorn Hat.

    Aplica na posição determinada na posição indicada por width e height a cor indicada RGB.

    Args:
        width (decimal): Posição horizontal
        height (decimal): Posição vertical
        red (decimal): Cor para exibição no display.
        green (decimal): Cor para exibição no display.
        blue (decimal): Cor para exibição no display.

    """
    try:
        unicorn.set_pixel(width, height, red, green, blue)
    except Exception as identifier:
        print(identifier)


def show_pixels():
    """
    Exibe os pixels nas posições corretas no display do Unicorn Hat.
    """
    try:
        unicorn.show()
    except Exception as identifier:
        print(identifier)
