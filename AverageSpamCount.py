fname = input("Enter file name: ")
#fname = 'mbox-short.txt'
fh = open(fname)
#print(fh.read())
count = 0
total = 0
answer = 0
ftotal = 0
fcount = 0

num_list = []
for line in fh:
    if line.startswith("X-DSPAM-Confidence:"): 
        count += 1
        len_line = len(line)
        colonIndex = line.find(":")
        strNum = float(line[colonIndex +1 :len_line])
        total += strNum
    else:
        continue
answer = total / count

print ("Average spam confidence:", answer)
