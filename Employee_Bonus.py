import csv

infile = open('EmployeePay.csv','r')
csvfile = csv.reader(infile, delimiter=',')
next(csvfile) # skip the headers

for record in csvfile:
    employee_bonus = float(record[3]) * float(record[4])
    print(record[1], record[2], '{:0.2f}'.format(employee_bonus))
    