
"""
Retreives articles that contain the mention of selected betterplace topics.
"""

from eventregistry import *

sourceUri = 'focus.de' # http://eventregistry.org/documentation?tab=suggSources


#apikey = 'eda663f8-e934-42a5-88e2-bd75014130d1'
apikey = 'fb953bd0-17fb-4c30-a93c-c48b6ed5f181'
keywords = ['climate', 'animal protection', 'childern']
max_items = 1

er = EventRegistry(apiKey=apikey)

# TODO loop through keywords
q = QueryArticlesIter(
    keywords=QueryItems.OR(['umweltschutz', 'klimaschutz', 'tierschutz', 'kinder', 'fluechtlingshilfe', 'frauen', 'gesundheit', 'katastrophenschutz',
                            'hunger', 'obdachlose', 'nothilfe', 'hungerhilfe', 'trinkwasser', 'menschenrechte', 'senioren']),
    conceptUri = QueryItems.OR('https://en.wikipedia.org/wiki/Sustainable_Development_Goals'),
    #dataType=["news"],
    lang='deu',
    isDuplicateFilter='skipDuplicates',
    sourceLocationUri=er.getLocationUri("Germany"),
    sourceUri=er.getNewsSourceUri('focus.de')
    )

for art in q.execQuery(er,  maxItems=max_items):
    print('Retrieving Articles...')
    print(type(art))
    # append keyword to dictionary

    # convert dictionary to json lines

    # store results to file
    print(art.keys())
