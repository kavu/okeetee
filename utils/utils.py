# coding=utf-8
import os
import binascii


def get_random():
    return binascii.b2a_hex(os.urandom(8))
