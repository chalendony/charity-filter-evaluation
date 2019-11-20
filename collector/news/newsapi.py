# https://newsapi.org/docs/client-libraries/python

from newsapi.newsapi_client import NewsApiClient

apikey = 'eda663f8-e934-42a5-88e2-bd75014130d1'

newsapi = NewsApiClient(api_key=apikey)

target_lst = ['museums', 'united ways', 'development and relief services',
              'advocacy and education', 'children and family services']

lst = []
for topic in target_lst():
    res = all_articles = newsapi.get_everything(q=topic,
                                          language='en',
                                          sort_by='relevancy',
                                          page=2)
    lst.extend(res)


print(lst)