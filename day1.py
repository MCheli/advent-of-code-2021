# Day 1 - Sonar

import day1data

d = day1data.data
d_values = d.splitlines()

d_values = list(map(int, d_values))

num_increase = 0

for index, measurement in enumerate(d_values):
  if(index > 0):
    if(measurement > d_values[index-1]):
      num_increase += 1

print(f"Part 1 Answer - Num Increases = {num_increase}")

sliding_num_increase = 0

for index, measurement in enumerate(d_values):
  if(index > 1) and (index < len(d_values)-1 ):
    print(f"Current Window - Value 1 {d_values[index-1]} Value 2 {d_values[index]} Value 3 {d_values[index+1]}")

    current_window_sum = d_values[index-1] + d_values[index] + d_values[index+1]
    print(current_window_sum)

    print(f"Previous Window - Value 1 {d_values[index-2]} Value 2 {d_values[index - 1]} Value 3 {d_values[index]}")

    previous_window_sum = d_values[index-2] + d_values[index-1] + d_values[index]
    print(previous_window_sum)

    if(current_window_sum>previous_window_sum):
      print("Greater!")
      sliding_num_increase += 1

print(f"Part 2 Answer - Num Increases = {sliding_num_increase}")