from requests import get
from bs4 import BeautifulSoup
import os
import re

BASE_URL = input("Paste base URL: ")

if (BASE_URL[-1] == '/'):
    BASE_URL = BASE_URL.rstrip(BASE_URL[-1])

print(BASE_URL)

URL = input("Paste categories URL: ")

# example URLs:
# BASE_URL = "https://octopathtraveler.fandom.com"
# URL = "https://octopathtraveler.fandom.com/wiki/Special:Categories"

def get_file_text(file_tup):
    to_return = ""
    
    sub_page_html = get(file_tup[0]).text
    sub_page = BeautifulSoup(sub_page_html, features="html.parser")

    box = sub_page.find_all('div', class_="category-page__members")
    box_str = str(box)

    # this has to be done with one pattern only because otherwise titles will show up twice
    pattern = "a href=\"\/wiki\/.+?\" title=\".+?\""
    # example output: a href="/wiki/Capable_Culinarian" title="Capable Culinarian"

    links_and_titles_unfinished = re.findall(pattern, box_str)
    for text in links_and_titles_unfinished:
        text_list = text.split("\"")

        title = text_list[3]
        url = BASE_URL + text_list[1]

        to_add = f"{title}: {url}\n"
        to_return += to_add
    
    return to_return

# if the file exists already, it won't be affected
# else, it'll make the file and write to it as desired
def create_files(file_list):
    for file_tup in file_list:
        file_name = file_tup[1] + ".txt"

        # if the file doesn't exist, make it, otherwise open it
        file_open = open(file_name, 'a') # appends to the file if it exists, doesn't overwrite
        
        file_text = get_file_text(file_tup)
        file_open.write(file_text)

        file_open.close()


# given the correct box, retrieves category names and links
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
        link = BASE_URL + links_unfinished[i][6:]
        title = titles_unfinished[i][16:]

        l_t_tup = (link, title)
        to_return.append(l_t_tup)
    
    return to_return


# if __name__ == "__main__":
#     page_html = get(URL).text
#     page = BeautifulSoup(page_html, features="html.parser")
    
#     desired_box = page.find_all('div', class_="mw-spcontent")
#     categories = get_categories(desired_box)
#     create_files(categories)

