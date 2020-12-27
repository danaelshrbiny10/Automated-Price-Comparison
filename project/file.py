import json
import csv

with open("./my_json.json" , encoding='utf-8') as file:
    data = json.load(file)

full = data ["viewData"]["products"]

fname = "output.csv"

with open(fname ,'w',encoding='utf-8') as file:
    csv_file = csv.writer(file)
    csv_file.writerow(["name","url"])
    for item in full:
        csv_file.writerow([item["name"],item["url"]])    