import requests
import csv

data = requests.get("http://api.open-notify.org/astros.json")
items = data.json()['people']


with open('people.csv', 'w') as f:
    writer = csv.DictWriter(f, fieldnames=['name', 'craft'])
    writer.writeheader()
    for i in items:
        writer.writerow(i)

craft_sorted = {}
for i in items:
    craft_name = i['craft']
    if craft_name not in craft_sorted:
        craft_sorted[craft_name] = []
    craft_sorted[craft_name].append(i)
for craft in craft_sorted:
    with open(str(craft)+'.csv', 'w') as f:
        writer = csv.DictWriter(f, fieldnames=['name', 'craft'])
        writer.writeheader()
        for line in craft_sorted[craft]:
            writer.writerow(line)
xdsfsdf