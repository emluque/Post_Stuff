import matplotlib.pyplot as plt
import utils

class Histograma:
  ''' Clase para generar un histograma a partir de una distribucion de valores '''

  def __init__(self, muestra):
    self.muestra = muestra

  def generar_histograma(self, directorio):
    rango_posible = self.muestra.rango_posible()
    n, bins, patches = plt.hist( self.muestra.resultados, range( rango_posible[0], rango_posible[1] ), normed=1, facecolor='green', alpha=0.75)
    plt.xlabel('Costo')
    plt.ylabel('Probabilidad')
    plt.title('Histograma: n={n}, k={k}, cant={cant}'.format(n=self.muestra.n, k=self.muestra.k, cant=self.muestra.cant) )
    plt.grid(True)
    fecha = utils.fecha_para_filename()
    filename = str(self.muestra.n) + "-" + str(self.muestra.k) + "-" + str(self.muestra.cant) + "_" + fecha + ".png"
    plt.savefig( directorio + filename ,dpi=(640/8))
    plt.close()
    return filename


if  __name__  ==  '__main__':
  import muestras

  '''
  cants = [10, 100, 1000, 10000, 100000]
  for i in cants:
    muestra = muestras.Muestra(8,8,i)
    muestra.generar_resultados()
    muestra.mostrar_resultados()
    hist = Histograma(muestra)
    hist.generar_histograma("resultados/reportes/imagenes")

  muestra = muestras.Muestra(6,6, (6**6))
  for a1 in range(0,6):
    for a2 in range(0,6):
      for a3 in range(0,6):
        for a4 in range(0,6):
          for a5 in range(0,6):
            for a6 in range(0,6):
              muestra.resultados.append( muestra.generar_resultado( ",".join( [str(x) for x in [a1, a2, a3, a4, a5, a6]]) ) )

  hist = Histograma(muestra)
  hist.generar_histograma("resultados/reportes/imagenes")
  
  muestra = muestras.Muestra(100,100,100000)
  muestra.generar_resultados()
  hist = Histograma(muestra)
  hist.generar_histograma("resultados/reportes/imagenes")
  '''
