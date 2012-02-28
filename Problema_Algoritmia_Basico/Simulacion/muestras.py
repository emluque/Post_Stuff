import subprocess
import random
import math
import utils

class Muestra:
  
  '''Clase para generar muestras de resultados aleatorios del algoritmo'''  

  def __init__(self, n, k, cant):
    self.n = n
    self.k = k
    self.cant = cant
    self.resultados = []

  def generar_lista(self):
    lista = []
    for i in range(self.n):
      lista.append(random.randint(1, self.k))
    return ",".join( [str(x) for x in lista])

  def generar_resultado(self, lista ):
    process = subprocess.Popen(["algoritmo/algo", lista] , shell=False, stdin=subprocess.PIPE, stdout=subprocess.PIPE)
    res = ""
    for char in process.stdout.read():
      res += char
    
    process.wait()
    #Esta linea que sigue es medio al dope
    if (process.returncode != None):
      if(process.returncode < 0):
        print("----")
        print(process.returncode)
        print("----")
        raise NameError("Tio, No andubo el proceso.") 
    else:   
      process.kill()

    return int(res)

  def generar_resultados(self):
    for i in range(self.cant):
      strr = self.generar_lista();
      a = self.generar_resultado( strr )
      self.resultados.append(a)

  def guardar_resultados(self, directory):
    fecha = utils.fecha_para_filename()
    filename =  str(self.n) + '-' + str(self.k) + '_' + fecha + ".csv" 
    with open(directory + filename, mode="w") as my_file:
      towrite = ",".join( [str(x) for x in self.resultados])
      my_file.write( towrite )
    return filename

  def leer_resultados(self, filename):
    with open(filename, mode="r") as my_file:
      res = my_file.readline()
    self.resultados = res.split(",")
          
  def limpiar_resultados(self):
    self.resultados = []

  def mostrar_resultados(self):
    print ",".join( [str(x) for x in self.resultados])

  def promedio(self):
    suma = 0
    for i in self.resultados:
      suma += i
    return float(suma) / self.cant

  def rango(self):
    return( min(self.resultados), max(self.resultados) )

  def desvio_estandard(self):
    suma = 0
    promedio = self.promedio()
    for i in self.resultados:
      suma += ( ( i - promedio ) ** 2 )
    res = math.sqrt( ( suma )/ (self.cant - 1) )
    return res  
  
  def rango_posible(self):
    return( self.n -1, (self.n*(self.n-1))/2 )

  def distribucion(self):
    dist = {}
    sort_res = self.resultados
    sort_res.sort()
    for x in sort_res:
      if x in dist:
        dist[x] += 1
      else:
        dist[x] = 1
    return dist

  def distribucion_a_lista_tuplas(self):
    d_dist = self.distribucion()
    l = []
    for x in d_dist:
      l.append( (x, d_dist[x] ) )
    l.sort()
    return l
   
  def poblacion(self):
    return self.k ** self.n

  def mediana(self):
    dist = self.distribucion_a_lista_tuplas()
    #medio trucho
    if(self.cant%2==1):
      posicion = self.cant/2
      suma = 0
      for x in range(0,len(dist)):
        suma += dist[x][1]
        if(suma >= posicion):
          return dist[x][0]
    else: 
      posicion = self.cant/2
      suma = 0
      for x in range(0,len(dist)):
        suma += dist[x][1]
        if(suma >= posicion):
          if(suma == posicion):
            return float(dist[x][0]+dist[x+1][0])/2  
          else: 
            return dist[x][0]

  def modo(self):
    d = self.distribucion_a_lista_tuplas()
    sd = sorted(d, key= lambda kk: kk[1], reverse=True)
    l = []
    a = 0
    t = sd[0][1]

    while( t == sd[0][1] and a < len(sd) ):
      l.append(sd[a][0])
      a += 1
      if a<len(sd): t = sd[a][1]
    return l


  '''

if  __name__  ==  '__main__':

  #Generar y Guardar
  muestra = Muestra(100,100,100000)
  muestra.generar_resultados()
  #muestra.guardar_resultados("resultados/muestras")
  muestra.mostrar_resultados()
  print( muestra.promedio() )
  print( muestra.rango() )
  print( muestra.desvio_estandard() )
  print( muestra.rango_posible() )
  dist = muestra.distribucion()
  k = dist.keys()
  k.sort()
  total = 0.0
  for key in k:
    print(str(key) + ' : ' + str(dist[key]) + ' : ' + str(float(dist[key])/muestra.cant))
    total += float(dist[key])/muestra.cant
  print total


  #Leer
  muestra = Muestra(100,100,20)
  muestra.leer_resultados("resultados/100-100_2011-11-24-23-27-13.csv")
  muestra.mostrar_resultados()

  '''

  '''
  import muestras
  m = muestras.Muestra(10,10,100)
  m.generar_resultados()
  m.distribucion_a_lista_tuplas()
  '''
