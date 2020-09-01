from turtle import *

class Agente:

 def __init__(self, x, y, cor, tam_celula, tam_agente):
    self._x = x
    self._y = y
    self._cor = cor
    self._tam_celula = tam_celula
    self._tam_agente = tam_agente

 def desenhar_agente(self):
     c = self._tam_celula // 2
     up()
     goto(x + c, y + c)
     down()
     dot(self._tam_agente, cor)
