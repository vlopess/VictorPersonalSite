import requests
import json
from VictorPersonalSite.models.Artist import Artist
from VictorPersonalSite.models.Song import Song
from VictorPersonalSite.models.Musica import Musica

class LastFmController:
  
  def getDadosFromLastfm(period = 'overall'):
    try:
      payload = {
        'api_key': '4a9f5581a9cdf20a699f540ac52a95c9',
        'method': 'user.gettopartists',
        'format': 'json',
        'user' : 'Netuno8',
        'limit' : '1',
        'period' : period,
        
      }
      response = requests.get('http://ws.audioscrobbler.com/2.0/', params=payload)
      artista = Artist.from_dict(response.json())
      return artista
      
    except Exception as err:
        print(f'Other error occurred: {err}')

  def getrecenttrack():
    try:
      payload = {
        'api_key': '4a9f5581a9cdf20a699f540ac52a95c9',
        'method': 'user.getrecenttracks',
        'format': 'json',
        'user' : 'Netuno8',
        'limit' : '1',
        
      }
      response = requests.get('http://ws.audioscrobbler.com/2.0/', params=payload)
      song = Song.from_dict(response.json())
      return song
      
    except Exception as err:
        print(f'Other error occurred: {err}')


  def gettoptracks():
    try:
      payload = {
        'api_key': '4a9f5581a9cdf20a699f540ac52a95c9',
        'method': 'user.gettoptracks',
        'format': 'json',
        'user' : 'Netuno8',
        'limit' : '1',
        'period': '7day'      
      }
      response = requests.get('http://ws.audioscrobbler.com/2.0/', params=payload)
      musica = Musica.from_dict(response.json()) 
      return musica
      
    except Exception as err:
        print(f'Other error occurred: {err}')

  def getInfo():
    try:
      payload = {
        'api_key': '4a9f5581a9cdf20a699f540ac52a95c9',
        'method': 'user.getInfo',
        'format': 'json',
        'user' : 'Netuno8',  
      }
      response = requests.get('http://ws.audioscrobbler.com/2.0/', params=payload)
      obj = response.json()
      return obj['user']['playcount'] 
      
    except Exception as err:
        print(f'Other error occurred: {err}')

