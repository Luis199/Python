import csv

with open('sample_data.csv', mode='w') as csvfile:
    csvwriter = csv.writer(csvfile)
    csvwriter.writerow(["Name", "Department", "Location"])
    csvwriter.writerow(["John Wright", "R&D", 'NYC'])
    csvwriter.writerow(["Joel Rodriguez", "Marketing", 'LA'])
    csvwriter.writerow(["Nick Wright", "Sales", 'DC'])
    