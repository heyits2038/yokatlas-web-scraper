"""
    Author: @heyits2038
    GitHub: https://github.com/heyits2038
"""
from yokatlas.utils import get_html_content


def get_university_list():
    """
    Fetch and return the list of universities.
    """
    soup = get_html_content(
        "https://yokatlas.yok.gov.tr/lisans-univ.php")

    if soup is None:
        raise RuntimeError("Failed to fetch the list of universities.")

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
