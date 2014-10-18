import unicodecsv

fw = open("cmsc.csv","w")
fw.write("Course No., Section No., Instructor, Seats, Open, Waitlist, Days, Time, Bldg., Room No.\n")

f = open("cmsc.txt","r")
l = f.readline().strip()
while l!='':
    course = l
    l = f.readline().strip()
    while l!= '':
        section = l
        instr = f.readline().strip()
        l = f.readline().strip().split(": ")
        totalseats = l[1].split(",")[0]
        openseats = l[2].split(",")[0]
        waitlist = l[3].split(")")[0]
        l = f.readline().strip().split()
        day = l[0]
        time = ' '.join(l[1:])
        l = f.readline().strip().split()
        bldg = l[0]
        room = l[1]
        fw.write(course + ", " + section + ", " + instr + ", " + totalseats + ", " + openseats + ", " + waitlist + ", " + day + ", " + time + ", " + bldg + ", " + room + "\n")
        l = f.readline().strip()
    l = f.readline().strip()
f.close()
fw.close()        



