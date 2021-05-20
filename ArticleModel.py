from datetime import datetime

class ArticleModel:
    def __init__(self, article):
        self.article = article
        self.sub_title, self.title = self.extract_titles()
        self.abstract = self.extract_abstract()
        self.download_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.update_time = None


    def update(self, existing):
        self.download_time = existing['download_time']
        self.update_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    def to_dict(self):
        return {
            'title': self.title,
            'sub_title': self.sub_title,
            'abstract': self.abstract,
            'download_time': self.download_time,
            'update_time': self.update_time
        }

    def extract_titles(self):
        list = [elm.text.strip() for elm in self.article.select("h2 span")]
        sub_title = list[0]
        title = ''
        for elm in list:
            if elm is not sub_title:
                title = elm
                break
        if title == '':
            return '', sub_title
        return sub_title, title

    def extract_abstract(self):
        sections = self.article.select("section")
        if len(sections) == 0:
            return ''
        return sections[0].text.strip()