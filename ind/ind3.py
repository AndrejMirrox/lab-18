#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os

if __name__ == "__main__":
    folder_name = 'test_py'
    os.mkdir(folder_name)

    num_files = min(len(folder_name), 10)

    for i in range(1, num_files + 1):
        file_name = f"{i}.txt"
        file_path = os.path.join(folder_name, file_name)
        open(file_path, 'w').close()