# CSV
import csv

with open('testfile.csv', 'w', newline='') as f:
    a = csv.writer(f, delimiter=',')
    a.writerow(range(10))

with open('testfile.csv', 'a', newline='') as f:
    a = csv.writer(f, delimiter=',')
    for i in range(10):
        a.writerow([i])

with open('testfile.csv', newline='') as f:
    a = csv.reader(f)
    for row in a:
        print(row)

with open('pets.csv', 'w', newline='') as f:
    fieldnames = ['animal_type', 'pet_name']
    a = csv.DictWriter(f, fieldnames=fieldnames)
    a.writeheader()
    a.writerow({'animal_type': 'Cat', 'pet_name': 'Sniffles'})
    a.writerow({'animal_type': 'Dog', 'pet_name': 'Sir Barks-a-lot'})
    a.writerow({'animal_type': 'Turtle', 'pet_name': 'Crush'})

with open('pets.csv', newline='') as f:
    a = csv.DictReader(f)
    print('Pet Names')
    for row in a:
        print(row['animal_type'], '-', row['pet_name'])
