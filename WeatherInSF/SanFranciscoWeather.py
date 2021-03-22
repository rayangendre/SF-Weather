import csv
import matplotlib.pyplot as plt
from datetime import datetime
'''
The purpose of this program is to read a csv file of San Francisco Weather from the NOAA
The data is then represented in a graph using the pyplot class from matplotlib
'''

filename = 'SanFranciscoWeather-01-01-2019-12-31-2019.csv'

with open(filename) as file:
    #set up a reader for a csv and skip the header line
    reader = csv.reader(file)
    header_row = next(reader)

    dates, highs, lows, = [], [], []

    for row in reader:
        #format date into a datetime object
        current_date = datetime.strptime(row[2], "%Y-%m-%d")

        #append all dates into their specific list
        dates.append(current_date)
        highs.append(int(row[3]))
        lows.append(int(row[4]))


    #plot the temperatures
    plt.style.use('seaborn')
    fig, ax = plt.subplots()
    ax.plot(dates, highs, c='red', alpha=0.5)
    ax.plot(dates, lows, c='blue', alpha=0.5)
    plt.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1)

    #Format the plot
    ax.set_title("Daily high and low temperatures - 2019", fontsize=24)
    ax.set_xlabel('Day', fontsize=16)
    fig.autofmt_xdate()
    ax.set_ylabel('Temperature (F)', fontsize=16)
    ax.tick_params(axis='both', which='major', labelsize=10)

    #draw graph
    plt.show()