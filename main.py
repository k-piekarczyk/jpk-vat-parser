from vars import headers

output = [headers]

incomeFile = open('input/przychod.csv', 'r')
income = []
for line in incomeFile:
    if line.endswith('\n'):
        line = line[:-1]
    income.append(line.split(';'))
incomeFile.close()

spendingsFile = open('input/wydatki.csv', 'r')
spendings = []
for line in spendingsFile:
    spendings.append(line.split(';'))
spendingsFile.close()

for line in income:
    tmp = []
    for i in range(len(headers)):
        if i < 23:
            tmp.append('')
        elif i < 61:
            tmp.append(line[i - 23])
        else:
            tmp.append('')
    output.append(tmp)

of = open('output.csv', 'a')
for line in output:
    of.write(';'.join(line))
    of.write('\n')
of.close()
