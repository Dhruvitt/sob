import csv

sample = open('samplefile.txt', 'w')
with open('mempool.csv', 'r') as file:
    reader = csv.reader(file)

    for column in reader:
        for row in reader:
            print(row[3], file = sample)
            print(row[0], file = sample)
sample.close

#to remove empty line with copying only lines
with open('samplefile.txt', 'r') as sample, open('block.txt','a') as blocks:
    for line in sample:
        if not line.isspace():
            blocks.write(line)
sample.close

#to replace semi-colon with newline
f1=open("block.txt","r+")
input=f1.read()
input=input.replace(';','\n')
f2=open("block.txt","w+")
f2.write(input)
f1.close()
f2.close()
