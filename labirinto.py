from utils import floor
from turtle import *
import numpy as np

class Labirinto:

 def obter_visinhos(lin, col):
   pass

 def __init__(self, dim, tam_celula, cor_celula, cor_pastilhas, x, y):
  self._dim = dim
  self._cor_celula = cor_celula
  self._cor_pastilhas = cor_pastilhas
  self._tam_celula = tam_celula
  self._x = x
  self._y = y
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

 def ler_matriz_aleatoria(self):
  return np.random.randint(2,size=(self._dim,self._dim))

 def criar_labirinto(self, p1=500, p2=500, p3=370, p4=0):
  tracer(False)
  hideturtle()
  bgcolor('black')
  setup(p1,p2,p3,p4)
  for lin in range(self._dim):
   for col in range(self._dim):
    if (matriz[lin][col] == 1):
     x,y = em_coord_turtle()
     desenhar_celula()
     desenhar_pastilha()

 def desenhar_celula(self):
  color(self._cor_celula)
  up()
  goto(x,y)
  down()
  begin_fill()
  for _ in range(4):
    forward(self._tam_celula)
    left(90)
  end_fill()
  up()

 def chao_da_celula(self):
  chao_x = int(floor(self._x, self._tam_celula))
  chao_y = int(floor(self._y, self._tam_celula))
  return chao_x, chao_y

 def em_coord_turtle(self):
  meio = self._dim // 2
  x = (col - meio) * self._tam_celula
  y = (meio - lin) * self._tam_celula
  return x, y

 def em_coord_matriz(self):
  chao_da_celula()
  meio = self._dim // 2
  self._lin = int(meio - (chao_y / tam_celula))
  self._col = int(meio + (chao_x / tam_celula))
  return self._lin, self._col

 def cel_aleatoria(self):
  i, j = np.random.randint(self._dim, size=(2))
  while(not eh_caminho()):
   i, j = np.random.randint(self._dim, size=(2))
  return i, j

 def eh_caminho():
     return matriz [i][j] == 1

 def desenhar_pastilha(self):
  c = self._tam_celula // 2
  up()
  goto(x + c, y + c)
  down()
  dot(3, self._cor_pastilhas)
