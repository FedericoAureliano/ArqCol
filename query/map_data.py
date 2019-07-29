import csv

keys = ["Sitio", "Región", "Referencia", "Latitud", "Longitud"]

with open('data/cronologia_colombiana.csv') as cronologia_csv:
    cronologia = list(csv.DictReader(cronologia_csv))

etapas = []

for c in cronologia:
    if c["Etapa"] not in etapas and c["Etapa"] != "":
        etapas.append(c["Etapa"])

with open('data/sitios_arqueologicos.csv') as sitios_csv:
    sitios = list(csv.DictReader(sitios_csv))


result = [keys + etapas + ["Total"]]

for sitio in sitios:
    row = []

    for k in keys:
        if k in ["Latitud", "Longitud"]:
            row.append(sitio[k])
        else:
            row.append("\"" + sitio[k] + "\"")

    total = 0
    for etapa in etapas:
        count = 0
        for c in cronologia:
            if c["Sitio"] == sitio["Sitio"] and c["Etapa"] == etapa:
                count += 1
                total += 1 
        row.append(str(count))
    
    row.append(str(total))

    result.append(row)


with open("data/mapa.csv", "w") as outfile:
    for row in result:
        outfile.write(",".join(row) + "\n")

