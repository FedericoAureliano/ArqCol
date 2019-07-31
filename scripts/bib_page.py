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
    margin-top: 5%;
    margin-bottom: 5%;
    margin-left: auto;
    margin-right: auto;
    min-width: 300px;
    max-width: 85%;
    word-wrap:break-word;
}
</style>
<body>
  <div class="main">
  <h3>Referencias bibliográficas</h3>
  <div class="hbar"> </div><br>
'''

post = '''
  </div>
</body>
</html>
'''

keys = ["Autor", "Año", "Título", "Publicado"]

with open('data/bib.csv') as bib_csv:
    bib = list(csv.DictReader(bib_csv))

results = []

for row in bib:
    result = []
    for k in keys:
        result.append(row[k].replace("\"", ""))
    results.append(result)

results.sort(key=itemgetter(1), reverse=True)
results = sorted(results, key=lambda x: strip_accents(x[0].lower()))

with open("bib.html", "w") as outfile:
    outfile.write(pre)
    for row in results:
        # ref = row["Autor"] + ". " + row["Año"] + " " + row["Título"] + " " + row["Publicado"] + "\n"
        ref = "<p>" + row[0] + " " + row[1] + " " + row[2] + " " + row[3] + "</p>\n"
        outfile.write(ref)
    outfile.write(post)
