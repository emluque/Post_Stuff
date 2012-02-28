#!/usr/local/bin/python
# coding: utf-8

import muestras
import utils
import graficos

class Reporte2:
  
  def __init__(self, n, cant=10000):
    self.n = n
    self.cant = cant

  def generar_reporte(self, reg, rango=[10,20,50,100,200,500]):

    html = '<!doctype html><html><head><meta http-equiv="content-type" content="text/html; charset=UTF-8">'
    html += '<title>Reporte 2: n={n}, muestras={k}.</title>'.format(n=self.n, k=self.cant)
    html += '<link type="text/css" rel="stylesheet" href="styles.css" />'
    html += '</head>'
    html += '<body>'
    
    nav = '<div id="nav"><ul>'
    nav += utils.nav_para_gens(reg.suffix)
    nav += '<li class="titulo">Experimentos</li>'

    
    content = '<div id="content"><h1>Reporte 2: n={n}, muestras={k}.</h1>'.format(n=self.n, k=self.cant)

    abstract = '<div id="abstract"><h2>Explicacion</h2>'
    abstract += '<p class="texto">Es un reporte para investigar graficamente el comportamiento de la funcion manteniendo el tamaño de cadena y el tamanño de muestra, pero variando el tamaño del alfabeto. Se intenta ver como se modifica el grafico de la funcion.</p>'
    abstract += '<h3>Parametros comunes:</h3>'
    abstract += '<p><strong>Tamaño de cadena (n)</strong>: {a}</p>'.format(a=self.n)
    abstract += '<p><strong>Tamaño de muestra</strong>: {a}</p>'.format(a=self.cant)
    abstract += '<p><strong>Rango de tamaño de Alfabeto</strong>: '
    abstract += ', '.join([str(x) for x in rango])
    abstract += '</p>'
    abstract += '</div>'

    content += abstract

    for x in rango:
      navlink, subsec = self.generar_seccion(x, reg)
      nav += navlink
      content += subsec
    
    nav += '</ul></div>'
    content += '</div>'

    html += nav
    html += content
    html += '</body></html>'

    filename = "reporte2-{n}-{k}_".format(n=self.n, k=self.cant) + utils.fecha_para_filename() + ".html"
    with open(reg.directorio_reportes + filename, mode="w") as my_file:
      my_file.write( html )
    return filename
    

  def generar_seccion(self, tamanio_alfabeto, reg):

    subseccion = '<div class="subseccion" id="talfabeto{a}">'.format(a=tamanio_alfabeto)
    subseccion += '<h2>Experimento con Tamaño de alfabeto: {a}</h2>'.format(a=tamanio_alfabeto)
    
    navlink = '<li><p><a href="#talfabeto{a}">Alfabeto de Tamaño {a}</a></p>'.format(a=tamanio_alfabeto)

    m = muestras.Muestra(self.n, tamanio_alfabeto, self.cant)

    m.generar_resultados()
    muestra_file = m.guardar_resultados(reg.directorio_muestras)
    subseccion += '<h3>Parametros independientes a la muestra:</h3>'
    subseccion += '<p><strong>Tamaño de cadena (n)</strong>: {a}</p>'.format(a=m.n)
    subseccion += '<p><strong>Tamaño de alfabeto (k)</strong>: {a}</p>'.format(a=m.k)
    
    subseccion += '<p><strong>Tamaño de Poblacion</strong>: '
    try:
      subseccion += '{a}'.format(a=float(m.poblacion()))
    except:
      subseccion += '{a} * {b}'.format(a=m.k, b= m.n)
    subseccion += '</p>'


    ran_gen = m.rango_posible()
    subseccion += '<p><strong>Mejor Caso</strong>: {a}</p>'.format(a=ran_gen[0])
    subseccion += '<p><strong>Peor Caso</strong>: {a}</p>'.format(a=ran_gen[1])

    subseccion += '<h3>Resultados:</h3>'
    subseccion += '<p><strong>Promedio</strong>: {a}</p>'.format(a=m.promedio())
    subseccion += '<p><strong>Desvio Estandard</strong>: {a}</p>'.format(a=m.desvio_estandard())
    subseccion += '<p><strong>Mediana</strong>: {a}</p>'.format(a=m.mediana())

    subseccion += '<p><strong>Modo</strong>: '
    modos = m.modo()
    subseccion += ', '.join([str(x) for x in modos]) 
    subseccion += '</p>'
        
    subseccion += '<p><strong>Minimo</strong>: {a}</p>'.format(a=(m.rango())[0])
    subseccion += '<p><strong>Maximo</strong>: {a}</p>'.format(a=(m.rango())[1])
    subseccion += '<h4>Distribucion</h4>'

    hist = graficos.Histograma(m)
    img_file = hist.generar_histograma(reg.directorio_imagenes)

    subseccion += '<figure class="histograma" id="gtalfabeto' + str(tamanio_alfabeto) +'"><img src="' + reg.directorio_imagenes_html + img_file + '" alt="Histograma: n=' + str(self.n) + ', k=' + str(tamanio_alfabeto) + ', muestra=' + str(self.n)  + '"><figcaption>Tamaño de cadena=' + str(self.n) + ', Tamaño de alfabeto=' + str(tamanio_alfabeto) + ', Tamaño de muestra=' + str(self.cant)  + '</figcaption></figure>'
    subseccion += '<p><small><a href="../muestras/' + muestra_file + '" targe="new">Muestra</a></small></p>'
    subseccion += '</div>'

    navlink += '<p class="link_grafico"><a href="#gtalfabeto' + str(tamanio_alfabeto) +'">Grafico</a></p>'
    navlink += '</li>'

    return navlink, subseccion

'''
if  __name__  ==  '__main__':

  r = Reporte2(20,5000)
  r.generar_reporte("resultados", [5, 10,50,100, 250,500, 750, 1000, 2000, 5000])
'''
