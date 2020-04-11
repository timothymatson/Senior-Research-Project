import glob
import os

files = glob.glob(os.path.join(os.getcwd(), '*'))

try:
    os.mkdir('renamed')
except FileExistsError:
    pass

counter = 1
for f in files:
    if os.path.isdir(f):
        continue

    ext = os.path.splitext(f)[1]
    new_file = f'{counter:03}{ext}'
    os.rename(f, os.path.join('renamed', new_file))
    counter += 1
