import csv

infile = open('steps.csv','r')
csvfile = csv.reader(infile, delimiter=',')
next(csvfile) # skip the headers

steps = [0]
days = [0]
current_month = 1

for record in csvfile:
    if int(record[0]) != current_month:
        current_month += 1
        steps.append(0)
        days.append(0)
    days[current_month-1] += 1
    steps[current_month-1] += int(record[1])
infile.close()


months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
outfile = open('avg_steps.csv', 'w')
outfile.write('Month,Avg_Steps\n')

for month in range(len(days)):
    avg = steps[month] / days[month]
    outfile.write(months[month] + ',' + '{:0.2f}'.format(avg) + '\n')
outfile.close()