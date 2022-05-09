import matplotlib.pyplot as plt
import math as m
'''def szabalyos(n):
    radius = 0.5
    rotation=0
    translation=None
    one_segment = m.pi * 2 / n

    points = [
        (m.sin(one_segment * i + rotation) * radius,
         m.cos(one_segment * i + rotation) * radius)
        for i in range(n+1)]

    if translation:
        points = [[sum(pair) for pair in zip(point, translation)]
                  for point in points]
        
    xs, ys = zip(*points)
    
    plt.figure()
    plt.axis('equal')
    plt.plot(xs,ys)
    plt.show()
szabalyos(4)'''

fig, ax = plt.subplots()

year_1 = [2016, 2017, 2018, 2019, 2020, 2021]
population_1 = [42, 43, 45, 47, 48, 50]

year_2 = [2016, 2017, 2018, 2019, 2020, 2021]
population_2 = [43, 43, 44, 44, 45, 45]

plt.plot(year_1, population_1, marker='o', linestyle='--', color='g', label='Country 1')
plt.plot(year_2, population_2,  marker='d', linestyle='-', color='r', label='Country 2')

plt.xlabel('Year')
plt.ylabel('Population (M)')
plt.title('Year vs Population')
plt.legend(loc='lower right')
plt.show()
fig