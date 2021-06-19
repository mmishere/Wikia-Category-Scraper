from requests import get
from bs4 import BeautifulSoup
import os
import re # regex

# BASE_URL = input("Paste base URL: ")
# URL = input("Paste categories URL: ")

BASE_URL = "https://octopathtraveler.fandom.com"
URL = "https://octopathtraveler.fandom.com/wiki/Special:Categories?offset=&limit=500"
# URL = "https://octopathtraveler.fandom.com/wiki/Special:Categories"

# https://octopathtraveler.fandom.com/wiki/Special:Categories?offset=&limit=500
# have to use offset lmao
# users have to put in pages on their own i guess

def get_categories(box):
    box_str = str(box)

    to_return = []

    link_pattern = "href=\"\/wiki\/Category:.+?(?=\")"
    # example output: a href="/wiki/Category:Advanced_Job_Shrines
    title_pattern = "title=\"Category:.+?(?=\")"
    # example output: title="Category:Advanced Job Shrines


    links_unfinished = re.findall(link_pattern, box_str)
    titles_unfinished = re.findall(title_pattern, box_str)

    
    for i in range(0, len(links_unfinished)):
        link = BASE_URL + links_unfinished[i][8:]
        title = titles_unfinished[i][16:]

        l_t_tup = (link, title)
        to_return.append(l_t_tup)

        print(to_return[i])

    # for url in box_str.find_all('a', href=True):
    #     if (url['href'].startswith("/wiki/Category:")):
    #         to_return.append(get_url_tuple(url))
    
    return to_return

def get_url_tuple(url):
    category_name = url['href'][15:]
    new_url = BASE_URL + url['href']
    return (category_name, new_url)

if __name__ == "__main__":
    page_html = get(URL).text
    page = BeautifulSoup(page_html, features="html.parser")

    
    desired_box = page.find_all('div', class_="mw-spcontent")
    # print(desired_box)

    categories = get_categories(desired_box)
    print()
    print(len(categories))

    # for c in categories:
    #     # os.makedirs(c[0], exist_ok=True)
    #     print(c)


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