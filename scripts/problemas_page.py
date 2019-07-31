from operator import itemgetter
import csv
import unicodedata


def strip_accents(s):
   return ''.join(c for c in unicodedata.normalize('NFD', s)
                  if unicodedata.category(c) != 'Mn')


pre = '''
<!DOCTYPE html>
<html>
<head>
  <title>Sitios Arqueológicos de Colombia</title>
  <meta charset="utf-8" />
  <script src="https://d3js.org/d3.v3.min.js"></script>
  <link href="https://fonts.googleapis.com/css?family=Rubik&display=swap" rel="stylesheet">
  <link rel="stylesheet" type="text/css" href="main.css">
  <link rel="shortcut icon" type="image/png" href="./images/favicon.png" />
  <script async src="https://www.googletagmanager.com/gtag/js?id=UA-65924431-1"></script>
  <script>
    window.dataLayer = window.dataLayer || [];
    function gtag() {
      dataLayer.push(arguments);
    }
    gtag('js', new Date());
    gtag('config', 'UA-65924431-1');
  </script>
</head>
<style>
body {
    min-width: 400px;
    max-width: 1000px;
}
.main {
    margin-top: auto;
    margin-bottom: auto;
    margin-left: auto;
    margin-right: auto;
    min-width: 300px;
    max-width: 85%;
    word-wrap:break-word;
}
</style>
<body>
  <div class="main">
  <h3>Problemas Identificados</h3>
  <div class="hbar"> </div><br>
'''

post = '''
  </div>
</body>
</html>
'''

with open('data/mapa.csv') as mapa_csv:
    mapa = list(csv.DictReader(mapa_csv))

region = []
coord = []

for row in mapa:
    if len(row["Sitio"]) < 2:
        continue
    if len(row["Región"]) < 2:
        region.append(row["Sitio"])
    if row["Latitud"] == "" or row["Latitud"] == "":
        coord.append(row["Sitio"])

region = sorted(region, key=lambda x: strip_accents(x[0].lower()))
coord = sorted(coord, key=lambda x: strip_accents(x[0].lower()))

with open("problemas.html", "w") as outfile:
    outfile.write(pre)

    outfile.write("<h4>Sitios sin coordenadas</h4>\n")
    for row in coord:
        outfile.write("<p>" + row + "</p>\n")

    outfile.write("<br><br><h4>Sitios sin región</h4>\n")
    for row in region:
        outfile.write("<p>" + row + "</p>\n")

    outfile.write(post)
