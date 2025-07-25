"""
Author: @heyits2038
GitHub: https://github.com/heyits2038
"""

import re


def transform_key_to_english(key: str):
    """
    Transforms a Turkish key to its English key equivalent.
    """
    turkish_chars = "şŞıİçÇöÖüÜğĞ"
    english_chars = "sSiIcCoOuUgG"
    table = str.maketrans(turkish_chars, english_chars)
    key = key.translate(table).lower()

    return re.sub(r"\W+", "", key)
