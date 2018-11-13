#Goal: read through file and figure out who
# has sent the greatest number of messages
name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)
word = handle.read()
#Reading file
senders = dict()
#Creating a dictionary to store user name and
# the number of messages they have sent
for line in handle:
    if not line.startswith("From:"): continue
    line = line.split()
    line = line[1]
    senders[line] = senders.get(line, 0) + 1
#Looping through the file and picking the second
# value on lines that start with from. If the same
# user appears multiple times a one is added
# if this is a new user they start at 0 but then
# get a subsequent one added
bigcount = None
bigword = None
#Looping through both the key and value in the
# senders dictionary to find the biggest word
# and biggest count
for word, sender in senders.items():
    if bigcount == None or sender > bigcount:
        bigword = word
        bigcount = sender
print(bigword, bigcount)
