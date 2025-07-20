"""
    Author: @heyits2038
    GitHub: https://github.com/heyits2038
"""
import re
from typing import Optional

from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait


def get_html_content(url: str) -> Optional[BeautifulSoup]:
    """
    Fetches HTML content using Selenium and returns it as a BeautifulSoup object.
    """
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    driver = webdriver.Chrome(options=chrome_options)

    try:
        driver.get(url)
        WebDriverWait(driver, 10).until(lambda driver: driver.execute_script(
            "return document.readyState") == "complete")
        return BeautifulSoup(driver.page_source, "html.parser")
    finally:
        driver.quit()


def transform_key_to_english(key: str):
    """
    Transforms a Turkish key to its English key equivalent.
    """
    turkish_chars = "şŞıİçÇöÖüÜğĞ"
    english_chars = "sSiIcCoOuUgG"
    table = str.maketrans(turkish_chars, english_chars)
    key = key.translate(table).lower()

    return re.sub(r"\W+", "", key)
