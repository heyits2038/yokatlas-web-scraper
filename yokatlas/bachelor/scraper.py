"""
    Author: @heyits2038
    GitHub: https://github.com/heyits2038
"""
from yokatlas.utils import get_html_content
from yokatlas.bachelor.parser import (
    parse_university_list,
    parse_programs_by_university_id,
    parse_program_general_info_by_id
)


def fetch_university_list():
    """
    Fetch and return the list of universities.
    """
    soup = get_html_content(
        "https://yokatlas.yok.gov.tr/lisans-univ.php")

    if soup is None:
        raise RuntimeError("Failed to fetch the list of universities.")

    return parse_university_list(soup)


def fetch_programs_by_university_id(university_id: str):
    """
    Fetch and return the list of programs for the given university ID.
    """
    if not university_id or not university_id.strip():
        raise ValueError("university_id must be a non-empty string.")

    soup = get_html_content(
        f"https://yokatlas.yok.gov.tr/lisans-univ.php?u={university_id}"
    )

    if soup is None:
        raise RuntimeError("Failed to fetch programs for the university.")

    return parse_programs_by_university_id(soup)


def fetch_program_general_info_by_id(program_id: str):
    """
    Fetch and return the general information of a program by its ID.
    """
    if not program_id or not program_id.strip():
        raise ValueError("program_id must be a non-empty string.")

    soup = get_html_content(
        f"https://yokatlas.yok.gov.tr/content/lisans-dynamic/1000_1.php?y={program_id}")

    if soup is None:
        raise RuntimeError("Failed to fetch program information.")

    return parse_program_general_info_by_id(soup)
