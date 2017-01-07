# coding=utf-8
import os


def get_random():
    return os.urandom(16).hex()
