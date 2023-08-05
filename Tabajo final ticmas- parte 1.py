sueldo_promedio=( float((300*6 + 500*4+ 700*2)/12))
print(" El sueldo promedio  de Juan es de : " + str(sueldo_promedio) +  " dolares")

if sueldo_promedio < 300:
    print(" Juan se encuentra cobrando un sueldo bajo de :" + str(sueldo_promedio) +  " dolares")
elif sueldo_promedio > 300 and  sueldo_promedio< 900: 
    print(" Juan se encuentra cobrando un sueldo normal de : " + str(sueldo_promedio)+"dolares")
else:
    print( " Juan se encuentra cobrando un sueldo mejor de lo normal de : " + str(sueldo_promedio) +  " dolares")
