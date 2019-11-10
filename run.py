from gitcreeps import get_clean_data, to_json_file, merge_names, days, hour, date
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

clean_data = get_clean_data('log.txt')
to_json_file(clean_data, 'log.json')

names = ["Abdur-Rahmaan Janhangeer", "Abdur-RahmaanJ", "arj"]
merge_names(clean_data, names, default="Abdur-RahmaanJ")

mydata = clean_data["Abdur-RahmaanJ"]
arj_day = []
arj_time = []
arj_date = []
arj_hour = []

for d in mydata:
    times = mydata[d]['times']
    for t in times:
        arj_day.append(d)
        arj_hour.append(hour(t))
        arj_date.append(date(t))

#print(arj_date, arj_days, arj_time)
df = pd.DataFrame({
    'day':arj_day,
    'hour':arj_hour,
    'date':arj_date
})

ax = plt.gca()
df.plot(kind='line', x='date', y='hour',ax=ax)
plt.show()
