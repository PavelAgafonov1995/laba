from math import *;

class Dot:
    def __init__(self, *coordinates):
        self.coordinates = coordinates

    def __str__(self):
        return ",".join(map(str, self.coordinates)) #join вставляет разделитель
        #map применяет функцию к списку

    def distance(self, other):
        if not len(self.coordinates) == len(other.coordinates):
            raise ValueError
        return sum((a-b)**2 for a,b in zip(self.coordinates, other.coordinates))**0.5;

    def middle(self, other):
        if not len(self.coordinates) == len(other.coordinates):
            raise ValueError
        return Dot(*((a+b)/2.0 for a,b in zip(self.coordinates, other.coordinates)));





for A,B in (Dot(1,2,3),Dot(3,4,5)), (Dot(1,2),Dot(3)):
    print (A)
    try:
        print ("{:.3f}".format(A.distance(B)))
        print (A.middle(B))
    except ValueError:
       print ("ERROR")
