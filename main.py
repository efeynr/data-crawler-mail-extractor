import re
from requests_html import HTMLSession
from crawler import crawl, internal_urls
import sqlite3

crawl("https://www.bacchettagiuseppesrl.it/")


EMAIL_REGEX = r"""(?:[a-z0-9!#$%&'*+/=?^_`{|}~-]+(?:\.[a-z0-9!#$%&'*+/=?^_`{|}~-]+)*|"(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21\x23-\x5b\x5d-\x7f]|\\[\x01-\x09\x0b\x0c\x0e-\x7f])*")@(?:(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?\.)+[a-z0-9](?:[a-z0-9-]*[a-z0-9])?|\[(?:(?:(2(5[0-5]|[0-4][0-9])|1[0-9][0-9]|[1-9]?[0-9]))\.){3}(?:(2(5[0-5]|[0-4][0-9])|1[0-9][0-9]|[1-9]?[0-9])|[a-z0-9-]*[a-z0-9]:(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21-\x5a\x53-\x7f]|\\[\x01-\x09\x0b\x0c\x0e-\x7f])+)\])"""
EXTENSION_REGEX =r"\S+\.jpg"
EX_REGEX = r"\w+\.jpg"
jpgRegex = re.compile(EXTENSION_REGEX)
urls = internal_urls
links=[]
for link in urls:
    if re.search(EXTENSION_REGEX,link) is None:
        links.append(link)

for url in urls:
    session =HTMLSession()
    r=session.get(url)
    r.html.render()
    for re_match in re.finditer(EMAIL_REGEX, r.html.raw_html.decode()):
        print(re_match.group())



