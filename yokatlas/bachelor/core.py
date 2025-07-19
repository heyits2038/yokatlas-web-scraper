"""
    Author: @heyits2038
    GitHub: https://github.com/heyits2038
"""
from yokatlas.bachelor import scraper


def get_university_list():
    """
    Get the list of universities.
    """
    return scraper.fetch_university_list()


def get_programs_by_university_id(university_id: str):
    """
    Get the list of programs for a given university ID.
    """
    return scraper.fetch_programs_by_university_id(university_id)
