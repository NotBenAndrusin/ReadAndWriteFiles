import csv

infile = open('customers.csv', 'r')

csvfile = csv.reader(infile, delimiter=',')

next(csvfile) #This skips the first line/rendition


for record in csvfile:
    print('fname:', record[1])
    print('lname:', record[2])
    print('Country:', record[4])
    input()
# output is "John Doe, Germany"

infile = close

