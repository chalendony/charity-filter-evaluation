"""
Summary stats on the better place projects
"""

import json
import pandas as pd

from collections import namedtuple

## TODO move to config
path = "/home/avare/repos/charity_navigator-filter-evaluation/data/"
outfile = "betterplace_projects_de_bak.json"

Project = namedtuple(
    "Entry",
    [
        "id",
        "title",
        "description",
        "summary",
        "categories",
    ],
)

df = pd.DataFrame()

def text():
    lst = []
    with open(path + outfile, 'r') as myfile:
       content=myfile.read()
    dat = json.loads(content)
    for key in dat:
        proj = dat[key]
        id = proj['id']
        # tokenize text
        title = proj['title']
        description = proj['description']
        summary = proj['summary']
        cat = proj['categories']

        # convert cat

        # string html

        e = Project(id,  title, description, summary, cat)
        lst.append(e)




    #proj = Project(id='dat', name=30, description='male', summary=, categories=)


    #cat.append(e)




if __name__ == "__main__":
    text()