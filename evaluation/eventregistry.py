#http://eventregistry.org/documentation


from eventregistry import *

apikey = 'eda663f8-e934-42a5-88e2-bd75014130d1'


target_lst = ['museums', 'united ways', 'development and relief services',
              'advocacy and education', 'children and family services']

er = EventRegistry(apiKey = apikey)
q = QueryArticlesIter(
    keywords = QueryItems.OR(["George Clooney", "Sandra Bullock"]),
    dataType = ["news", "blog"])
# obtain at most 500 newest articles or blog posts
for art in q.execQuery(er, sortBy = "date", maxItems = 500):
    print(art)