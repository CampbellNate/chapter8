lst=[]
while True:
    a=input("Enter a Number:")
    if a == "done":
        break
    else:
        lst.append(a)
        print(a)
print("max is",max(lst))
print("min is",min(lst))
print(lst)