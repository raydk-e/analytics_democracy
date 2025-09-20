l = [5,7,8,3,87,43,45,53,12]
l.sort(reverse=True)
print(l)
i = int(input("provide the nth position to find the highest: "))

for j in range(0, len(l)):
    if j == i-1:
        print(l[j])

