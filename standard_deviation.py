import csv
import math

with open('data.csv', newline='') as f:
    reader = csv.reader(f)
    file_data = list(reader)
data = file_data[0]
squared_list = []

def mean(data):
    n = len(data)
    total = 0
    for x in data:
        total += int(x)
    mean = total/n
    # print(mean)
    return mean

for number in data:
    a = float(number) - mean(data)
    a = a**2
    squared_list.append(a)

sum = 0
for i in squared_list:
    sum = sum + i

result = sum/(len(data)-1)
std_deviation = math.sqrt(result)

print(f"The standard deviation is {std_deviation:.2f}")