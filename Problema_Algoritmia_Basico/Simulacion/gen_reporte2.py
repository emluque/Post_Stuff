#!/usr/local/bin/python
# coding: utf-8

import muestras
import utils
import graficos
import reporte2

class GenerarReporte2:
  
  def __init__(self, enes=[10,50,100,200,500], rango=[5, 10,50,100, 250,500, 750, 1000, 2000, 5000], cant=5000):
    self.enes = enes
    self.rango = rango
    self.cant = cant

  def generar_reportes(self, reg):

    html = '<!doctype html><html><head><meta http-equiv="content-type" content="text/html; charset=UTF-8">'
    html += '<title>Reportes de Tipo 2</title>'
    html += '<link type="text/css" rel="stylesheet" href="styles.css" />'
    html += '</head>'
    html += '<body>'

    nav = '<div id="nav"><ul>'
    nav += utils.nav_para_gens(reg.suffix)
    nav += '</ul></div>'

    html += nav

    html += '<div id="content"><h1>Reportes de Tipo 2</h1>'

    abstract = '<div class="abstract"><p class="texto">Familia de reportes del tipo 2. En estos reportes, el <em>tamaño de cadena</em> y el <em>tamaño de muestra</em> se mantienen constantes, luego se va variando el tamaño del alfabeto. Se intenta investigar graficamente como afecta el tamaño de <em>alfabeto</em> a la distribucion.</p>'


    abstract += '<h3>Parametros comunes:</h3>'
    abstract += '<p><strong>Tamaño de Muestra</strong>: {a}'.format(a=self.cant)
    abstract += '<p><strong>Rango de tamaño de Cadena</strong>: '
    abstract += ', '.join([str(x) for x in self.enes])
    abstract += '</p>'
    abstract += '<p><strong>Rango de tamaño de Alfabeto</strong>: '
    abstract += ', '.join([str(x) for x in self.rango])
    abstract += '</p>'

    abstract += '</div>'
  
    
    html += abstract
    html += '<h2>Reportes Generados</h2>'

    for n in self.enes:
      link = self.generar_reporte2(n, reg)
      html += link

    html += '</div></body></html>'

    filename = reg.directorio_reportes + "reportes-2_" + reg.suffix + ".html"
    with open(filename, mode="w") as my_file:
      my_file.write( html )
    return filename
    

  def generar_reporte2(self, n, reg):

    r = reporte2.Reporte2(n,self.cant)
    r_filename = r.generar_reporte(reg, self.rango)
    link = '<p class="texto"><a href="' + r_filename + '">Tamaño de N: ' + str(n) + '</a></p>'
    return link

