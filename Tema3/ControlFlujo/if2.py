# -*- coding: utf-8 -*-

dinero =input("¿Te has gastado de 0 a 100 euros?")

if dinero <= 50:
	print "Pagare con efectivo"
elif dinero > 50 and dinero < 100:
	print "Pagare con tarjeta de debito"
else: 
	print "Pagare con tarjeta de credito" 

