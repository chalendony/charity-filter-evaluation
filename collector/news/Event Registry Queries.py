
from eventregistry import *

apikey = 'eda663f8-e934-42a5-88e2-bd75014130d1'

conceptUri = ['https://en.wikipedia.org/wiki/Poverty','https://en.wikipedia.org/wiki/Hunger',
              'https://en.wikipedia.org/wiki/Health' ,'https://en.wikipedia.org/wiki/Education',
              'https://en.wikipedia.org/wiki/Gender_equality', 'https://en.wikipedia.org/wiki/Sustainable_Development_Goals'
         'water', 'sanitation','energy','economic', 'society',
         'climate','inequality','cities'
        ]
 
#target_lst = ['museum', 'united ways', 'development and relief services',
#              'education', 'children',  'family']

#goals = ['sustainable development']
target_lst = ['museum']

#target_lst.extend(goals)
max_items = 1

er = EventRegistry(apiKey = apikey)



for kw in target_lst:
    q = QueryArticlesIter(
        keywords = QueryItems.AND('children'), # mentions
        conceptUri = QueryItems.OR('https://en.wikipedia.org/wiki/Sustainable_Development_Goals'),
        categoryUri = QueryItems.OR(['dmoz/Health','dmoz/Society/Issues/Warfare_and_Conflict']), 
        dataType = ["news", "blog"],
        ignoreLocationUri = er.getLocationUri('North America'),
        ignoreKeywords = 'Trump',
        lang = 'eng',
        dateStart='2013-01-01',
        isDuplicateFilter='skipDuplicates',
        hasDuplicateFilter='skipHasDuplicates',
        sourceLocationUri = er.getLocationUri("Germany"))
    
    # obtain articles that have were shared the most on social media (Facebook, G+, LinkedIn, ...)
    for art in q.execQuery(er, sortBy = "rel", maxItems =max_items):
        print(art)


# In[ ]:


er_sourceuri = EventRegistry.getNewsSourceUri()
er_concept_uri = EventRegistry.getConceptUri()


# In[20]:


from eventregistry import *
er = EventRegistry(apiKey = apikey)
q = QueryArticlesIter(
    # here we don't use keywords so we will also get articles that mention immigration using various synonyms
    conceptUri = er.getConceptUri("immigration"),
    categoryUri = er.getCategoryUri("business"),
    sourceLocationUri = er.getLocationUri("New York City"))
# obtain 500 articles that have were shared the most on social media (Facebook, G+, LinkedIn, ...)
for art in q.execQuery(er, sortBy = "socialScore", maxItems = 500):
    print(art)


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