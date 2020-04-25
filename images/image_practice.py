import re
from os import listdir
import os
from os.path import isfile, join, isdir

from PIL import Image

while True:
    images_folder = input('Please define images to convert folder - ')
    if not isdir(images_folder):
        print('Incorrect folder name, try again')
        continue
    break

new_folder = input('Please define new folder name to save images - ')
if not isdir(new_folder):
    os.mkdir(new_folder)

images = [f for f in listdir(images_folder) if isfile(join(images_folder, f))]
for image in images:
    img = Image.open(f'{images_folder}/{image}')
    name = os.path.splitext(image)[0]
    img.save(f'{new_folder}/{name}.png', 'png')
