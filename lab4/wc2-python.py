import unicodecsv
import re

fw = open("wc2.csv","w")

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


for i in range(1930,2015,4):
    fw.write(" ," + str(i))
fw.write("\n")
for k in awards:
    fw.write(k)
    for i in range(1930, 2015, 4):
        fw.write(', -' if str(i) not in awards[k].keys() else ', ' + str(awards[k][str(i)]))
    fw.write("\n")
fw.close()
