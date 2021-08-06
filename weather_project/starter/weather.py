import csv
from datetime import date, datetime

DEGREE_SYBMOL = u"\N{DEGREE SIGN}C"


def format_temperature(temp):
    """Takes a temperature and returns it in string format with the degrees
        and celcius symbols.

    Args:
        temp: A string representing a temperature.
    Returns:
        A string contain the temperature and "degrees celcius."
    """
    return f"{temp}{DEGREE_SYBMOL}"

    #not writing print, just doing 'return' alot. If you want to print must put outside the function (not indented)


def convert_date(iso_string):
    """Converts and ISO formatted date into a human readable format.

    Args:
        iso_string: An ISO date string..
    Returns:
        A date formatted like: Weekday Date Month Year e.g. Tuesday 06 July 2021
    """
    #have to define the iso string , so 'strip' the string to by putting in the codes from web
    weekday = datetime.strptime(iso_string, "%Y-%m-%dt%H:%M:%S%z").strftime("%A")
    day = datetime.strptime(iso_string, "%Y-%m-%dt%H:%M:%S%z") .strftime("%d")
    month = datetime.strptime(iso_string, "%Y-%m-%dt%H:%M:%S%z") .strftime("%B")
    year = datetime.strptime (iso_string, "%Y-%m-%dt%H:%M:%S%z") .strftime("%Y")
    return (f"{weekday} {day} {month} {year}")
#descriptor 'strftime' for 'datetime.date' objects doesn't apply to a 'str' object??
#make sure indenting to keep 'in the function'





def convert_f_to_c(temp_in_farenheit):
    """Converts an temperature from farenheit to celcius.

    Args:
        temp_in_farenheit: float representing a temperature.
    Returns:
        A float representing a temperature in degrees celcius, rounded to 1dp.
    """

    Celsius = round((float(temp_in_farenheit) - 32)*5/9,1)
    return Celsius



def calculate_mean(weather_data):
    """Calculates the mean value from a list of numbers.

    Args:
        weather_data: a list of numbers.
    Returns:
        A float representing the mean value.
    """
    total_v = 0
    for total in weather_data:
        total_v += float(total)

    mean_weather_data = total_v/len(weather_data)
    return mean_weather_data


def load_data_from_csv(csv_file):
    """Reads a csv file and stores the data in a list.

    Args:
        csv_file: a string representing the file path to a csv file.
    Returns:
        A list of lists, where each sublist is a (non-empty) line in the csv file.
    """
    lists = []
    with open(csv_file) as csv_file:
        reader = csv.reader(csv_file, delimiter = ",")    
    for reading, row in enumerate(reader):
        if reading != 0 and len(row) != 0:
            lists.append([row[0],int(row[1]), int(row[2])])
        return(lists)


def find_min(weather_data):
    """Calculates the minimum value in a list of numbers.

    Args:
        weather_data: A list of numbers.
    Returns:
        The minium value and it's position in the list.
    """
    minimum = min(weather_data)
    min_index = weather_data.index (minimum)
    return (f"({minimum}, {min_index})")


def find_max(weather_data):
    """Calculates the maximum value in a list of numbers.

    Args:
        weather_data: A list of numbers.
    Returns:
        The maximum value and it's position in the list.
    """
    if len(weather_data) == 0:
        return()
    for i in range(0,len(weather_data)):
        max = round(float(max(weather_data)),1)
        max1 = weather_data.reverse()
        max1 = len(weather_data) - weather_data.index(max(weather_data)) -1
        return(max, max1)


def generate_summary(weather_data):
    """Outputs a summary for the given weather data.

    Args:
        weather_data: A list of lists, where each sublist represents a day of weather data.
    Returns:
        A string containing the summary information.
    """
    day = 0

    for rows in weather_data:
        if len(rows) != 0:
            day = day + 1


    a = list(weather_data[1])
    b = convert_f_to_c(a)
    c = list(weather_data[2])
    d = convert_f_to_c(c)
    e = list(weather_data[0])
    f = convert_date(e)
    g = min(a)
    h = max(c)
    #return (b, d, f, g, h)
    
    summary = (f"The lowest temperature will be {generate_summary[0]}°C, and will occur on {generate_summary()}")
    summary = (f"The highest temperature will be {generate_summary[1]}°C, and will occur on {generate_summary[2]}")
    summary =  (f"The average low this week is {generate_summary[3]}°C")
    summary = (f"The average high this week is {generate_summary[4]}°C")
    
    return (summary)


#referencing above functions, check expected outputs
#make sure outputting for all of the exmpales, so consider variable in number of days

def generate_daily_summary(weather_data):
    """Outputs a daily summary for the given weather data.

    Args:
        weather_data: A list of lists, where each sublist represents a day of weather data.
    Returns:
        A string containing the summary information.
    """
    summary = ""
    for rows in weather_data:
       summary += f"{convert_date(rows[0])} \n"
       summary += f" Minimum Temperature: {format_temperature(convert_f_to_c(int(rows[1])))} \n"
    summary += f" Maximum Temperature: {format_temperature(convert_f_to_c(int(rows[2])))}  \n"
    summary += f"\n"
    return summary 
   
#referencing above functions, check expected outputs

#Weather_data = [
#['date','min','max'],
#['2020-06-19T07:00:00+08:00',47,46],
#['2020-06-20T07:00:00+08:00',51,67],
#['2020-06-21T07:00:00+08:00',58,72],
#['2020-06-22T07:00:00+08:00',59,71],
#['2020-06-23T07:00:00+08:00',52,71],
#['2020-06-24T07:00:00+08:00',52,67],
#['2020-06-25T07:00:00+08:00',48,66],
#['2020-06-26T07:00:00+08:00',53,66]
#]

#iso_string = '2020-06-19T07:00:00+08:00'


#print (convert_date(iso_string))
#print(Weather_data)
#can use to check all functions, make sure to comment or delet before running/ submitting tents
#list of min or max temp, sometimes string so make sure int or float
#