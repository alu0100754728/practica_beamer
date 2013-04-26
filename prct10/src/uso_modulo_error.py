#!/usr/bin/python

import random, sys, math
from error import error

l=[('(a*b)**3','(a**3)*(b**3)'),
   ('a/b','1/(b/a)'),
   ('e**(a+b)','(e**a)*(e**b)'),
   ('log10(a**b)','b*log10(a)'),
   ('a-b','-(b-a)'),
   ('(a*b)**4','(a**4)*(b**4)'),
   ('(a+b)**2','(a**2)+(2*a*b)+(b**2)'),
   ('(a+b)*(a*b)','(a**2)-(b**2)'),
   ('log10(a*b)','(log10(a))*(log10(b))'),
   ('a*b','e**((log10(a))+(log10(b)))'),
   ('1/((1/a)+(1/b))','(a*b)/(a+b)'),
   ('a*(((sin(b))**2)+((cos(b))**2))','a'),
   ('sinh(a+b)','((e**a)*(e**b)-(e**(-a)*(e**(-b))))/2'),
   ('tan(a+b)','(sin(a+b))/(cos(a+b))'),
   ('sin(a+b)','((sin(a))*(cos(b)))+((sin(b))*(cos(a)))')]

if __name__=='__main__':   
       A= float(sys.argv[1])
       B= float(sys.argv[2])
       n= int(sys.argv[3])
       resultados = (sys.argv[4])
       umbrales=(1.0e-5,1.0e-10, 1.0e-100,1.0e-1000,1.0e-10000,1.0e-100000)
       
       f = open('resultados','w')
       
       for elem in l:
          expr1 = elem[0]
          expr2 = elem[1]
          f.write('%s \n%s\n'%( expr1, expr2))
          for umbral in umbrales:
	     f.write('%10.1f\n' %error(expr1, expr2, A, B, n, umbral))
       f.close()