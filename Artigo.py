import json

class Artigo:
    url: str
    title: str
    pubDate: str
    thumbnail: str
  
    def __init__(self, url, title, pubDate, thumbnail):
      self.url = url
      self.title = title
      self.pubDate = pubDate
      self.thumbnail = thumbnail
      
    @staticmethod
    def from_dict(obj) -> 'Artigo':
        url = str(obj['items'][0]['link'])
        title = str(obj['items'][0]["title"])
        pubDate = str(obj['items'][0]["pubDate"])
        thumbnail = str(obj['items'][0]["thumbnail"])
        return Artigo( url, title, pubDate, thumbnail)
      
    def __str__(self):
      return 'Title: ' + self.title + '\nUrl: ' + self.url + '\nData: ' + self.pubDate+'\nThumbnail: ' + self.thumbnail