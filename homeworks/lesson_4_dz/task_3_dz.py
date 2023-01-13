



def delAll(lst,a):
    r = []
    for x in lst:
        if x != a:
            r += [x]
    return r
    
def getUniq(x):
    if x == []:
        return []
    if x[0] in x[1:]:
        return getUniq(delAll(x,x[0]))
    else:
        return [x[0]]+getUniq(x[1:])
    
z = getUniq([1,2,3,4,3,2,1,14,9,14,7,5]) 
print (z)