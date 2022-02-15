new_planets = ''
planets = []

while new_planets.lower() != 'done':
    new_planets= input ('Dame el planeta:  ')
    if new_planets != '' and new_planets.lower() != 'done':
        planets.append(new_planets.capitalize())
indice= 1
for planeta in planets:
    print (f'{indice}.- {planeta}')
    indice += 1     

