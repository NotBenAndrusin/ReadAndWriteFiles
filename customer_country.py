import csv

infile = open('customers.csv','r')
csvfile = csv.reader(infile, delimiter=',')
next(csvfile) # skip the headers

customers = []
for record in csvfile:
    print_customers = [record[1],record[2],record[4]]
    customers.append(print_customers)
infile.close()

outfile = open('customer_country.csv', 'w')
outfile.write('FirstName,LastName,Country\n')
for customer in customers:
    outfile.write(customer[0] + ',' + customer[1] + ',' + customer[2] + '\n')
outfile.close()