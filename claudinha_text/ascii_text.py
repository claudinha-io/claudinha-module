#!/usr/bin/env python3

import sys
import json
import os

from claudinha_text.ascii_screen import scroll_display
from claudinha_text.ascii_converter import appendLetterToPhrase, splitLettersOfMessage

with open(os.path.join(os.path.dirname(__file__), 'colors.json')) as json_data:
    colors = json.load(json_data)

def validate_args(user_input):
    if len(user_input) < 2:
        print(len(user_input))
        return ["Teste"]
    elif len(user_input) > 2 and user_input[1] in colors["rgb"]:
        print(len(user_input))
        return [" ".join(user_input[2:]), user_input[1]]
    else:
        return [" ".join(user_input[1:])]

def main(args):
    try:
        validated_text = validate_args(args)
    except AttributeError as error:
        print("Entrada invalida.", error)
    if len(validated_text) == 1:
        text = appendLetterToPhrase(splitLettersOfMessage(validated_text[0]))
        scroll_display(text)
    if len(validated_text) == 2:
        text = appendLetterToPhrase(splitLettersOfMessage(validated_text[0]))
        scroll_display(text, validated_text[1])

if __name__ == '__main__':
    main(sys.argv)
