#!/usr/bin/env python3
#
# qfix.py:
#       Fix a batch of images in a certain folder
#
# Copyright (c) 2022
# Andres Eloy Rivera Garcia
#
# SPDX-License-Identifier: MIT
#
import os
import re
import subprocess

from PIL import Image

src_dir = './images'
dest_dir = './tmp'

for file in os.listdir(src_dir):
    file_path = os.path.join(src_dir, file)
    file_type = subprocess.run(['file', file_path], capture_output=True).stdout.decode()
    is_tiff = re.search(r'.*: TIFF', file_type) is not None
    if is_tiff:
        with Image.open(file_path) as im:
            im.rotate(-90).resize((128,128)).convert('RGB').save(os.path.join(dest_dir, file), 'JPEG')
