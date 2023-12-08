import json

class Artist:
    url: str
    name: str
  
    def __init__(self, url, name):
      self.url = url
      self.name = name
      
    @staticmethod
    def from_dict(obj) -> 'Artist':
        _url = str(obj['topartists']['artist'][0]['url'])
        _name = str(obj['topartists']['artist'][0]["name"])
        return Artist(_url, _name)
      
    def __str__(self):
      return 'Nome: ' + self.name + '\nurl: ' + self.url