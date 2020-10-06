
from Retina import Retina
import matplotlib.pyplot as plt
import statistics
from Punktvector import PunktVector, coord
from Raytrays import see
res = 80 #Auflösug der Retina
dim = 34 #für Raytrays gibt an wie weit der Strahl in den Raum zeigt
landmarks = [[[3.5, 2], 0.5],
             [[3.5, -2], 0.5],
             [[0, -4], 0.5]
             ]
coordxlist = []
coordylist = []
vecxlist = []
vecylist = []
abweichunglist = []
def main():
    conter = 1
    marker0r: list = []
    marker1r: list = []
    marker0s: list = []
    marker1s: list = []
    #baut den Snapshot auf mit dem verglichen werden soll
    b= see(0,0,res,dim,landmarks)
    snap = Retina(b,marker0s,marker1s)
    for j in range(-12,12):
        for i in range(-12, 12):
            marker0r.clear()
            marker1r.clear()
            #baut die Retina am entsprechenden Punkt auf
            a = see(i, j, res, dim, landmarks)
            ret = Retina(a, marker0r, marker1r)
            #berechnet Homevector und die Abweichung
            ve = PunktVector(ret, snap, coord(j, i))
            ve.berechneVector()
            #setzt die berechneten werte in listen zur weiter verarbeitung
            coordxlist.append(ve.coordpos.x)
            coordylist.append(ve.coordpos.y)
            vecxlist.append(ve.vecberechnet.real)
            vecylist.append(ve.vecberechnet.imag)
            print("Vector ",conter," berechnet")
            conter +=1
            abweichunglist.append(ve.abweichung)

    print(statistics.mean(abweichunglist))
    grafik()
#zeichnet die Landmarks und Vektoren in ein Grafik
def grafik():
    fig, ax = plt.subplots()
    q = ax.quiver(coordxlist, coordylist, vecxlist, vecylist)
    plt.plot([landmarks[0][0][0], landmarks[1][0][0], landmarks[2][0][0]],
             [landmarks[0][0][1], landmarks[1][0][1], landmarks[2][0][1]], "ob")
    plt.show()
if __name__ == "__main__":
    main()
