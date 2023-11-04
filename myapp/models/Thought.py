class Thought:
    texto: str
    time: str
  
    def __init__(self,texto, time):
      self.texto = texto
      self.time = time

    def __str__(self) -> str:
       return f'[{self.texto}, {self.texto}]'