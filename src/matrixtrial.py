from numpy import *
class Matrix(object):
  M = 0
  N = 0
  data = array([[],[]], dtype=float)

  def __init__(M,N):
#      for i in range (0, M):
#          for j in range (0, N):
#              self.data[i][j] = 0.000000
#      self.M = M
#      self.N = N

  def random(M,N):
      
      for i in range (0, M):
          for j in range (0, N):
              self.data[i][j] = random.random()
      self.M = M
      self.N = N

  def show():
      for i in range (0, self.M):
          for j in range (0, self.N):
              print(self.data[i][j])

foo = Matrix.__init__(5,5)
foo.show()

