import unicodecsv

fw = open("cmsc-python-edited.csv","w")
writer = unicodecsv.writer(fw, encoding="utf8", lineterminator="\n")
writer.writerow(("Course No.","Section No.","Instructor","Seats","Open","Waitlist","Days","Time","Bldg.","Room No."))

f = open("cmsc.txt","r")

l = f.readline().strip()
while l!='':
    course = l
    l = f.readline().strip()
    while l!= '':
        section = l
        instr = f.readline().strip()
        l = f.readline().strip().split(": ")
        print l
        totalseats = l[1].split(",")[0]
        openseats = l[2].split(",")[0]
        waitlist = l[3].split(")")[0]
        l = f.readline().strip().split()
        day = l[0]
        time = ' '.join(l[1:])
        l = f.readline().strip().split()
        bldg = l[0]
        room = l[1]
        writer.writerow((course, section, instr, totalseats, openseats, waitlist, day, time, bldg, room))
        l = f.readline().strip()
    l = f.readline().strip()
f.close()
fw.close()        



