import math
coords = []
for i in range(4):
    coords.append(float(input(f'Введите ')))
coords = input('Введите координаты через пробел: ').split(' ')
print(coords)
result = math.sqrt((int(coords[0]) - int(coords[2]))**2 +(int(coords[1]) - int(coords[3]))**2)
print(round(result,2))