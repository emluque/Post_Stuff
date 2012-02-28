#!/usr/local/bin/python
# coding: utf-8

import muestras
import utils
import graficos

class Reporte1:
  
  def __init__(self, n, k):
    self.n = n
    self.k = k

  def generar_reporte(self, reg, rango=[10,100,1000,10000,100000]):

    html = '<!doctype html><html><head><meta http-equiv="content-type" content="text/html; charset=UTF-8">'
    html += '<title>Reporte 1: n={n}, k={k}.</title>'.format(n=self.n, k=self.k)
    html += '<link type="text/css" rel="stylesheet" href="styles.css" />'
    html += '</head>'
    html += '<body>'
    
    nav = '<div id="nav"><ul>'
    nav += utils.nav_para_gens(reg.suffix)
    nav += '<li class="titulo">Experimentos</li>'
    
    content = '<div id="content"><h1>Reporte 1: n={n}, k={k}.</h1>'.format(n=self.n, k=self.k)

    m_gen = muestras.Muestra(self.n,self.k, 0)

    abstract = '<div id="abstract"><h2>Explicacion</h2>'
    abstract += '<p class="texto">Es un reporte para investigar graficamente el comportamiento de la funcion con diferentes tamanños de muestra. Tratando de investigar las caracteristicas del caso promedio.</p>'
    abstract += '<h3>Parametros comunes:</h3>'
    abstract += '<p><strong>Tamaño de cadena (n)</strong>: {a}</p>'.format(a=self.n)
    abstract += '<p><strong>Tamaño de alfabeto (k)</strong>: {a}</p>'.format(a=self.k)
    
    abstract += '<p><strong>Tamaño de Poblacion</strong>: '
    try:
      abstract += '{a}'.format(a=float(m_gen.poblacion()))
    except:
      abstract += '{a} * {b}'.format(a=m_gen.k, b= m_gen.n)
    

    abstract += '</p>'


    ran_gen = m_gen.rango_posible()

    abstract += '<p><strong>Mejor Caso</strong>: {a}</p>'.format(a=ran_gen[0])
    abstract += '<p><strong>Peor Caso</strong>: {a}</p>'.format(a=ran_gen[1])

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

    filename = "reporte1-{n}-{k}_".format(n=self.n, k=self.k) + utils.fecha_para_filename() + ".html"
    with open(reg.directorio_reportes + filename, mode="w") as my_file:
      my_file.write( html )
    return filename
    

  def generar_seccion(self, tamanio_muestra, reg):

    subseccion = '<div class="subseccion" id="tmuestra{a}">'.format(a=tamanio_muestra)
    subseccion += '<h2>Experimento con Tamaño de muestra: {a}</h2>'.format(a=tamanio_muestra)
    
    navlink = '<li><p><a href="#tmuestra{a}">Muestra de Tamaño {a}</a></p>'.format(a=tamanio_muestra)

    m = muestras.Muestra(self.n, self.k, tamanio_muestra)
    m.generar_resultados()
    muestra_file = m.guardar_resultados(reg.directorio_muestras)

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

    subseccion += '<figure id="gtmuestra' + str(tamanio_muestra) + '" class="histograma"><img src="' + reg.directorio_imagenes_html + img_file + '" alt="Histograma: n=' + str(self.n) + ', k=' + str(self.k) + ', muestra=' + str(tamanio_muestra)  + '"><figcaption>Tamaño de cadena=' + str(self.n) + ', Tamaño de alfabeto=' + str(self.k) + ', Tamaño de muestra=' + str(tamanio_muestra)  + '</figcaption></figure>'
    subseccion += '<p><small><a href="../muestras/' + muestra_file + '" targe="new">Muestra</a></small></p>'
    subseccion += '</div>'


    navlink += '<p class="link_grafico"><a href="#gtmuestra' + str(tamanio_muestra) + '">Grafico</a></p>'
    navlink += '</li>'

    return navlink, subseccion

'''
if  __name__  ==  '__main__':

  r = Reporte1(10,10)
  r.generar_reporte("resultados", [10,100,1000])
'''
