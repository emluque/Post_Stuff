class Funcion1:
  
  '''  Funcion  que  calcula  la  cantidad  de  cadenas  de  tamanio  n  formadas  '''
  '''  con  exactamente  m  simbolos  de  un  alfabeto  de  k  simbolos.  '''
  '''  Se  usa  programacion  dinamica, el cache y los metodos son estaticos  '''

  cache_f = {}
  cache_fac = {}

  @staticmethod
  def factorial(n):
    if n in Funcion1.cache_fac: 
      return Funcion1.cache_fac[ n ]
    else:
      if(n==1 or n==0):
        return 1
      else:
        Funcion1.cache_fac[ n ] = n * Funcion1.factorial(n-1)
        return Funcion1.cache_fac[ n ]

  @staticmethod
  def combinatorio(n, m):
    return  Funcion1.factorial(n)  /  (  Funcion1.factorial(n-m)  *  Funcion1.factorial(m)  )  

  @staticmethod
  def f(n, m):
    #No  definidos  
    if(n<m):  return  0
    if(n==0):  return  0
    #Caso  base
    if(n==1  and  m==1):  return  1  
    #Para  optimizar
    if(n==1):  return  m
    if(m==1):  return  1  
    #Testear  Cache
    if  (n,m)  in  Funcion1.cache_f:
      return  Funcion1.cache_f[  (n,m)  ]
    else:
      Funcion1.cache_f[  (n,m)  ]  =  m  *  (  Funcion1.f(n-1,  m)  +  Funcion1.f(n-1,m-1)  )
    return  Funcion1.cache_f[  (n,m)  ]

  @staticmethod
  def g(n, m, k):
    if(n<m):  return  0
    if(k<m):  return  0
    if(n==0):  return  0
    if(m==k):  return Funcion1.f(n,k)
    return  Funcion1.combinatorio(k,m)  *  Funcion1.f(n,m)	

