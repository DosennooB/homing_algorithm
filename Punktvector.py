import math

from Marker import Marker
from Retina import Retina


# kleine Klasse zum speichern der Position einer Retina
# wird für berechnung der Abweichung benötigt
class coord:
    x: int
    y: int

    def __init__(self, x, y):
        self.x = x
        self.y = y


# Verwaltet retina und Snapshot berechnet den homevektor und die Abweischung für disen punkt
class PunktVector:
    retina: Retina
    snapshot: Retina
    coordpos: coord
    vecberechnet: complex = 0
    abweichung: float  # in grad

    def __init__(self, retina, snapshot, coord):
        self.coordpos = coord
        self.retina = retina
        self.snapshot = snapshot
    #gibt den vp Vektor von dem Objekt markerret und dem nächsten gleichwertigen Marker auf dem Snapshot zurück
    def vp(self, markerret: Marker, sample):
        a: complex = 0 + 0j
        # Methode um den nächsten Marker auf snapshot zu finden sample ist der Wert des Markers
        markersnap: Marker = self.snapshot.nearestMarker(markerret, sample)
        if (markersnap.mitte + 1 - markerret.mitte) % 1 < 0.5:
            a = complex(-markerret.complex.imag, markerret.complex.real)
            #kehrt den Vektor um falls der Marker mehr als die Hälfte der Retina einnimmt
            if markerret.breite > 0.5:
                a = a * (-1)
        elif (markersnap.mitte + 1 - markerret.mitte) % 1 > 0.5:
            a = complex(markerret.complex.imag, -markerret.complex.real)
            if markerret.breite > 0.5:
                a = a * (-1)
        return a
    #gibt den vt Vektor analog zu vp zurück
    def vt(self, markerret: Marker, sample):
        markersnap: Marker = self.snapshot.nearestMarker(markerret, sample)
        if markersnap.breite > markerret.breite:
            return markerret.complex * 3
        elif markersnap.breite < markerret.breite:
            return -markerret.complex * 3
        else:
            return 0
    #berechnet für eine Retina den Homingvector, die Abweichung und normalisiert den Homingvector
    def berechneVector(self):
        #Berechnung des homingvector
        for rm0 in self.retina.marker0:
            self.vecberechnet = self.vecberechnet + self.vp(rm0, 0)
            self.vecberechnet = self.vecberechnet + self.vt(rm0, 0)
        for rm1 in self.retina.marker1:
            self.vecberechnet = self.vecberechnet + self.vp(rm1, 1)
            self.vecberechnet = self.vecberechnet + self.vt(rm1, 1)
        #Berechnung der Abweichung
        dot = -self.coordpos.x * self.vecberechnet.real + -self.coordpos.y * self.vecberechnet.imag
        betrag = math.sqrt(self.coordpos.y ** 2 + self.coordpos.x ** 2) * math.sqrt(
            self.vecberechnet.imag ** 2 + self.vecberechnet.real ** 2)
        if betrag == 0:
            self.abweichung = 0
        else:
            self.abweichung = math.degrees(math.acos(dot / betrag))
            #Normalisirung des Homingvectors kann auskommentiert
            #ist verantwortlich für Vector bei 0,0
            self.vecberechnet = self.vecberechnet / math.sqrt(self.vecberechnet.real ** 2 + self.vecberechnet.imag ** 2)
        return self.vecberechnet
