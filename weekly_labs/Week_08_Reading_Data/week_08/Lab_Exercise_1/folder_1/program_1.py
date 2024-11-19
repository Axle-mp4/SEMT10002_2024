import csv

with open('rainfall.csv', 'r') as f:
    a = f.read()
    print(a)

with open('../unit_description.txt', 'r') as f:
    a = f.readlines()
    print(a[2])


with open('./data/xyz_data.csv','r', encoding = 'utf-8-sig') as f:
    a = csv.reader(f)
    xyz_s = []
    list_1 = []
    for row in a:
        xyz_s.append(row)
    del xyz_s[0]
    print(xyz_s)
    for i in range(len(xyz_s)):
        list_1.append((int(xyz_s[i][0])+int(xyz_s[i][2])))
    print(list_1)