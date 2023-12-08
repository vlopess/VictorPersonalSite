import requests
import json
from requests.exceptions import HTTPError
from myapp.models.Artigo import Artigo

def getDadosFromMedium():
  try:
    response = requests.get('https://api.rss2json.com/v1/api.json?rss_url=https://medium.com/feed/@Victorldev')
    artigo = Artigo.from_dict(response.json())
    return artigo
    
  except Exception as err:
      print(f'Other error occurred: {err}')
