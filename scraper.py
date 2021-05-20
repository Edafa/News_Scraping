import requests
from bs4 import BeautifulSoup
from tinydb import TinyDB, Query
from ArticleModel import ArticleModel

db = TinyDB('db.json')

def start():
    res = requests.get("https://www.spiegel.de/international/")
    content = BeautifulSoup(res.text, 'html.parser')

    articles = content.find_all("article")

    for article in articles:
        articleModel = ArticleModel(article)
        ArticleQuery = Query()
        results = db.search((ArticleQuery.title == articleModel.title) & (ArticleQuery.sub_title == articleModel.sub_title))

        if len(results) == 0:
            db.insert(articleModel.to_dict())
        else:
            articleModel.update(results[0])
            db.update(articleModel.to_dict(), (ArticleQuery.title == articleModel.title) & (ArticleQuery.sub_title == articleModel.sub_title))