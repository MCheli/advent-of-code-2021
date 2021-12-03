# Day 2 - Submarine

import day2data

d = day2data.data
d_values = d.splitlines()

depth = 0
position = 0
aim = 0

for index, movement in enumerate(d_values):
  mov_array = movement.split( )
  if mov_array[0] == "forward":
    print(f"moved forward by {mov_array[1]}")
    position += int(mov_array[1])
    depth += aim * int(mov_array[1])
  elif mov_array[0] == "up":
    print(f"moved up by {mov_array[1]}")
    aim -= int(mov_array[1])
  elif mov_array[0] == "down":
    print(f"moved up by {mov_array[1]}")
    aim += int(mov_array[1])
  else:
    print("No idea what happened here")

multiplied_position = depth * position

print(f"Depth of {depth} and a position of {position} for a multiple position of {multiplied_position}")