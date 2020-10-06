from Marker import Marker

#Klasse extrahiert aus dem Array der Raytrays.see methode Marker und verwaltet diese
class Retina(object):
    array: list =[]
    marker0: list =[]
    marker1: list = []

    def __init__(self, a, marker0:list, marker1:list):

        self.marker1 = marker1
        self.marker0 = marker0
        self.array = a
        anf = 0
        sample = a[len(self.array) - 1]
        # suche ersten Marker und erzeuge ihn beginend bei pos len-1
        while sample == a[anf] and anf < len(self.array):
            anf = anf + 1
        if anf > len(self.array):
            return
        else:
            sample = a[anf]
            marker = self.makeMarker(anf, a[anf])
            if sample == 0:
                self.marker0.append(marker)
            else:
                self.marker1.append(marker)
        # erzeuge weitere marker entnehme Anfang aus Ende aus Marker
        while anf <= marker.end != len(self.array)-1:
            sample = self.array[(marker.end + 1) % len(self.array)]
            marker = self.makeMarker((marker.end + 1) % len(self.array), sample)
            if sample == 0:
                self.marker0.append(marker)
            else:
                self.marker1.append(marker)

    # Suche die erste Abweichung in dem Array und baue aufgrund dessen einen Marker
    def makeMarker(self, anf, sample):
        end = anf
        while self.array[end] == sample:
            end = (end + 1) % len(self.array)
        if end == 0:
            end = len(self.array)
        return Marker(anf, end - 1, len(self.array))
    # kann anhand eines übergebenden Markers und dem Wert des Markers den nächsten Marker auf der eigenen Retina zurück geben
    def nearestMarker(self,marker,sample):
        if sample == 0:
            marklist = self.marker0
        else:
            marklist = self.marker1
        minimum = 1
        nearest = marklist[0]
        for m in marklist:
            if min(abs(m.mitte-marker.mitte), abs(m.mitte-marker.mitte-1)) < minimum:
                minimum = min(abs(m.mitte-marker.mitte), abs(m.mitte-marker.mitte-1))
                nearest = m
        return nearest