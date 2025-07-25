"""
Author: @heyits2038
GitHub: https://github.com/heyits2038
"""

from typing import Optional

from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait


def _get_html_content(url: str, *, timeout: int = 10) -> Optional[BeautifulSoup]:
    """
    Get the HTML content of a given URL.
    """
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    driver = webdriver.Chrome(options=chrome_options)
    try:
        driver.get(url)
        WebDriverWait(driver, timeout).until(
            lambda d: d.execute_script("return document.readyState") == "complete"
        )
        return BeautifulSoup(driver.page_source, "html.parser")
    finally:
        driver.quit()


def fetch_html(url: str) -> BeautifulSoup:
    """
    Fetch the HTML content of a given URL.
    """
    soup = _get_html_content(url)

    if soup is None:
        raise RuntimeError(f"Failed to fetch {url}")

    return soup


# Backward compatibility.
get_html_content = _get_html_content
