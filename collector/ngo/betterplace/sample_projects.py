import json

from requests_html import HTMLSession



"""
Formating Queries and filtering based on API facet and order  

## example query
https://www.betterplace.org/de/api_v4/projects?per_page=27&category_id=2&facets=state:activated|min_activity_threshold_reached:true|hidden_from_platform:false&order=category_boost:desc|score:desc|completed:asc|rank:desc|last_donation_at:desc
https://api.betterplace.org/de/api_v4/projects.json?around=10997+Berlin%2C+Germany&around_distance=25km&facets=completed%3Afalse&nelat=51.123&nelng=12.123&order=rank%3ADESC&q=Skateistan&scope=location&swlat=51.001&swlng=12.001

## example facet using api docs 
facet = "tax_deductible:true|completed:false|closed:false|prohibit_donations:false|state:activated|min_activity_threshold_reached:true|hidden_from_platform:false"

## example order using betterplace api docs
order = "category_boost:desc|score:DESC|rank:DESC|progress_percentage:ASC|tax_deductible:DESC|completed:ASC|created_at:DESC|updated_at:DESC|last_donation_at:DESC|id:ASC"

## query based on category - simple and ideally retreives all docs in this category
https://www.betterplace.org/de/api_v4/projects?category_id=2
"""

session = HTMLSession()

## TODO move to config
path = "/home/avare/repos/charity-filter-evaluation/data/"
outfile = "betterplace_sample_projects_de.json"
max_category_id = 46
base = "https://www.betterplace.org/de/api_v4/projects?per_page=5&category_id="


# dict
PROJ =  {}
category = {}
category_totals = {}


def count_projects_on_page(page):
    count = len(page['data'])
    return count



def projects():

    # max category id
    #for category in range (min_category_id,max_category_id):
    for category in range(1, max_category_id):

        url = base + str(category)
        text = getpage(url)
        dat = json.loads(text)
        total_entries = dat["total_entries"]
        total_pages = dat["total_pages"]

        print(f"category: ", category)
        print(f"total_entries: ",total_entries)
        print(f"total_pages: ", total_pages)

        # total_pages : project for the given category
        for page in [1]:

            url = base + str(category) + '&page=' + str(page)
            text = getpage(url)
            dat = json.loads(text)
            nr_proj = count_projects_on_page(dat)

            # assign categories to every project
            for p in range(0,nr_proj):
                proj = dat['data'][p]
                id = proj['id']

                # a project can be associated with multiple categories
                if id in PROJ:
                    #print(f"project with multiple categories ", id)
                    PROJ[id]['categories'].append(category)
                    #print(PROJ[id]['categories'])
                else:
                    proj['categories'] = []
                    proj['categories'].append(category)
                    PROJ[id] = proj
                    #print(PROJ[id]['categories'])
    writefile(path + outfile,PROJ)

def getpage(url):
    r = session.get(url)
    return r.text


def writefile(filename, data):
    with open(filename, 'w') as f:
        json.dump(data, f)


if __name__ == "__main__":
    projects()