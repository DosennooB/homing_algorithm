import math

#Diese Klasse enthält alle Werte eines Makers
class Marker:
    complex = 0 #Richtungsvektor auf der Retina zum addieren mit Vektoren
    mitte = 0  # Mitte des Makers von 0 bis 1
    breite = 0  # in Radiand
    anf = -1
    end = -1

    def __init__(self, anf, end, length):
        self.end = end
        self.anf = anf
        if anf <= end:
            self.mitte = (anf + end) / 2 / length
            self.breite = (end - anf+1) / length
        else:
            self.mitte = (end + length + anf) / 2 / length % 1
            self.breite = (length - anf + end+1) / length
        self.complex = complex(math.sin(self.mitte * 2 * math.pi), math.cos(self.mitte * 2 * math.pi))
