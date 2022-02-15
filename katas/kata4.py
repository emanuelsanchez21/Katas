text = """Interesting facts about the Moon. The Moon is Earth's only satellite. There are several interesting facts about the Moon and how it affects life here on Earth. 
On average, the Moon moves 4cm away from the Earth every year. This yearly drift is not significant enough to cause immediate effects on Earth. The highest daylight temperature of the Moon is 127 C."""

oraciones = text.split(sep= '. ')
palabras_clave = ["average", "temperature", "distance"]
for oracion in oraciones:
    for palabra in palabras_clave:
        if oracion.find(palabra) >= 0:
            oracion = oracion.replace('C.', 'Celsius')
            print (oracion)


name = "Moon"
gravity = 0.00162 # in kms
planet = "Earth"
titulo = f'Gravedad de {name}'
dato = f'{"*"*100}\nNombre del planeta:{planet}\nGravedad en {name}: {gravity} km/s2'    
dato1 = f'{"*"*100}\nNombre del planeta:{planet}\nGravedad en {name}: {gravity*1000} m/s2'  

print (f'{titulo}\n{dato}')
print (f'\n{"-"*100}\n')
print (f'{titulo}\n{dato1}')
