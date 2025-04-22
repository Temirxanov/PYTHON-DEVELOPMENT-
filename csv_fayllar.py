# -------------------JSON CSV formati------------
import csv 

file = open(file='file2.csv',mode='w')
write = csv.writer(file,delimiter=';',lineterminator='\n')

write.writerow(
    [
        'Onim',
        'bahasi',
    ]
)

write.writerow(
    [
        'Qumsheker',
        15000
    ]
)

data = [
    [
        'Sari may',
        1000
    ],
    [
        'Mayanez',
        5000
    ],
    [
        'Sut',
        15000
    ],
    [
        'Yogurt',
        5000
    ]
]
write.writerows(data)
file.close()


open_file = open(file='file2.csv',mode='r')
read = csv.reader(open_file,delimiter=';',lineterminator='\n')
for i in read:
    print(i)
