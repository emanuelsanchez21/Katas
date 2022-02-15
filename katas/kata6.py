planets = ['Mercurio', 'Venus', 'Tierra', 'Marte', 'Jupiter', 'Saturno', 'Urano', 'Neptuno']
planets.append('Plutón')
print (f'El total de planetas es de: {len(planets)},\nY el ultimo planeta es: {planets[-1]}')


planets = ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Neptune']
nombre= input('Deme el nombre del planeta que quiere buscar: ')
indice= planets.index(nombre)
print (planets[0:indice])

print (planets[indice+1:])
