import csv

file =  "/home/deepak/projects/my_data.csv"

with open(file, 'r') as f:
    reader = csv.reader(f)
    next(reader)
    for t in reader:
        for i in range(len(t)):
            # print(t[i])
            for j in range(len(t[i])):
                print(t[i][j])


