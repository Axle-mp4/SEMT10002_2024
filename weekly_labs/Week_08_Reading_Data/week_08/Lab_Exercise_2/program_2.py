import csv

a = 0
std_dev_sqr = 0

with open('rainfall.csv', 'r', encoding = 'utf-8-sig') as f:
    next(f)
    file_reader = csv.reader(f)
    rows = []
    for row in file_reader:
        rows.append(row)
    rows = rows[0]
    for i in range(len(rows)):
        a += int(rows[i])
    b = a/len(rows)
    print(b)
    for row in rows:
        std_dev_sqr += (((1/len(rows))*((int(row) - b)**2)))
    std_dev = std_dev_sqr**0.5
    print(std_dev)


