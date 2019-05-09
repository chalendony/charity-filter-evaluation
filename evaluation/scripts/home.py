import requests
import re
from lxml import html
import string
import time

sleeptime = 1


url_file =  '../data/urls_organization.txt'
raw_path  = '../data/raw/charity/organization_home/'
urlbase = 'https://www.charitynavigator.org/index.cfm'


def extractid(url):
    r = 'orgid=(\d+)'
    m = re.search(r,url)
    id = m.group(1)
    return id


links = open(url_file, 'r', encoding='utf-8')
for url in links:
    # https://www.charitynavigator.org/index.cfm?bay=search.summary&orgid=6082
    charity_id = str(extractid(url))
    page = requests.get(urlbase, params={'bay': 'search.summary', 'orgid': charity_id})

    time.sleep(sleeptime)

    filename = charity_id + '.html'
    print(filename)
    # store entire page

    with open(raw_path + charity_id + '.html', 'w', encoding='utf-8') as fp:
        fp.write(page.text)
        fp.close()



