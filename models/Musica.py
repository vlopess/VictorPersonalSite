import json

class Musica:
    url: str
    name: str
    artista: str
  
    def __init__(self, url, name, artista):
      self.url = url
      self.name = name
      self.artista = artista
      
    @staticmethod
    def from_dict(obj) -> 'Musica':
        _url = str(obj['toptracks']['track'][0]['url'])
        _name = str(obj['toptracks']['track'][0]['name'])
        _artista = str(obj['toptracks']['track'][0]['artist']['name'])
        return Musica(_url, _name, _artista)
      
    def __str__(self):
      return 'Nome: ' + self.name + '\nurl: ' + self.url