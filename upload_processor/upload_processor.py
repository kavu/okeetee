# coding=utf-8
import os
import subprocess

from app_file import AppFile
from utils import get_random


class UploadProcessor:
    def __init__(self, file, save_dir="uploads", http_dir="uploads", prefix="processed", separator="-"):
        self.file = AppFile(file)
        self.save_dir = save_dir
        self.http_dir = http_dir
        self.prefix = prefix
        self.separator = separator
        self.secure_hash = get_random()

    def __output_filename(self):
        file_parts = [self.prefix, self.secure_hash]
        return self.separator.join(file_parts) + self.file.ext

    output_filename = property(__output_filename)

    def __output_path(self):
        return os.path.abspath(os.path.join(self.save_dir, self.output_filename))

    output_path = property(__output_path)

    def __input_path(self):
        return self.file.save_path

    input_path = property(__input_path)

    def __http_path(self):
        return "/" + self.http_dir + "/" + self.output_filename

    http_path = property(__http_path)

    def save(self):
        self.file.save()

    def process(self, input_path=None, log_to_file=False):
        if input_path is None:
            input_path = self.input_path

        if log_to_file:
            stdout = open(self.output_path + '.log', mode='a')
        else:
            stdout = subprocess.DEVNULL

        # Executing Two Commands
        subprocess.Popen(['cp', input_path, self.output_path], stdout=stdout, stderr=stdout)
        subprocess.Popen(['file', input_path], stdout=stdout, stderr=stdout)
        subprocess.Popen(['echo', "'Woot'"], stdout=stdout, stderr=stdout)

        return self.http_path
