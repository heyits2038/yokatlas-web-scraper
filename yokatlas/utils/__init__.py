"""
Author: @heyits2038
GitHub: https://github.com/heyits2038
"""

from .json import read_json_file, save_json_file
from .net import fetch_html, get_html_content
from .text import transform_key_to_english

__all__ = [
    "save_json_file",
    "read_json_file",
    "fetch_html",
    "get_html_content",
    "transform_key_to_english",
]
