from utils import floor
from turtle import *
import numpy as np

class Labirinto:

 def obter_visinhos(lin, col):
   pass

 def __init__(self, dim, tam_celula):
  self._dim = dim
  self._tam_celula = tam_celula
  self._matriz = np.random.randint(2, size=(dim,dim))

 def ler_matriz_fixa(self):
  return [[0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0],\
            [0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0],\
            [0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0],\
            [0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0],\
            [0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0],\
            [0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0],\
            [0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0],\
            [0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0],\
            [0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0],\
            [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],\
            [0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0],\
            [0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0],\
            [0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0],\
            [0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0],\
            [0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0],\
            [0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0],\
            [0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0],\
            [0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0],\
            [0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0],\
            [0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0]]

 def ler_matriz_aleatoria(self, dim):
  return np.random.randint(2,size=(self._dim,self._dim))

 def criar_labirinto(self, p1=500, p2=500, p3=370, p4=0):
  tracer(False)
  hideturtle()
  bgcolor('black')
  setup(p1,p2,p3,p4)
  for lin in range(self._dim):
   for col in range(self._dim):
    if (self._matriz[lin][col] == 1):
     x,y = self.em_coord_turtle(lin,col)
     self.desenhar_celula(x, y, 'blue')
     self.desenhar_pastilha(x, y, 'white')

 def desenhar_celula(self, x, y, cor):
  color(cor)
  up()
  goto(x,y)
  down()
  begin_fill()
  for _ in range(4):
    forward(self._tam_celula)
    left(90)
  end_fill()
  up()

 def chao_da_celula(self, x, y):
  chao_x = int(floor(x, self._tam_celula))
  chao_y = int(floor(y, self._tam_celula))
  return chao_x, chao_y

 def em_coord_turtle(self, lin, col):
  meio = self._dim // 2
  x = (col - meio) * self._tam_celula
  y = (meio - lin) * self._tam_celula
  return x, y

 def em_coord_matriz(self, x, y):
  x, y = self.chao_da_celula(x,y)
  meio = self._dim // 2
  lin = int(meio - (y / tam_celula))
  col = int(meio + (x / tam_celula))
  return lin, col

 def cel_aleatoria(self, lin, col):
  i, j = np.random.randint(self._dim, size=(2))
  while(not self.eh_caminho(i, j)):
   i, j = np.random.randint(self._dim, size=(2))
  return i, j

 def eh_caminho(self):
     return self.matriz[lin][col] == 1

 def desenhar_pastilha(self, x, y, cor):
  c = self._tam_celula // 2
  up()
  goto(x + c, y + c)
  down()
  dot(3, cor)
