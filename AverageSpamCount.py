# Use the file name mbox-short.txt as the file name
fname = input("Enter file name: ")
fh = open(fname)
count = 0
total = 0
answer = 0
ftotal = 0
fcount = 0
for line in fname:
    if not line.startswith("X-DSPAM-Confidence:") : continue
    count = count + 1
    fcount = float(count)
    num = float(line[21:])
    total = total + num
    ftotal = float(total)
answer = ftotal / fcount

print ("Average spam confidence:", answer)
