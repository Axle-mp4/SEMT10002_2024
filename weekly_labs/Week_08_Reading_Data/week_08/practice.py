import csv

with open('../my_data/student_marks.csv') as file:

    reader = csv.reader(file)

    data = list(reader)

    print(data)