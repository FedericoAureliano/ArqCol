import csv

keys = ["Año", "Autor", "Título", "Publicado", "Sitios", "Etapa", "Región"]

with open('data/arqueologia_de_colombia.csv') as bib_csv:
    bib = list(csv.DictReader(bib_csv))

results = []
results.append(keys)

for row in bib:
    result = []
    for k in keys:
        if k in ["Año"]:
            result.append(row[k].replace("\"", ""))
        else:
            result.append("\"" + row[k].replace("\"", "") + "\"")
    results.append(result)

results = sorted(results, key=lambda x: (x[0], x[1]), reverse=True)

with open("data/bib.csv", "w") as outfile:
    for row in results:
        outfile.write(",".join(row) + "\n")
