import csv

sample = open('samplefile.txt', 'w')
with open('mempool.csv', 'r') as file:
    reader = csv.reader(file)
    for column in reader:
        for row in reader:
            print(row[3], file = sample)
            print(row[0], file = sample)
sample.close
