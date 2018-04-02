from itertools import groupby

def height_class(h):
    if h > 180:
        return "tall"
    if h < 160:
        return  "short"
    else:
        return "meddle"

frends = [198, 192, 160 ,158, 174, 189]
frends = sorted(frends, key = height_class)

for m, n in groupby(frends, key = height_class):
    print(m)
    print(list(n))