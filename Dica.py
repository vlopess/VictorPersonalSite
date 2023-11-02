class Dica:
    url: str
    texto: str
    image_url: str
    tipo: str
  
    def __init__(self, url, texto, image_url, tipo):
      self.url = url
      self.texto = texto
      self.image_url = image_url
      self.tipo = tipo      