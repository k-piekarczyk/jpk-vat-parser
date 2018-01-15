from vars import headers

output = [headers]
info = []
income = []
spendings = []
# Parse info file
try:
    infoFile = open('input/info.csv', 'r')
    infoFileSTR = infoFile.readline()
    if infoFileSTR.endswith('\n'):
        line = infoFileSTR[:-1]
    info = infoFileSTR.split(';')
except FileNotFoundError:
    print("Nie znaleziono pliku 'info.csv'. Upewnij się że znajduje się on w folderze input.")

# Parse income file
try:
    incomeFile = open('input/przychod.csv', 'r')
    for line in incomeFile:
        if line.endswith('\n'):
            line = line[:-1]
        income.append(line.split(';'))
    incomeFile.close()
except FileNotFoundError:
    print("Nie znaleziono pliku 'przychod.csv'. Upewnij się że znajduje się on w folderze input.")

# Parse spendings file
try:
    spendingsFile = open('input/wydatki.csv', 'r')
    for line in spendingsFile:
        if line.endswith('\n'):
            line = line[:-1]
        spendings.append(line.split(';'))
    spendingsFile.close()
except FileNotFoundError:
    print("Nie znaleziono pliku 'wydatki.csv'. Upewnij się że znajduje się on w folderze input.")

# Add first info line to output array
tmp = []
for i in range(len(headers)):
    if i < 10:
        tmp.append(info[i])
    else:
        tmp.append('')
output.append(tmp)

# Add second info line to output array
tmp = []
for i in range(len(headers)):
    if i < 10 or i >= 13:
        tmp.append('')
    elif i < 13:
        tmp.append(info[i])
output.append(tmp)

# Add third info line to output array
tmp = []
for i in range(len(headers)):
    if i < 13 or i >= 23:
        tmp.append('')
    elif i < 23:
        tmp.append(info[i])
output.append(tmp)

# Add income to output array
incomeTaxSum = 0
for line in income:
    tmp = []
    # Change '23,12' -> '23.12' for proper str to float formatting
    incomeTaxLIST = list(line[18])
    incomeTaxLIST[line[18].find(',')] = '.'
    incomeTaxSum += float(''.join(incomeTaxLIST))

    for i in range(len(headers)):
        if i < 23:
            tmp.append('')
        elif i < 61:
            tmp.append(line[i - 23])
        else:
            tmp.append('')
    output.append(tmp)
incomeEntries = len(income)
incomeTaxSumSTR = "%.2f" % incomeTaxSum

incomeTaxSumLIST = list(incomeTaxSumSTR)
incomeTaxSumLIST[incomeTaxSumSTR.find('.')] = ','
incomeTaxSumSTR = ''.join(incomeTaxSumLIST)

output.append(['' for whatever in range(len(headers))])  # Empty line -- for some reason '...' doesn't work here
incomeINSERT = ['' for whatever in range(len(headers))]
incomeINSERT[61] = str(incomeEntries)
incomeINSERT[62] = incomeTaxSumSTR
output.append(incomeINSERT)  # Adds number of income entries and cumulative income tax

# Add spendings to output array
spendingsTaxSum = 0
for line in spendings:
    tmp = []
    # Change '23,12' -> '23.12' for proper str to float formatting
    spendingsTaxLIST = list(line[11])
    spendingsTaxLIST[line[11].find(',')] = '.'
    spendingsTaxSum += float(''.join(spendingsTaxLIST))

    for i in range(len(headers)):
        if i < 63:
            tmp.append('')
        elif i < 79:
            tmp.append(line[i - 63])
        else:
            tmp.append('')
    output.append(tmp)
spendingsEntries = len(spendings)
spendingsTaxSumSTR = "%.2f" % spendingsTaxSum

spendingsTaxSumLIST = list(spendingsTaxSumSTR)
spendingsTaxSumLIST[spendingsTaxSumSTR.find('.')] = ','
spendingsTaxSumSTR = ''.join(spendingsTaxSumLIST)

spendingsINSERT = ['' for whatever in range(len(headers))]
spendingsINSERT[79] = str(spendingsEntries)
spendingsINSERT[80] = spendingsTaxSumSTR
output.append(spendingsINSERT)  # Adds number of income entries and cumulative spending tax

try:
    # Clear file before saving to avoid duplication (if it exist)
    cf = open('output/output.csv', 'w')
    cf.write('')
    cf.close()
    of = open('output/output.csv', 'a')
    for line in output:
        of.write(';'.join(line))
        of.write('\n')
    of.close()
except PermissionError:
    print("Plik 'output.csv' jest otwarty w innym programie. Zamknij i spróbuj jeszcze raz.")
