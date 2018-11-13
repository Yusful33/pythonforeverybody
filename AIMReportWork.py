AIMReport = open('AIM_Report.txt')
AIMReport.rstrip()
x = 0
try:
    for line in AIMReport:
        x = x + 1
        print(x)
except:
    print('No lines in this workbook')
