fh = open(input())
count = 0
for line in fh:
    if not line.startswith("From "):
        continue
    else:
        words=line.split()
        if len(words)>=2:
            print(words[2])
        else:
            continue