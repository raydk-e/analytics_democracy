def is_sorted(l):
    if sorted(l, reverse=True) == l:
        print(l)
        print(sorted(l,reverse=True))
        return "sorted"
    else:
        print(l)
        sorted(l,reverse=True)
        return "Not Sorted"


k = [87,76,65,54,43]
print("The array is: " , is_sorted(k))