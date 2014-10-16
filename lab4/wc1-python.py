import unicodecsv
import re

fw = open("wc1-python-edited.csv","w")
writer = unicodecsv.writer(fw, encoding="utf8", lineterminator="\n")
writer.writerow(("Team","Year","Position"))

f = open("worldcup.txt","r")
f.readline()

l = f.readline().strip()
while l!="|}":
    l = f.readline().strip()
    country = l.split("{{fb|")[1].split("}}")[0]
    for i in range(4):
        pos = re.findall("\|\d{4}]]", f.readline().strip())
        for pos in pos:
            writer.writerow((country, pos[1:-2], i+1))
    f.readline()
    l = f.readline().strip()
fw.close()
f.close()
