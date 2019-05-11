http://eventregistry.org/documentation

apikey = 'eda663f8-e934-42a5-88e2-bd75014130d1'

from eventregistry import *
er = EventRegistry(apiKey = YOUR_API_KEY)
q = QueryArticlesIter(
    keywords = QueryItems.OR(["George Clooney", "Sandra Bullock"]),
    dataType = ["news", "blog"])
# obtain at most 500 newest articles or blog posts
for art in q.execQuery(er, sortBy = "date", maxItems = 500):
    print art