from wikia_scraper import *

# create_files() and get_file_text() were tested manually, not with unit testing like this.

def test_get_box():
    page_html = get(URL).text
    page = BeautifulSoup(page_html, features="html.parser")

    desired_box = page.find_all('div', class_="mw-spcontent")
    assert len(desired_box) == 1, "Only 1 box"


def test_get_categories_full():
    test_base_url = "https://octopathtraveler.fandom.com/"
    test_url = "https://octopathtraveler.fandom.com/wiki/Special:Categories?offset=&limit=500"
    page_html = get(test_url).text
    page = BeautifulSoup(page_html, features="html.parser")

    desired_box = page.find_all('div', class_="mw-spcontent")
    categories = get_categories(desired_box)
    assert len(categories) == 264, "264 categories on full page"


def test_get_categories_partial():
    test_base_url = "https://octopathtraveler.fandom.com/"
    test_url = "https://octopathtraveler.fandom.com/wiki/Special:Categories"
    page_html = get(test_url).text
    page = BeautifulSoup(page_html, features="html.parser")

    desired_box = page.find_all('div', class_="mw-spcontent")
    categories = get_categories(desired_box)
    assert len(categories) == 50, "50 categories on 50-page"

