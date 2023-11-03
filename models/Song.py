import json

class Song:
    url: str
    name: str
    artista: str
    image: str
    nowplaying: bool
  
    def __init__(self, url, name, artista, image, nowplaying):
      self.url = url
      self.name = name
      self.artista = artista
      self.image = image
      self.nowplaying = nowplaying
      
    @staticmethod
    def from_dict(obj) -> 'Song':
        url = str(obj['recenttracks']['track'][0]['url'])
        name = str(obj['recenttracks']['track'][0]['name'])
        artista = str(obj['recenttracks']['track'][0]["artist"]["#text"])
        image = str(obj['recenttracks']['track'][0]["image"][2]["#text"])
        nowplaying = bool('@attr' in obj['recenttracks']['track'][0])
      
        return Song(url, name, artista, image, nowplaying)
      
    def __str__(self):
      return self.url + '\n' + self.name + '\n' + self.artista + '\n' + self.image + '\n' + str(self.nowplaying)