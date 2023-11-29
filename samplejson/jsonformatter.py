"""
    JSON File Formatter
"""
import json


with open("sample.json", "r") as read_file:
    data = json.load(read_file)


with open("sample.json", "w") as write_file:
    json.dump(data, write_file, indent=4)