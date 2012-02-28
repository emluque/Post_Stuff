#!/usr/local/bin/python
# coding: utf-8

import muestras
import utils
import graficos

class Reporte3:
  
  def __init__(self, cant):
    self.cant = cant

  def generar_reporte(self, reg, rango=[(10,10),(15,15),(20,20),(50,50),(100,100),(200,200)]):

    html = '<!doctype html><html><head><meta http-equiv="content-type" content="text/html; charset=UTF-8">'
    html += '<title>Reporte 3: cant={a}.</title>'.format(a=self.cant)
    html += '<link type="text/css" rel="stylesheet" href="styles.css" />'
    html += '</head>'
    html += '<body>'
    
    nav = '<div id="nav"><ul>'
    nav += utils.nav_para_gens(reg.suffix)
    nav += '<li class="titulo">Experimentos</li>'


    
    content = '<div id="content"><h1>Reporte 3: cant={a}.</h1>'.format(a=self.cant)

    abstract = '<div id="abstract"><h2>Explicacion</h2>'
    abstract += '<p class="texto">Es un reporte para investigar graficamente el comportamiento de la funcion manteniendo el tamaño de muestra constante y variando el tamaño de cadena y el tamaño de muestra. Se intenta ver como se modifica el grafico de la funcion.</p>'
    abstract += '<h3>Parametros comunes:</h3>'
    abstract += '<p><strong>Tamaño de muestra</strong>: {a}</p>'.format(a=self.cant)

    content += abstract

    for x in rango:
      navlink, subsec = self.generar_seccion(x[0], x[1], reg)
      nav += navlink
      content += subsec
    
    nav += '</ul></div>'
    content += '</div>'

    html += nav
    html += content
    html += '</body></html>'

    filename = "reporte3-{a}_".format(a=self.cant) + utils.fecha_para_filename() + ".html"
    with open(reg.directorio_reportes + filename, mode="w") as my_file:
      my_file.write( html )
    return filename
    

  def generar_seccion(self, n,k, reg):

    subseccion = '<div class="subseccion" id="t{a}-{b}">'.format(a=n, b=k)
    subseccion += '<h2>Experimento con Tamaño de Cadena: {a} ; Tamaño de alfabeto: {b} </h2>'.format(a=n, b=k)
    
    navlink = '<li><p><a href="#t{a}-{b}">Alfabeto de Tamaño {a}</a></p>'.format(a=n, b=k)

    m = muestras.Muestra(n, k, self.cant)

    m.generar_resultados()
    muestra_file = m.guardar_resultados(reg.directorio_muestras)
    subseccion += '<h3>Parametros:</h3>'
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

    subseccion += '<figure class="histograma" id="gt' + str(n) + '-' + str(k) + '"><img src="' + reg.directorio_imagenes_html + img_file + '" alt="Histograma: n=' + str(n) + ', k=' + str(k) + ', muestra=' + str(self.cant)  + '"><figcaption>Tamaño de cadena=' + str(n) + ', Tamaño de alfabeto=' + str(k) + ', Tamaño de muestra=' + str(self.cant)  + '</figcaption></figure>'
    subseccion += '<p><small><a href="../muestras/' + muestra_file + '" targe="new">Muestra</a></small></p>'
    subseccion += '</div>'

    navlink += '<p class="link_grafico"><a href="#gt' + str(n) + '-' +  str(k) + '">Grafico</a></p>'
    navlink += '</li>'

    return navlink, subseccion


if  __name__  ==  '__main__':

  r = Reporte3(5000)
  r.generar_reporte("resultados", [(10,10),(15,15),(20,20),(50,50)])

