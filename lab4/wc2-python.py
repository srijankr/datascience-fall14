import unicodecsv
import re

fw = open("wc2-python-edited.csv","w")
writer = unicodecsv.writer(fw, encoding="utf8", lineterminator="\n")

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

writer.writerow([i for i in range(1930,2015,4)])
for k in awards:
    x = [k]
    print k, awards[k].keys()
    for i in range(1930, 2015, 4):
        x.append('-' if str(i) not in awards[k].keys() else awards[k][str(i)])
    writer.writerow(x)
fw.close()
