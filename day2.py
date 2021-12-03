# Day 2 - Submarine

import day2data

d = day2data.data
d_values = d.splitlines()

depth = 0
position = 0

for index, movement in enumerate(d_values):
  mov_array = movement.split( )
  if mov_array[0] == "forward":
    print("moved forward")
    position += int(mov_array[1])
  elif mov_array[0] == "up":
    print("moved up")
    depth -= int(mov_array[1])
  elif mov_array[0] == "down":
    print("moved up")
    depth += int(mov_array[1])
  else:
    print("No idea what happened here")

multiplied_position = depth * position

print(f"Depth of {depth} and a position of {position} for a multiple position of {multiplied_position}")