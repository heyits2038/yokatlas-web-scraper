"""
    Author: @heyits2038
    GitHub: https://github.com/heyits2038
"""
from typing import Union
from bs4 import BeautifulSoup


def parse_university_list(soup: BeautifulSoup):
    """
    Parse the university list from the BeautifulSoup object.
    """
    universities = []
    seen_ids = set()

    for opt in soup.select("#univ2 option"):
        name = opt.text.strip()
        if name == "Seç...":
            continue

        uid = opt.get("value")
        if not uid or uid in seen_ids:
            continue

        seen_ids.add(uid)
        universities.append({
            "university_id": uid,
            "university_name": name
        })

    return universities


def parse_programs_by_university_id(soup: BeautifulSoup):
    """
    Parse the programs for a university from the BeautifulSoup object.
    """
    programs = []

    for panel in soup.select(".container .panel.panel-primary"):
        anchor = panel.select_one(".panel-heading a")
        if not anchor:
            continue

        href_val: Union[str, list[str], None] = anchor.get("href")
        if not href_val:
            continue

        if isinstance(href_val, list):
            if not href_val:
                continue

            href = href_val[0]
        else:
            href = href_val

        _, _sep, _id_part = href.partition("=")
        if not _sep:
            continue

        program_id = _id_part.strip()
        program_name = anchor.text.strip()

        if not program_id or not program_name:
            continue

        programs.append({
            "program_id": program_id,
            "program_name": program_name
        })

    return programs
