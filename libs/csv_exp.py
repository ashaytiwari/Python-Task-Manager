import csv

with open("files/weather.csv", 'r') as file:
    data = list(csv.reader(file))

city = input("Enter a city:").strip()

temperature = 0

for item in data[1:]:
    if item[0] == city:
        temperature = item[1]
        break
    else:
        temperature = 0

if temperature == 0:
    print('Data not available for entered city')
else:
    print(f"Temperature of {city} is {temperature} degree celsiusU")
