import requests
from lxml import html
import string
import time

sleeptime = 1

azlisting =[]

azlisting.extend(list(string.ascii_uppercase))
azlisting.extend(['1','2','3','4','5','6','7','8','9'])

print(azlisting)

path_urls =  './data/parsed/'
path_pages = './data/parsed/pages/'
urlbase = 'https://www.charitynavigator.org/index.cfm'

links = open(path_urls + "urls_organization.txt", 'w', encoding='utf-8')


for num in azlisting:
    num = str(num)
    # construct url
    pagenumber = num + '#ltr-' + num

    print(pagenumber)

    # request page
    page = requests.get(urlbase, params={'bay': 'search.alpha', 'ltr': pagenumber})
    time.sleep(sleeptime)

    # # store entire page
    # with open(path_pages + num +'_alphabetic_organization_list.html', 'w', encoding='utf-8') as fp:
    #     fp.write(page.text)
    #     fp.close()

    # lxml to create tree
    tree = html.fromstring(page.content)

    # construct xpath
    organizations = tree.xpath('//*[@id="maincontent2"]/div/a/@href')

    print(len(organizations))
    # extract value, store in file
    for i in organizations:
        links.write(i)
        links.write('\n')


links.close()