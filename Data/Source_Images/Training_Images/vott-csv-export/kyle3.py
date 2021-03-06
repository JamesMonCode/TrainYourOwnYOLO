import csv
f = open('allAnnotations.csv')
write_to = open("ta_train.txt", 'w')
reader = csv.reader(f, delimiter=';')
labels = set()
set_path = '/Users/kylezeng/TrainYourOwnYolo/Data/Source_Images/Training_Images/vott-csv-export/'
for row in reader:
    #row = row[:-5]
    if row[1] != 'Annotation tag':
        labels.add(row[1])
#print(labels)
labels = sorted(labels)
#print(labels)
    
traffic_dict = dict(zip(labels, range(len(labels))))
#print(traffic_dict)

f.seek(0)
reader = csv.reader(f, delimiter=';')

for row in reader:
    row = row[:-5]
    if row[1] != 'Annotation tag' and not row[0].startswith('a'):
        row[1] = traffic_dict[row[1]]
        row[0] = set_path + row[0]
        row.append(str(row.pop(1)))
        row = ','.join(row)
        print(row)
        write_to.write(row+'\n')
        
write_to.close()
f.close()
