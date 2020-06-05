import csv
from math import sin, cos, sqrt, atan2, radians

# approximate radius of earth in km
R = 6373.0

def k_min_distance(u, k):
    best_r = [""]*k
    best_d = [-1]*k
    
    for p in known:
        d = distance(p, u)
        for i in range(k):
            if d < best_d[i] or best_d[i] < 0:
                best_d[i] = d
                best_r[i] = p["Región"]
                break

    return best_r

def distance(p, u):
    lat1 = radians(float(".".join(p["Latitud"].split(".", 2)[:2])))
    lon1 = radians(float(".".join(p["Longitud"].split(".", 2)[:2])))
    lat2 = radians(float(".".join(u["Latitud"].split(".", 2)[:2])))
    lon2 = radians(float(".".join(u["Longitud"].split(".", 2)[:2])))

    dlon = lon2 - lon1
    dlat = lat2 - lat1

    a = sin(dlat / 2)**2 + cos(lat1) * cos(lat2) * sin(dlon / 2)**2
    c = 2 * atan2(sqrt(a), sqrt(1 - a))

    distance = R * c
    return distance

with open('data/mapa.csv') as mapa_csv:
    puntos = list(csv.DictReader(mapa_csv))

known = []
unknown = []

for p in puntos:
    if p["Región"] == "" and p["Latitud"] != "" and p["Longitud"] != "":
        unknown.append(p)
    elif p["Latitud"] != "" and p["Longitud"] != "":
        known.append(p)

for i in range(len(unknown)):
    closest = k_min_distance(unknown[i], 5)
    if (all([p == closest[0] for p in closest])): 
        unknown[i]["Región"] = closest[0] 
        print(unknown[i]["Sitio"], "assigned to", unknown[i]["Región"])

with open("data/mapa2.csv", "w") as outfile:
    keys = [str(t) for t in puntos[0].keys()]
    outfile.write(",".join(keys) + "\n")
    for row in known:
        row = [row[t] for t in keys]
        row[0] = "\"%s\"" % row[0]
        row[1] = "\"%s\"" % row[1]
        row[2] = "\"%s\"" % row[2]
        outfile.write(",".join(row) + "\n")
    for row in unknown:
        row = [row[t] for t in keys]
        row[0] = "\"%s\"" % row[0]
        row[1] = "\"%s\"" % row[1]
        row[2] = "\"%s\"" % row[2]
        outfile.write(",".join(row) + "\n")

