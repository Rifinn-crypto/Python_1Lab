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
    while True:
        html_text = requests.get(URL).text
        json_pars = json.loads(html_text)
        current_day = json_pars["Date"]
        final_current_day = re.findall(r"(\d{4}\-\d{2}\-\d{2})", current_day)

        current_course = json_pars["Valute"]["USD"]["Value"]

        previous_day_url = json_pars["PreviousURL"]
        final_previous_day_url = previous_day_url.replace("//", "")
        switch_previous_day_url = "http://" + final_previous_day_url
        finish_current_day = str(final_current_day)[2:-2]
        finish_current_day = finish_current_day.replace("'", "")