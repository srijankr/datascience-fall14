import unicodecsv
import re

fw = open("wc1.csv","w")

awards = {}
f = open("worldcup.txt","r")
f.readline()

l = f.readline().strip()
while l!="|}":
    l = f.readline().strip()
    country = l.split("{{fb|")[1].split("}}")[0]
    countryawards = awards.get(country, {})
    for i in range(4):
        pos = re.findall("\|\d{4}]]", f.readline().strip())
        for pos in pos:
            countryawards[pos[1:-2]] = i+1
    awards[country] = countryawards
    f.readline()
    l = f.readline().strip()
f.close()
