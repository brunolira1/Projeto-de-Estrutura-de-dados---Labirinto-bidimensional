from turtle import *

class Agente:

 def __init__(self, tam_celula, tam_agente):
    self._tam_celula = tam_celula
    self._tam_agente = tam_agente

 def desenhar_agente(self, x, y, cor):
     c = self._tam_celula // 2
     up()
     goto(x + c, y + c)
     down()
     dot(self._tam_agente, cor)
     
