name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)
counts = dict()
for line in handle:
    line = line.strip()
    # if line == "": continue
    words = line.split()
    if words[0] != "Received": continue
    received = words[2].split("")
    counts[received[0]] = counts.get(received[0], 0 ) + 1
list = list()
for key, value in counts.items():
    list.append((key,value))
list.sort()
for email, count in list:
    print(email,count)
