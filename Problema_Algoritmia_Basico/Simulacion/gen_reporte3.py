#!/usr/local/bin/python
# coding: utf-8

import muestras
import utils
import graficos
import reporte3

class GenerarReporte3:
  
  def __init__(self, nk=[(10,10),(15,15),(20,20),(50,50)], rango=[100,1000,5000,10000,50000,100000]):
    self.nk = nk
    self.rango = rango

  def generar_reportes(self, reg):

    html = '<!doctype html><html><head><meta http-equiv="content-type" content="text/html; charset=UTF-8">'
    html += '<title>Reportes de Tipo 3</title>'
    html += '<link type="text/css" rel="stylesheet" href="styles.css" />'
    html += '</head>'
    html += '<body>'

    nav = '<div id="nav"><ul>'
    nav += utils.nav_para_gens(reg.suffix)
    nav += '</ul></div>'

    html += nav

    html += '<div id="content"><h1>Reportes de Tipo 3</h1>'

    abstract = '<div class="abstract"><p class="texto">Familia de reportes del tipo 3. En estos reportes, <em>tamaño de muestra</em> se mantiene constantes, y se va variando el <em>tamaño del alfabeto y cadena</em>. Se intenta investigar graficamente como varia el grafico de la distribucion variando los parametros <em>n</em> y <em>k</em>.</p>'


    abstract += '<h3>Parametros comunes:</h3>'
    abstract += '<p><strong>Variaciones de tamaño de Cadena y Alfabeto</strong>: '
    temp = []
    #for x in self.nk:
    #  temp.append()
    abstract += ', '.join([ ("(" + str(x[0]) + "," + str(x[1]) + ")") for x in temp])
    abstract += '</p>'
    abstract += '<p><strong>Rango de tamaño de muestra</strong>: '
    abstract += ', '.join([str(x) for x in self.rango])
    abstract += '</p>'

    abstract += '</div>'
  
    
    html += abstract
    html += '<h2>Reportes Generados</h2>'

    for cant in self.rango:
      link = self.generar_reporte3(cant, reg)
      html += link

    html += '</div></body></html>'

    filename = reg.directorio_reportes + "reportes-3_" + reg.suffix + ".html"
    with open(filename, mode="w") as my_file:
      my_file.write( html )
    return filename
    

  def generar_reporte3(self, cant, reg):

    r = reporte3.Reporte3(cant)
    r_filename = r.generar_reporte(reg, self.nk)
    link = '<p class="texto"><a href="' + r_filename + '">Tamaño de Muestra: ' + str(cant) + '</a></p>'
    return link

