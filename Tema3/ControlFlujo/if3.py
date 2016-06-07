# -*- coding: utf-8 -*-

# Calculo de un descuento de compra

precio=input("¿Cual es el precio de tu portatil?")

if precio >= 700:
	porcentaje=10
	calculo_descuento=precio * porcentaje / 100
	total=precio - calculo_descuento
	print "El precio final ha sido de "+ str(total)+ "euros"
	print "Has ahorrado "+ str(calculo_descuento)+ " euros"
else:
	print "No has tenido descuento"
