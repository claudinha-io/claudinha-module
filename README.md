# Claudinha Module [![Build Status](https://travis-ci.org/claudinha-io/claudinha-module.svg?branch=master)](https://travis-ci.org/claudinha-io/claudinha-module)
Experimentos com uma pequena nuvem com Raspberry Pi e Unicorn Hat

*Requisitos*
- bitarray - 0.8.1
- py - 1.4.34
- pytest - 3.1.3
- unicornhat - 2.1.3

## Comandos via terminal

### Mostrar um Teste no UH
`python3 ascii_text.py`

### Mostrar um texto com cor padrão no UH
`python3 ascii_text.py <texto>`

### Mostrar um texto com cor especifica no UH
`python3 ascii_text.py <cor> <texto>`

- white => rgb(255, 255, 255) => #FFFFFF
- red => rgb(255, 0, 0) => #FF0000
- green => rgb(0, 255, 0) => #00FF00
- blue => rgb(0, 0, 255) => #0000FF
- yellow => rgb(255, 255, 0) => #FFFF00
- cyan => rgb(0, 255, 255) => #00FFFF
- magenta => rgb(255, 0, 255) => #FF00FF
