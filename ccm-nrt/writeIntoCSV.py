import csv

field_names = ['a', 'b', 'c']

#initial content
with open('/your/testReport.csv','w') as f:
    f.write('appCode,testCase,testCaseDesc,status,errorDesc\n') # TRAILING NEWLINE

with open('/your/testReport.csv','a',newline='') as f:
    writer=csv.writer(f)
    writer.writerow(['ADV','TC1','Test Case Description','SUCCESS',''])
    writer.writerow(['ADV','TC2','Test Case Description','FAILED','Error Description'])


with open('/your/testReport.csv') as f:
    print(f.read())