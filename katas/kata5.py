tierra = 149597870
jupiter= 778547200
print (tierra)
print (jupiter)
distancia = tierra - jupiter
distancia_millas= distancia * 0.621
print (abs(distancia_millas))

distancia1 = float(input('Distancia del planeta 1 al sol: '))
distancia2 = float(input('Distancia del planeta 1 al sol: '))
distancia = distancia1 - distancia2
distancia= abs(distancia)
distancia_millas= distancia * 0.621
print (f'La distancia en millas es : {abs(distancia_millas)}')