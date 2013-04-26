#!/usr/bin/python

import random, sys
from math import *

def error(expr1, expr2, A, B, n, umbral):
  i=1
  c=0
  while i<=n:
    a= random.uniform(A,B)
    b= random.uniform(A,B)  
    if abs(eval(expr1)-eval(expr2))>umbral:
      c+=1
    i+=1
  port = c*100/float(n)
  return port

if __name__=='__main__':   
       expr1 = (sys.argv[1])
       expr2 = (sys.argv[2])
       A= float(sys.argv[3])
       B= float(sys.argv[4])
       n= int(sys.argv[5])
       umbral =(sys.argv[6])
       print "El porcentaje de fallos es", error(expr1, expr2, A, B, n, umbral)
