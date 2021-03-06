#!/usr/bin/env python
# -*- coding: latin-1 -*-

from claudinha_text.ascii_uh import set_pixel, show_pixels
from time import sleep
from itertools import product as matriz
import json, logging, os

width = range(8)
height = range(8)
inverted_height = list(reversed(height))

with open(os.path.join(os.path.dirname(__file__), 'colors.json')) as json_data:
    colors = json.load(json_data)

def show_phrase_on_display(phrase, color):
    """
    Exibe os pixels nas posições corretas no display do Unicorn Hat.

    Cria uma lista contendo os valores RGB da cor escolhida e aplica as \
    posições dos pixels determinadas na matriz bidirecional 'phrase' e por \
    fim exibe no display.

    Args:
        phrase (list[bitarray]): Frase em formato de bitarray
        color (string): Cor para exibição no display. Padrão: Branco
    """
    
    rgb = []
    if color in colors["rgb"]:
        rgb = colors["rgb"][color].split(',')
    else:
        rgb = colors["rgb"]['white'].split(',')
    for w, h in matriz(width, height):
        if phrase[w][h]:
            set_pixel(w, inverted_height[h], int(rgb[0]), int(rgb[1]), int(rgb[2]))
        else:
            set_pixel(w, inverted_height[h], 0, 0, 0)
    show_pixels()


def scroll_display(phrase, color='white'):
    """
    Exibe a frase em scroll no display do Unicorn Hat.

    Executa um loop percorrendo todo o comprimento da matriz bidimensional \
    'phrase' pela altura do display. Dentro do loop chama o método show() \
    passando o objeto 'phrase' e a string color como parametro, para exibir \
    os pixels nas posições corretas no display. Depois elimina o conteudo da \
    primeira posição de cada linha da matriz e completa com 0 o final da \
    lista, mantendo o comprimento.

    Args:
        phrase (list[bitarray]): Frase em formato de bitarray
        color (string): Cor para exibição no display. Padrão: Branco

    """
    for i, collum_position in matriz(range(len(phrase[0])), height):
        logging.debug(["Position:", i, collum_position])
        show_phrase_on_display(phrase, color)
        phrase[collum_position].pop(0)
        phrase[collum_position].append(0)
        sleep(0.01)
