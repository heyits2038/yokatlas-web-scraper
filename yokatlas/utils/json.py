"""
Author: @heyits2038
GitHub: https://github.com/heyits2038
"""

import json
import os


def save_json_file(data, filename):
    """
    Saves the given data to a JSON file.
    """
    try:
        directory = os.path.dirname(filename)

        if directory:
            os.makedirs(directory, exist_ok=True)
        with open(filename, "w", encoding="utf-8") as file:
            json.dump(data, file, ensure_ascii=False, indent=4)
    except Exception as e:
        raise RuntimeError(f"Error saving JSON file: {e}")


def read_json_file(filename):
    """
    Reads a JSON file.
    """
    try:
        if not os.path.exists(filename):
            raise FileNotFoundError(f"File not found: {filename}")
        with open(filename, "r", encoding="utf-8") as file:
            return json.load(file)
    except Exception as e:
        raise RuntimeError(f"Error reading JSON file: {e}")
