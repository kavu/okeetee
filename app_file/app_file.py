# coding=utf-8
import os

from werkzeug.utils import secure_filename

from utils import get_random


class AppFile:
    def __init__(self, file):
        self.__file = file
        self.saved = False
        self.save_path = None

    def __get_original_filename(self):
        return secure_filename(self.__file.filename)

    original_filename = property(__get_original_filename)

    def __get_ext(self):
        ext_tuple = os.path.splitext(self.original_filename)

        return ext_tuple[len(ext_tuple) - 1]

    ext = property(__get_ext)

    def save(self, name=None, save_dir="uploads", prefix="original", separator="-"):
        if name is None:
            file_parts = [prefix, get_random()]
            name = separator.join(file_parts) + self.ext

        self.save_path = os.path.abspath(os.path.join(save_dir, name))

        self.__file.save(self.save_path)

        self.saved = True
