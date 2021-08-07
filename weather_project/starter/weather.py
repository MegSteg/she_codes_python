import csv
from datetime import date, datetime

DEGREE_SYBMOL = u"\N{DEGREE SIGN}C"

#Camila is an absolute ANGEL and Randall was wonderful, big shout-out to them for helping me through!

def format_temperature(temp):
   
    return f"{temp}{DEGREE_SYBMOL}"

def convert_date(iso_string):
  
    date = datetime.strptime(iso_string, "%Y-%m-%dt%H:%M:%S%z")
    new_date = date.strftime("%A %d %B %Y")
    return new_date


def convert_f_to_c(temp_in_farenheit):
  

    Celsius = round((float(temp_in_farenheit) - 32)*5/9,1)
    return Celsius

def calculate_mean(weather_data):
 
    total_v = 0
    for total in weather_data:
        total_v += float(total)

    mean_weather_data = total_v/len(weather_data)
    return mean_weather_data


def load_data_from_csv(csv_file):
  
    lists = []
    with open(csv_file, mode ="r", encoding = "utf-8") as csv_file:
        reader = csv.reader(csv_file, delimiter = ",")    
        next(reader)
        for row in reader:
            if len(row) != 0 :
                lists.append([row[0],int(row[1]), int(row[2])])
    return(lists)


def find_min(weather_data):
    if len(weather_data) == 0 :
        return()
    minimum = float(weather_data[0])
    min_position = 0
    for index, num in enumerate(weather_data):
        if float(num) <= minimum:
            minimum = float(num)
            min_position= index

    return (minimum, min_position)


def find_max(weather_data):
    if len(weather_data) == 0 :
        return()
    maximum = float(weather_data[0])
    max_position = 0
    for index, num in enumerate(weather_data):
        if float(num) >= maximum:
            maximum = float(num)
            max_position= index
    return (maximum, max_position) #fix names
   

def generate_summary(weather_data):
    day = 0
    all_min =[]
    all_max =[]
    for rows in weather_data:
        if len(rows) != 0:
            day += 1
            all_min.append(rows[1])
            all_max.append(rows[2])
    min_temp, min_position = find_min(all_min)
    minimum_c = convert_f_to_c(min_temp)
    min_temp = format_temperature(minimum_c)
    min_date = convert_date(weather_data[min_position][0])

    maximum, max_position = find_max(all_max)
    maximum_c = convert_f_to_c(maximum)
    max_temp = format_temperature(maximum_c)
    max_date = convert_date(weather_data[max_position][0])
    av_low = calculate_mean(all_min)
    av_low_c = convert_f_to_c(av_low)
    av_high = calculate_mean(all_max)
    av_high_c = convert_f_to_c(av_high)

    summary = ""
    summary += f"{day} Day Overview\n"
    summary += f"  The lowest temperature will be {min_temp}, and will occur on {min_date}.\n"
    summary += f"  The highest temperature will be {max_temp}, and will occur on {max_date}.\n"
    summary += f"  The average low this week is {format_temperature(av_low_c)}.\n"
    summary += f"  The average high this week is {format_temperature(av_high_c)}.\n"
    
    return summary


def generate_daily_summary(weather_data):

    summary = ""
    for rows in weather_data:
        if len(rows) != 0:
            summary += f"---- {convert_date(rows[0])} ----\n"
            summary += f"  Minimum Temperature: {format_temperature(convert_f_to_c(int(rows[1])))}\n"
            summary += f"  Maximum Temperature: {format_temperature(convert_f_to_c(int(rows[2])))}\n"
            summary += f"\n"
    return summary 
   