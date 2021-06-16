import csv

sample = open('samplefile.txt', 'w')
with open('mempool.csv', 'r') as file:
    reader = csv.reader(file)
    for column in reader:
        print(column[3], file = sample)
        print(column[0], file = sample)
sample.close
