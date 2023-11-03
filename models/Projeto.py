import json

class Projeto:
    url: str
    name: str
  
    def __init__(self, name, url):
      self.url = url
      self.name = name
      
    def __str__(self):
      return 'Nome: ' + self.name + '\nurl: ' + self.url