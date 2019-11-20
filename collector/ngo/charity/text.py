import requests
from lxml import html
import string
import time
import glob
import re
import pandas as pd

from sklearn.feature_extraction.text import CountVectorizer

files = glob.glob(
    '/Users/stewarta/repos/charity-filter-evaluation/evaluation/data/raw/charity/organization_home/*.html')
# files = ['/Users/stewarta/repos/charity-filter-evaluation/evaluation/data/raw/charity/organization_home/3204.html']
corpus = []
vectorizer = CountVectorizer()
analyze = vectorizer.build_analyzer()


def extractid(url):
    r = '(\d+).html'
    m = re.search(r, url)
    id = m.group(1)
    return id


def createtagline(tree):
    # construct xpath
    text = tree.xpath('//*[@id="maincontent2"]/div[1]/h2/text()')
    if (len(text) > 0):
        text = str(text[0])
        text = text.strip()
        return text
    else:
        return ""


def createmission(tree):
    # construct xpath
    text = tree.xpath('//*[@id="overall"]/div[3]/div[3]/div/div/p/text()')

    if (len(text) > 0):
        text = str(text[0])
        text = text.strip()
        return text
    else:
        return ""


def extractcharityname(tree):
    # construct xpath
    text = tree.xpath('//*[@id="maincontent2"]/div[1]/h1/text()')

    if (len(text) == 0):
        return ""

    text = str(text[0])
    text = text.strip()
    return text


def categorycause(tree):
    r = '(.*):(.*)'
    # construct xpath
    text = tree.xpath('//*[@id="maincontent2"]/p/text()')

    if (len(text) == 0):
        return "", ""

    text = str(text[0])
    text = text.strip()

    # split dot
    m = re.search(r, text)
    acategory = m.group(1).strip()
    acause = m.group(2).strip()

    # strip both and return
    return acategory, acause


def convert(list):
    # Converting integer list to string list
    s = [str(i) for i in list]
    # Join list items using join()
    res = " ".join(s)
    return (res)


for f in files:
    extract_text = open(f, 'r', encoding='utf-8')

    # lxml to create tree
    tree = html.fromstring(extract_text.read())
    tagline = createtagline(tree)
    mission = createmission(tree)
    charityname = extractcharityname(tree)
    category, cause = categorycause(tree)
    charityid = extractid(f)

    # print()

    dict = {}
    dict['charityid'] = charityid
    dict['category'] = convert(analyze(category))
    dict['cause'] = convert(analyze(cause))
    dict['tagline'] = convert(analyze(tagline))
    dict['mission'] = convert(analyze(mission))

    corpus.append(dict)

df = pd.DataFrame(corpus)
df.to_csv('/Users/stewarta/repos/charity-filter-evaluation/evaluation/data/charity_navigator.csv')
