# Projeto-de-Estrutura-de-dados---Labirinto-bidimensional
# integrantes: Bruno Lira, Victor Couto, Guilherme Moreira

from turtle import *
from random import choice

def ler_matriz():
    tam_matriz = 20
    matriz = [[choice([0, 1]) for i in range(tam_matriz)] for j in range(tam_matriz)]
    return matriz
    
def criar_labirinto(p1=420, p2=420, p3=370, p4=100):
    """ Cria uma tela do Turtle """
    
   bgcolor('black')
   setup(p1, p2, p3, p4)
    
   hideturtle()
   speed(0)
    
   matriz = ler_matriz()
   for matriz_linha_idx, matriz_linha in enumerate(matriz):
       for matriz_coluna_idx, matriz_coluna in enumerate(matriz_linha):
           if matriz_coluna == 1:
               xt, yt = em_coord_turtle(matriz_linha_idx + 1, matriz_coluna_idx + 1)
               desenhar_celula(xt, yt, 'blue')
               
def desenhar_celula(xt, yt, cor='blue'):
    """ Dada uma coordenada (xt, yt) do Turtle, desenha um quadrado (célula) na posição """
    
   tam_quadrado = 20
    
   penup()
   goto(xt - (tam_quadrado/2), yt + (tam_quadrado/2))
    
   fillcolor(cor)
   begin_fill()
    
   for i in range(4): 
       forward(tam_quadrado)
       right(90)
        
   pendown()
   end_fill()
   
def em_coord_turtle(xm, ym):
  """ Dada uma coordenada da matriz (i,j) transforma em coordenada Turtle """
   matriz = ler_matriz()
    
   screensize = (420, 420)
    
   xc = xm * ((screensize[0] - 20) / len(matriz[0])) - ((screensize[0] - 20) / 2)
   xy = (ym * ((screensize[1] - 20) / len(matriz)) - ((screensize[1] - 20) / 2)) * -1
    
   return xc, xy
   
 def main():
  criar_labirinto()
  done()
   
 main()
