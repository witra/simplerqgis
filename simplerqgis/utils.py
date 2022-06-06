import os


def check_existing(path):
    if os.path.isfile(path):
        os.remove(path)

