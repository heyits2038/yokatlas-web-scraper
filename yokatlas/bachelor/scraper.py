"""
    Author: @heyits2038
    GitHub: https://github.com/heyits2038
"""
from yokatlas.utils import get_html_content


def get_university_list():
    """
    Returns a list of universities for bachelor's degree programs.
    """
    content = get_html_content("https://yokatlas.yok.gov.tr/lisans-univ.php")

    if content is None:
        raise ValueError("Failed to retrieve the soup object.")

    university_list = []

    for option_element in content.select("#univ2 option"):
        if option_element.text == "Seç...":
            continue

        university_name = option_element.text
        university_id = str(option_element.get("value", ""))

        university_list.append({
            "university_name": university_name,
            "university_id": university_id
        })

    return university_list
