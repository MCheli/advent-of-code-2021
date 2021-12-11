import statistics
import day3data
import numpy as np

d = day3data.data

d_values = d.splitlines()

d_array = []

for i in range(0, len(d_values[0])):
  d_array.append([])

for value in d_values:
  value_char_array = list(value)
  for index, char in enumerate(value_char_array):
    d_array[index].append(int(char))

gamma = []
epsilon = []

for index, value in enumerate(d_array):
  gamma.append(statistics.mode(value))
  epsilon.append(0 if gamma[index] == 1 else 1)

# print(gamma)
gamma_string = ''.join(str(x) for x in gamma)
epsilon_string = ''.join(str(x) for x in epsilon)
print(f"Gamma: {gamma_string} - Epsilon: {epsilon_string}")

power_consumption = int(gamma_string, 2) * int(epsilon_string, 2)

print(f"Power Consumption = {power_consumption}")

d_2d = []
for value in d_values:
  d_2d.append(list(map(int, value)))

arr = np.array(d_2d)

for i in range(0, len(d_values[0])):
  average = statistics.mean(list(map(float, arr[:, i])))
  if(average == 0.5):
    most_common = 1
  elif(average > 0.5):
    most_common = 1
  elif(average < 0.5):
    most_common = 0
  arr = arr[arr[:, i] == most_common]
oxygen_rating = arr

arr = np.array(d_2d)

for i in range(0, len(d_values[0])):
  average = statistics.mean(list(map(float, arr[:, i])))
  if(average == 0.5):
    most_common = 1
  elif(average > 0.5):
    most_common = 1
  elif(average < 0.5):
    most_common = 0
  arr = arr[arr[:, i] == (0 if most_common == 1 else 1)]
  numrows, numcolumns = arr.shape
  if(numrows == 1):
    break
c02_rating = arr

print(f"oxygen_rating: {oxygen_rating} - c02_rating: {c02_rating}")

oxygen_string = ''.join(str(x) for x in list(oxygen_rating[0, :]))
c02_string = ''.join(str(x) for x in list(c02_rating[0, :]))

oxygen_value = int(oxygen_string, 2)
c02_value = int(c02_string, 2)
print(f"oxygen_value: {oxygen_value} - c02_value: {c02_value}")
print(f"Final Answer: {oxygen_value * c02_value}")