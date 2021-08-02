import csv
from datetime import datetime

DEGREE_SYBMOL = u"\N{DEGREE SIGN}C"


def format_temperature(temp):
    """Takes a temperature and returns it in string format with the degrees
        and celcius symbols.

    Args:
        temp: A string representing a temperature.
    Returns:
        A string contain the temperature and "degrees celcius."
    """
    temp=str(temp)
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
    weekday = datetime.strftime 
    day = datetime.strftime
    month = datetime.strftime
    year = datetime.strftime 
    return (f"{weekday} {day} {month} {year}")

#make sure indenting to keep 'in the function'





def convert_f_to_c(temp_in_farenheit):
    """Converts an temperature from farenheit to celcius.

    Args:
        temp_in_farenheit: float representing a temperature.
    Returns:
        A float representing a temperature in degrees celcius, rounded to 1dp.
    """

    Celsius = (float(temp_in_farenheit) - 32) * 5.0/9.0 
    return Celsius



def calculate_mean(weather_data):
    """Calculates the mean value from a list of numbers.

    Args:
        weather_data: a list of numbers.
    Returns:
        A float representing the mean value.
    """

    #mean_weather_data = sum(weather_data) / len(weather_data)
    pass


def load_data_from_csv(csv_file):
    """Reads a csv file and stores the data in a list.

    Args:
        csv_file: a string representing the file path to a csv file.
    Returns:
        A list of lists, where each sublist is a (non-empty) line in the csv file.
    """
    pass

#make sure reading arg return and understanding what you need to do, dont jump ahead/ overcomplicate
#when doing loop, if length of row is 0 than dont consider

def find_min(weather_data):
    """Calculates the minimum value in a list of numbers.

    Args:
        weather_data: A list of numbers.
    Returns:
        The minium value and it's position in the list.
    """
    pass


def find_max(weather_data):
    """Calculates the maximum value in a list of numbers.

    Args:
        weather_data: A list of numbers.
    Returns:
        The maximum value and it's position in the list.
    """
    pass


def generate_summary(weather_data):
    """Outputs a summary for the given weather data.

    Args:
        weather_data: A list of lists, where each sublist represents a day of weather data.
    Returns:
        A string containing the summary information.
    """
    pass
#referencing above functions, check expected outputs
#make sure outputting for all of the exmpales, so consider variable in number of days

def generate_daily_summary(weather_data):
    """Outputs a daily summary for the given weather data.

    Args:
        weather_data: A list of lists, where each sublist represents a day of weather data.
    Returns:
        A string containing the summary information.
    """
    pass
#referencing above functions, check expected outputs

Weather_data = [
['date','min','max'],
['2020-06-19T07:00:00+08:00',47,46],
['2020-06-20T07:00:00+08:00',51,67],
['2020-06-21T07:00:00+08:00',58,72],
['2020-06-22T07:00:00+08:00',59,71],
['2020-06-23T07:00:00+08:00',52,71],
['2020-06-24T07:00:00+08:00',52,67],
['2020-06-25T07:00:00+08:00',48,66],
['2020-06-26T07:00:00+08:00',53,66]
]

iso_string = '2020-06-19T07:00:00+08:00'
print (convert_date(iso_string))
#print(Weather_data)
#can use to check all functions, make sure to comment or delet before running/ submitting tents
#list of min or max temp, sometimes string so make sure int or float
#