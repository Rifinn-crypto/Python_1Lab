import json
import re
import requests
import csv


URL = " https://www.cbr-xml-daily.ru/archive/2022/10/22/daily_json.js"
HEADER = ["Day", "Exchange rate"]
write_to_file = "C:/Users/esh20/Desktop/dataset.csv"

with open(write_to_file, "w") as file:
    dw = csv.DictWriter(file, delimiter=',',
                        fieldnames=HEADER)
    dw.writeheader()