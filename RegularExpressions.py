import re
sum = 0
avg = 0
digit = []
file = open('sum2.txt', 'r')
for line in file:
    digits = re.findall('[0-9]+', line)
    digit = digits + digit
    if not digits:
        continue
    else:
        for n in digits:
            sum += float(n)
            avg = sum / float(n)
print(int(avg))
