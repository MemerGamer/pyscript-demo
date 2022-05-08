import matplotlib.pyplot as plt
import math as m
def szabalyos(n):
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
