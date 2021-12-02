# Day 1 - Sonar

import day1data

d = day1data.data
d_values = d.splitlines()

num_increase = 0

for index, measurement in enumerate(d_values):
  if(index>0):
    if(measurement > d_values[index-1]):
      num_increase += 1

print(f"Num Increases = {num_increase}")