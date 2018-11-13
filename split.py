#fname = input("Enter file name: ")
fh = open('romeo.txt')
lst = list()
for line in fh:
    words = line.rstrip().split()
    i = 0
    for i in words:
        if i not in lst:
            lst.append(i)
        else:
            continue
lst.sort()
print(lst)
