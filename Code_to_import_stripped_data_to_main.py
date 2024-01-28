import csv

with open("weather_data.csv") as weather_data:
    # list_weather_data = weather_data.readlines()
    list_weather_data = csv.reader(weather_data)
    # print(f"list weather data: {list_weather_data}")
    # list weather data: <_csv.reader object at 0x0000016292285340>
    #this Object can be Looped through!

    tempuratures = []  #integers only, only temps go into this list

    # next(list_weather_data)   # Skip the header row

    for row in list_weather_data:
        # print(row)
        # if row[1].isdigit():
        #     temp = int(row[1])
        #     tempuratures.append(temp)
        if row[1] != "temp":
            tempuratures.append(int(row[1]))

    print(tempuratures)     #only integers added to list
        # print(f"temp: {temp}")

# with open("C:/Users/guber/Desktop/CoDex - Code Index - GitHub for HDD/Python/100 Days of Code - Projects Code - in PyCharm/__Learning Only Files - Only Mini-Projects here__/Day 25 Start - CSV Files and Pandas/main.py") as imported_to_main_file:
#     importing_data = imported_to_main_file.read()
#     for iteration in list_weather_data:
#         stripped_data = iteration.strip()
        # new_data_file = importing_data.replace(PLACEHOLDER, stripped_name)
        # print(new_letter)
        # print(f"Stripped data is: {stripped_data}")
        # with open("C:/Users/guber/Desktop/CoDex - Code Index - GitHub for HDD/Python/100 Days of Code - Projects Code - in PyCharm/__Learning Only Files - Only Mini-Projects here__/Day 25 Start - CSV Files and Pandas/main.py", mode="a") as completed_data:
            # print("\n")
            # completed_data.write(stripped_data)



