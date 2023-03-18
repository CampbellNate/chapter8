fname = input("Enter file name: ")
fh = open(fname)
lst = list()
for line in fh:
    hold=line.split()
    for x in hold:
        if x not in lst:
            lst.append(x)
lst.sort()
print(lst)
