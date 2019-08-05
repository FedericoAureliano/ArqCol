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


result = [keys + etapas + ["Total"] + ["Fechas"]]

for sitio in sitios:
    row = []

    for k in keys:
        if k in ["Latitud", "Longitud"]:
            row.append(sitio[k])
        else:
            row.append("\"" + sitio[k].replace("\"", "\'") + "\"")

    total = 0
    fechas = []
    for etapa in etapas:
        count = 0
        for c in cronologia:
            if c["Sitio"] == sitio["Sitio"] and c["Etapa"] == etapa:
                count += 1
                total += 1
                fecha = c["Fecha cristiana"]
                if len(fecha) > 0:
                    fechas.append(int(fecha))
        row.append(str(count))
    
    row.append(str(total))
    row.append("; ".join([str(f) for f in sorted(fechas)]))

    result.append(row)


with open("data/mapa.csv", "w") as outfile:
    for row in result:
        row[0] = s = row[0].split('---', 1)[0] + "\""
        outfile.write(",".join(row) + "\n")

