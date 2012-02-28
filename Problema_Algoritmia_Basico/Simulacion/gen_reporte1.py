#!/usr/local/bin/python
# coding: utf-8

import muestras
import utils
import graficos
import reporte1

class GenerarReporte1:
  
  def __init__(self, enes=[10,50,100,200,500], rango=[10,100,1000,10000,100000]):
    self.enes = enes
    self.rango = rango

  def generar_reportes(self, reg):

    html = '<!doctype html><html><head><meta http-equiv="content-type" content="text/html; charset=UTF-8">'
    html += '<title>Reportes de Tipo 1</title>'
    html += '<link type="text/css" rel="stylesheet" href="styles.css" />'
    html += '</head>'
    html += '<body>'

    nav = '<div id="nav"><ul>'
    nav += utils.nav_para_gens(reg.suffix)
    nav += '</ul></div>'

    html += nav
  

    html += '<div id="content"><h1>Reportes de Tipo 1</h1>'

    abstract = '<div class="abstract"><p class="texto">Familia de reportes del tipo 1. En estos reportes, el <em>tamaño de cadena</em> y el <em>tamaño de alfabeto</em> se mantienen constantes y equivalentes, luego se va variando el tamaño de la muestra. Se intenta mostrar graficamente como a mayor tamaño de <em>muestra</em> la distribucion va aproximandose a una grafica determinada.</p>'

    abstract += '<p class="texto">Se intenta asi mismo ver si esta grafica es equivalente para diferentes valores de <em>tamaño de cadena</em> y <em>tamaño de alfabeto</em>.</p>'

    abstract += '<h3>Parametros comunes:</h3>'
    abstract += '<p><strong>Rango de tamaño de Cadena</strong>: '
    abstract += ', '.join([str(x) for x in self.enes])
    abstract += '</p>'
    abstract += '<p><strong>Rango de tamaño de Muestra</strong>: '
    abstract += ', '.join([str(x) for x in self.rango])
    abstract += '</p>'
    abstract += '</div>'
  
    
    html += abstract
    html += '<h2>Reportes Generados</h2>'

    for n in self.enes:
      link = self.generar_reporte1(n, reg)
      html += link

    html += '</div></body></html>'

    filename = reg.directorio_reportes + "reportes-1_" + reg.suffix + ".html"
    with open(filename, mode="w") as my_file:
      my_file.write( html )
    return filename
    

  def generar_reporte1(self, n, reg):

    r = reporte1.Reporte1(n,n)
    r_filename = r.generar_reporte(reg, self.rango)
    link = '<p class="texto"><a href="' + r_filename + '">Tamaño de N y K: ' + str(n) + '</a></p>'
    return link

