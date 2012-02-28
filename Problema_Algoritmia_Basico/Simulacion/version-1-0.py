#!/usr/local/bin/python
# coding: utf-8

import gen_reporte1
import gen_reporte2
import gen_reporte3
import utils

'''
  Notas:
    En cadena y alfabeto = 500, el histograma se come toda la memoria y se tilda el script, independientemente del tamaño de Muestra.
    Por lo que dejamos como tamaño maximo: 200

'''

#Configuracion
reg = utils.registry

reg.directorio_reportes = "resultados/reportes/"
reg.directorio_imagenes = "resultados/reportes/imagenes/"
reg.directorio_muestras = "resultados/muestras/"
reg.directorio_imagenes_html = "imagenes/"

if  __name__  ==  '__main__':

  reg.suffix = utils.fecha_para_filename()

  #Version Rapida, Con Muestras pequeñas
  #Reporte 1
  print("Reportes de tipo 1")
  r1 = gen_reporte1.GenerarReporte1([10, 25], [10,20])
  r1.generar_reportes(reg)

  #Reporte2
  print("Reportes de tipo 2")
  r2 = gen_reporte2.GenerarReporte2([10, 25], rango=[5, 7], cant=10)
  r2.generar_reportes(reg)

  #Reporte3
  print("Reportes de tipo 3")
  r3 = gen_reporte3.GenerarReporte3([(10,10),(25,25)], [10,100])
  r3.generar_reportes(reg)

  '''
  #Version Completa, Muestras Grandes
  #Reporte 1
  print("Reportes de tipo 1")
  r1 = gen_reporte1.GenerarReporte1([10, 25, 50, 100, 150, 200], [10,100,1000,10000,100000])
  r1.generar_reportes(reg)

  #Reporte2
  print("Reportes de tipo 2")
  r2 = gen_reporte2.GenerarReporte2([10, 25, 50, 100, 150, 200], rango=[3, 5, 7, 10, 25, 50, 75, 100, 150, 200, 250, 500, 1000, 2000, 5000,10000, 10000000000], cant=50000)
  r2.generar_reportes(reg)

  #Reporte3
  print("Reportes de tipo 3")
  r3 = gen_reporte3.GenerarReporte3([(10,10),(25,25),(50,50),(100,100),(150,150), (200,200)], [10,100,500,1000,5000,10000,50000])
  r3.generar_reportes(reg)
  '''


  html = '<!doctype html><html><head><meta http-equiv="content-type" content="text/html; charset=UTF-8">'
  html += '<title>Reportes Generados</title>'
  html += '<link type="text/css" rel="stylesheet" href="styles.css" />'
  html += '</head>'
  html += '<body>'

  nav = '<div id="nav"><ul>'
  nav += utils.nav_para_gens(reg.suffix)
  nav += '</ul></div>'

  html += nav
 
  html += '<div id="content"><h1>Trabajo Final de Lenguajes de Scripting</h1>'
  html += '<p><strong>Alumno</strong>: Emiliano Martínez Luque</p>'
  html += '<p><strong>Legajo</strong>: 43556</p>'
  html += '<p><strong>Docente</strong>: Ares</p>'
  html += '<p><strong>Cursada</strong>: Viernes a la Noche, Segundo Cuatrimestre 2011</p>'
  html += '<h2>Descripción General</h2>'
  html += '<p class="texto">Se trata de una serie de scripts en <em>Python</em> para analizar el comportamiento de un algoritmo bajo diferentes inputs. Se generan una serie de reportes en los que se varian algunos de los parametros del input y se analizan los resultados.</p>'
  html += '<h2>Motivación</h2>'
  html += '<p class="texto">Por una cuestión de ejercitación personal, estuve realizando el análisis de complejidad de un algoritmo genérico básico. Al comenzar este análisis resulto relativamente fácil tanto determinar la corrección del algoritmo, como buscar estructuras de datos para mejorarlo, así como determinar matematicamente el mejor y el peor caso. Sin embargo la definición de una función matematica para determinar el comportamiento del <em>caso promedio</em> no resulto tan inmediato. Se busca con este trabajo proveer datos exploratorios para ayudar en este proceso.</p>'
  html += '<h3>Descripción del Algoritmo a Analizar</h3>'
  html += '<p class="texto">Es un algoritmo sencillo en el que dado una lista de números ordenados, por ejemplo: [1,3,3,6,4,8,6,4,10], retorna la misma lista manteniendo el orden pero sacando los duplicados, por ejemplo: [1,3,6,4,8,10]. Básicamente se crea otra lista <em>pasados</em> y se va iterando por la lista original y comparando contra <em>pasados</em>. En cada iteración si el valor preexiste en <em>pasados</em> se borra el valor de la lista original, si no preexiste, se lo agrega a <em>pasados</em> y se continua el proceso. Definitivamente el algoritmo puede ser mejorado usando mejores estructuras de datos (por ejemplo: binary search trees). Pero, dado que ese análisis ya lo he hecho, el objetivo de este Trabajo es otro, a saber analizar el comportamiento de la función sobre una distribución de probabilidades aleatorias.</p>'
  html += '<p>Una implementación en C del algoritmo para testear sobre linea de comandos, puede ser accedida en la carpeta <code>algoritmo</code> bajo el nombre de <code>algoritmo.c</code>.</p>'
  html += '<p>Una version modificada de esta implementación llamada <code>algo.c</code> es la que usa el script para generar las muestras.</p>.'
  html += '<h2>Descripción Detallada del Trabajo</h2>'
  html += '<p class="texto">Las muestras se generan corriendo un subproceso <code>algo</code> (originalmente codificado en C) desde los scripts de Python, con una lista de enteros separados por coma como argumento de la llamada. Esta lista randomizada es generada dentro del script de Python. El subproceso <code>algo</code> retorna por <code>stdout</code> un entero que es el resultado del calculo del costo de la porción del algoritmo que nos interesa analizar. El script de Python lee este valor. Luego de generar una cantidad determinada de experimentos con diferentes parametros de input y diferentes tamaños de muestras se generan reportes en HTML, que incluyen los resultados de las variables en cada experimento así como gráficos de la distribución. Así mismo se guardan las diferentes muestras en el sistema de archivos.</p>.'
  html += '<p>Se usan conceptos generales vistos en las materias Estadisca y Modelos y Simulación.</p>.'

  html += '<h2>Por que se Utilizo Python?</h2>'
  html += '<p class="texto">De los lenguajes vistos durante la cursada, aquellos que podrían haber sido usados para un trabajo de este tipo son: Ruby, Perl y Python, dado que AWK y Bash no tienen la capacidad expresiva, ni la intención de cubrir este tipo de casos de uso y Javascript es mayoritariamente ( a pesar de los avances actuales de Node.JS ) un lenguaje para desarrollo en clientes web. Se prefirió Python por el soporte y sus capacidades para procesamiento matematico, así como por su expresividad.</p>.'
  html += '<h2>Conceptos de programación en Python usados en el trabajo</h2>'
  html += '<ul>'
  html += '<li>Uso de tipos Primitivos: (Strings, Ints, Longs, Floats, Boolean)</li>'
  html += '<li>Uso de Estructuras de datos incluidas en el lenguaje: (Diccionarios, Listas, Tuplas)</li>'
  html += '<li>Uso de Librerias externas: (NumPy, Matlibplot)</li>'
  html += '<li>Creación e interface con Subprocesos</li>'
  html += '<li>Creación y lectura de archivos</li>'
  html += '<li>OOP</li>'
  html += '<li>Organización de Programas (modulos y sus correspondientes namespaces, configuracion global)</li>'
  html += '</ul>'
  html += '<p>Se intento tambíen hacer una interface gráfica moderna y bien presentada.</p>'

  html += '<h2>Advertencia</h2>'
  html += '<p class="texto">Por el costo computacional de generar las simulaciones, en la presentación del final los reportes generados en vivo serán pequeños. Se presenta así mismo un reporte completo y amplio (con mayores tamaños de muestra) pregenerado sin limitaciones de tiempo y en una maquina con mayor capacidad de procesamiento y memoria.</p>.'
  html += '</div></body></html>'

  filename = reg.directorio_reportes + "index_" + reg.suffix + ".html"
  with open(filename, mode="w") as my_file:
    my_file.write( html )
  print("El Script se ha ejecutado con exito.")

