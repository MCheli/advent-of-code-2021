import statistics
import day3data

d = day3data.data

d_values = d.splitlines()

d_array = []

for i in range(0, len(d_values[0])):
  d_array.append([])

for value in d_values:
  value_char_array = list(value)
  for index, char in enumerate(value_char_array):
    d_array[index].append(int(char))
    print(index)

gamma = []
epsilon = []

for index, value in enumerate(d_array):
  gamma.append(statistics.mode(value))
  epsilon.append(0 if gamma[index] == 1 else 1)

print(gamma)
gamma_string = ''.join(str(x) for x in gamma)
epsilon_string = ''.join(str(x) for x in epsilon)

power_consumption = int(gamma_string, 2) * int(epsilon_string, 2)

print(f"Power Consumption = {power_consumption}")
