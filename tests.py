from wikia_scraper import *

# create_files() and get_file_text() were tested manually, not with unit testing like this.


# this one had to be tested without pytest, with a line below it, aka `python3 tests.py`, but it did pass that check
def test_urls():
    # if formatted properly, returns properly
    # if formatted badly, returns properly
    # if empty, returns https:// b/c if the URL is invalid then it should catch that anyway at some point
    URL_good = get_categories_url("https://octopathtraveler.fandom.com/wiki/Special:Categories")
    assert URL_good == "https://octopathtraveler.fandom.com/wiki/Special:Categories", "URL good"
    
    URL_good_long = get_categories_url("https://octopathtraveler.fandom.com/wiki/Special:Categories?offset=&limit=500")
    assert URL_good_long == "https://octopathtraveler.fandom.com/wiki/Special:Categories?offset=&limit=500", "URL good long"
    
    URL_fix = get_categories_url("octopathtraveler.fandom.com/wiki/Special:Categories")
    assert URL_fix == "https://octopathtraveler.fandom.com/wiki/Special:Categories", "URL Fix"

    URL_fix_long = get_categories_url("octopathtraveler.fandom.com/wiki/Special:Categories?offset=&limit=500")
    assert URL_fix_long == "https://octopathtraveler.fandom.com/wiki/Special:Categories?offset=&limit=500", "URL Fix long"
    
    URL_invalid = get_categories_url("swoejf98234fj98j4.com/whaskdjflkj")
    assert URL_invalid == "https://swoejf98234fj98j4.com/whaskdjflkj", "URL invalid"

    URL_empty = get_categories_url("")
    assert URL_empty == "https://", "URL empty"

    # test base url with inputs
    BASE_URL_good = get_base_url(URL_good)
    assert BASE_URL_good == "https://octopathtraveler.fandom.com", "Base URL good"

    BASE_URL_good_long = get_base_url(URL_good_long)
    assert BASE_URL_good == "https://octopathtraveler.fandom.com", "Base URL good long"

    BASE_URL_invalid = get_base_url(URL_invalid)
    assert BASE_URL_invalid == "https://swoejf98234fj98j4.com/whaskdjflkj", "Base URL invalid doesn't change"
    
    BASE_URL_empty = get_base_url(URL_empty)
    assert BASE_URL_empty == "https://", "Base URL empty doesn't change"
# test_urls()


def test_get_box():
    page_html = get(URL).text
    page = BeautifulSoup(page_html, features="html.parser")

    desired_box = page.find_all('div', class_="mw-spcontent")
    assert len(desired_box) == 1, "Only 1 box"


def test_get_categories_full():
    BASE_URL = "https://octopathtraveler.fandom.com/"
    URL = "https://octopathtraveler.fandom.com/wiki/Special:Categories?offset=&limit=500"
    page_html = get(URL).text
    page = BeautifulSoup(page_html, features="html.parser")

    desired_box = page.find_all('div', class_="mw-spcontent")
    categories = get_categories(desired_box)
    assert len(categories) == 264, "264 categories on full page"


def test_get_categories_partial():
    BASE_URL = "https://octopathtraveler.fandom.com/"
    URL = "https://octopathtraveler.fandom.com/wiki/Special:Categories"
    page_html = get(URL).text
    page = BeautifulSoup(page_html, features="html.parser")

    desired_box = page.find_all('div', class_="mw-spcontent")
    categories = get_categories(desired_box)
    assert len(categories) == 50, "50 categories on 50-page"

