#!/usr/bin/env python3
# -*- coding: utf-8 -*-

if __name__ == "__main__":
    filename = 'input.txt'
    with open(filename, 'r', encoding='utf-8') as f:
        text = f.read()

    num_dict = {'0': 'ноль', '1': 'один', '2': 'два', '3': 'три', '4': 'четыре',
                '5': 'пять', '6': 'шесть', '7': 'семь', '8': 'восемь', '9': 'девять'}

    for key, value in num_dict.items():
        text = text.replace(key, value)

    sentences = text.split('.')
    for sentence in sentences:
        if sentence.strip():
            print(sentence.strip() + '.')
    f.close()