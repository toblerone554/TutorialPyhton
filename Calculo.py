#!/usr/bin/python
#coding: utf-8

# Vamos a calcular el pago del Iva e Irpf de una factura

factura_bruto = 1000 # Total de la factura en bruto

print "El total bruto de la factura es de ",factura_bruto, "euros"

iva = 21 # Iva al 21% 

irpf = 15 # Irpf al 15%

print "Hay que restar el Iva y el Irpf"

# Calculamos el IVA multiplicando el iva por el total entre 100

factura_iva= factura_bruto * iva /100 

# Calculamos el Irpf multiplicando el 15% por la factura_bruto

factura_irpf = (factura_bruto - irpf % 100) - factura_iva

print "Vamos a cobrar " ,factura_irpf, "euros"
