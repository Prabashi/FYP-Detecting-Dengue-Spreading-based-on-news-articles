import re

locations=["Meethotamulla","Colombo", "kandy","Anuradhapura","Galle","Matara","Ratmalana","Dangolla","Badulla","Elpitiya","Beliatte","Hatton","Marakolliya","Gampola","Kalubowila","Puttalam",]

import pandas as pd
import csv

df = pd.read_csv('TestDengueContent.csv')
df = df.fillna("")
print(df.shape)

for index, row in df.iterrows():
        for line in (row):
            i=0
            while i<len(locations):
                if locations[i] in line:
                    print(locations[i])
                i+=1


                