#!/usr/bin/env python3

import sys
import json

from claudinha_text.ascii_screen import scroll_display
from claudinha_text.ascii_converter import step, message

with open('./claudinha_text/colors.json') as json_data:
    colors = json.load(json_data)

def validate_args(user_input):
    if len(user_input) < 2:
        print(len(user_input))
        return 'Teste'
    elif len(user_input) > 2 and user_input[1] in colors["rgb"]:
        print(len(user_input))
        return " ".join(user_input[2:]), user_input[1]
    else:
        return " ".join(user_input[1:])

if __name__ == '__main__':
    validated_text = validate_args(sys.argv)
    with validated_text:
        if len(validated_text) == 1:
            text = step(message(validated_text))
            scroll_display(text)
        if len(validated_text) == 2:
            text = step(message(validated_text[0]))
            scroll_display(text, validated_text[1])
