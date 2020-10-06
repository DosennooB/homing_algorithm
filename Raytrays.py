from numpy import *

#Methode zum Berechnen der Retina ist in Zusammenarbeit mit Herrn Aha und Milczewski entstanden
def see(x, y, res, dim, landmarks):
    position = [float(x), float(y)]
    kreisarray = [None] * res

    for i in range(0, res):
        for c in landmarks:
            if (c[0] == position):
                continue
            q = c[0]
            r = c[1]
            p = position
            v = [cos((pi / (float(res) / 2.)) * i) * float(dim),
                 sin((pi / (float(res) / 2.)) * i) * float(dim)]
            s = add(p, divide(v, sqrt(v[0] ** 2 + v[1] ** 2) * float(2)))

            a = dot(v, v)
            b = 2 * dot(v, subtract(s, q))
            c = dot(s, s) + dot(q, q) - 2 * dot(s, q) - r ** 2

            d = b ** 2 - 4 * a * c
            if d < 0:
                continue
            else:
                e = sqrt(d)
                t = [(-b + e) / (2 * a),
                     (-b - e) / (2 * a)]

                if 0 <= t[0] <= 1 or 0 <= t[1] <= 1:
                    kreisarray[i] = 1
                    continue

        if kreisarray[i] is None:
            kreisarray[i] = 0

    return kreisarray
