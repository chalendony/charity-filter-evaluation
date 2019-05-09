


import requests
from lxml import html
import string
import time
import glob
import re

files = glob.glob('../*/*/*/organization_home/*.html')
#files = ['/Users/stewarta/repos/charity-filter-evaluation/evaluation/data/raw/charity/organization_home/3204.html']

def extractid(url):
    r = '(\d+).html'
    m = re.search(r,url)
    id = m.group(1)
    return id

def createtagline(tree):
    # construct xpath
    text = tree.xpath('//*[@id="maincontent2"]/div[1]/h2/text()')
    text = str(text[0])
    text = text.strip()
    return text

def createmission(tree):
    # construct xpath
    text = tree.xpath('//*[@id="overall"]/div[3]/div[3]/div/div/p/text()')
    text = str(text[0])
    text = text.strip()
    return text


def charityname(tree):
    # construct xpath
    text = tree.xpath('//*[@id="maincontent2"]/div[1]/h1/text()')
    text = str(text[0])
    text = text.strip()
    return text


def categorycause(tree):

    r = '(.*):(.*)'
    # construct xpath
    text = tree.xpath('//*[@id="maincontent2"]/p/text()')
    text = str(text[0])
    text = text.strip()
    # split dot
    m = re.search(r, text)
    category = m.group(1).strip()
    cause = m.group(2).strip()
    # strip both and return
    return category, cause

for f in files:

    text = open(f, 'r', encoding='utf-8')
    # lxml to create tree
    tree = html.fromstring(text.read())
    tagline = createtagline(tree)
    mission = createmission(tree)
    charityname = charityname(tree)
    category, cause = categorycause(tree)
    charityid = extractid(f)

    print(charityid)
    #print(category)
    #print(cause)


