def chop():
    """gets a list removes first and last element returns nothing"""
    length=len(a)
    del a[length-1]
    del a[0]
    return(None)
def middle(a):
    """gets a list removes first and las elements returns whats left"""
    length=len(a)
    del a[length-1]
    del a[0]
    return(a)
a=["a","b","c","d"]
c=chop()
print(c)
print(a)
a=["a","b","c","d"]
a=middle(a)
print(a)
