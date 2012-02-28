import datetime
import time

def fecha_para_filename():
    d = datetime.datetime.fromtimestamp(time.time())
    fecha = str(d.year) + '-' + str(d.month) + '-' + str(d.day )+ '-' + str(d.hour) + '-' + str(d.minute) + '-' + str(d.second)
    return fecha

def nav_para_gens(suffix):
  nav = '<li><p><a href="index_' + suffix + '.html">Home</a></p></li>'
  nav += '<li><p><a href="reportes-1_' + suffix + '.html">Reportes de Tipo 1</a></p></li>'
  nav += '<li><p><a href="reportes-2_' + suffix + '.html">Reportes de Tipo 2</a></p></li>'
  nav += '<li><p><a href="reportes-3_' + suffix + '.html">Reportes de Tipo 3</a></p></li>'
  return nav

class registry:
  pass
