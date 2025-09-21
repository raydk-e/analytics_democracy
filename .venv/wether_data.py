import csv
import pandas as pd
data_file = '/home/deepak/projects/analytics_democracy/weather_data.csv'

# with open (data_file, 'r') as file:
#     reader = csv.reader(file)
#     next(reader)
#     temp_list = []
#     for r in reader:
#         temp_list.append(int(r[2][ :2]))
#     print(temp_list)

data = pd.read_csv(data_file)
# print(data)
# print(type(data))

temp_data = data["temp"].to_list()
temp_data_num = []
for i in temp_data:
    temp_data_num.append(int(i[:2]))

print(temp_data_num)

sum_num = 0

for j in temp_data_num:
    sum_num = sum_num+j
avg_temp = sum_num/len(temp_data_num)
print(f"the average temperature is {avg_temp} degree celcius")
