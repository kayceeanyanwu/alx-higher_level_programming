#!/usr/bin/python3
""" module that contains stuff """


from sys import argv
import json

saved = __import__('5-save_to_json_file').save_to_json_file
loaded = __import__('6-load_from_json_file').load_from_json_file


try:
    listo = loaded("add_item.json")
except:
    listo = []

listo.extend(argv[1:])
saved(listo, "add_item.json")
