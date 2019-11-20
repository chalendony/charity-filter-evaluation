Uses the BetterPlace API to  produce a json file containing metadata about social project


Name: BetterPlace.Org

Web (German): https://www.betterplace.org/de

Web (English): https://www.betterplace.org/en


Language: German, English

Schema:
Each entry is a (key, value) mapping from an integer id to a BetterPlace "data" object. The keys are a unique identifier for the project.
Example : {5, {id:5, name='Name of Project', description="description of the project" ....}}

Loading Catalog
 import json
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
         ....