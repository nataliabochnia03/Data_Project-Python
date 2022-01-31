"""
This module is responsible for visualising the data using Matplotlib.
"""

"""
Task 22 - 24: Write suitable functions to visualise the data as follows:

- Display the number of confirmed cases per country/region using a pie chart
- Display the top 5 countries for deaths using a bar chart
- Display a suitable (animated) visualisation to show how the number of confirmed cases, deaths and recovery change over
time. This could focus on a specific country or countries.

Each function should visualise the data using Matplotlib.
"""
import matplotlib.pyplot as plt
from matplotlib import animation
import numpy as np

from matplotlib import pyplot as plt
from matplotlib.animation import FuncAnimation, writers
import numpy as np
from process import *
from tui import *


# TODO: Your code here
def pi_chart_conf_cases(data):
    countries = []
    cases_count = []
    for i in data:
        countries.append(i[0])
        cases_count.append(i[1])
    # Creating plot
    fig = plt.figure(figsize = (10,7))
    #autopct enables to display the percent value using Python string formatting.
    plt.pie(cases_count, lables = countries  ,autopct = '%1.1f%%')
    plt.title('Number of Confirmed cases per country/region')

    plt.legend()
    #show plt
    plt.show()

def pi_chart_top_5_death_countries(data):
    data = sorted(data,key =lambda l:l[3] , reverse=True)
    #print(data)
    countries = []
    cases_count = []
    c= 0
    for i in data:
        countries.append(i[0])
        cases_count.append(i[3])
        c+=1
        if c == 5:
            break
    # Creating plot
    plt.figure(figsize = (10,7))
    # plt.legend()

    plt.pie(cases_count, lables = countries, autopct = '%1.1f%%')
    # plt.axis('equal')
    plt.legend()

    # show plt
    plt.show()





def animate(i, dates, data):
    global anim
    # print(i)
    if i < len(dates):
        # i = i%len(dates)

        result = list(data[dates[i]])
        #print(i, dates[i],result , )

        plt.bar([f"Confirmed", "Death", "Recovered"], result, color=['yellow','red','green'])
        plt.title(f"Cases in {dates[i]} [C:{result[0]} | D:{result[1]} | R:{result[2]}", color=("blue"))
        if i >0 :
            plt.pause(0.5)

    else:
        anim.event_source.stop()


def visualization(data, name = None):
    if name == None:
        error("No valid Name entered")

        return

    all_unique_countries = []
    all_dates = []
    for d in data:
        if d[3] not in all_unique_countries:
            all_unique_countries.append(d[3])
        if d[1] not in all_dates:
            all_dates.append(d[1])

    result = {}  # stores results by dates
    if name == 'all':
        print('printing all result')
        pass

    else:
        if name not in all_unique_countries:
            error("Not Found in the Record For Any Country")

            return
        else:
            data = get_records_grouped_by_country_region(data)
            temp = []
            for d in data:
                if d[3] == name:
                    temp.append(d)
            data = temp
            pass

    for date in all_dates:
        result[date] = get_total_of_records(get_records_by_observation_dates(data, date))

    # print(result)

    dates = list(result.keys())
    values = list(result.values())
    max_val = 0
    for v in values:
        max_val = max(v)

    fig = plt.figure(figsize=(8, 6))
    axes = fig.add_subplot(1, 1, 1)
    axes.set_ylim(0, max_val + 100)
    fig.text()
    plt.style.use("seaborn")


    if name == 'all':
        plt.title("Overall Results of Cases", color=("blue"))
    else:
        plt.title(f"Cases of {name}", color=("blue"))
    # print(len(dates))
    # print(len(result))
    global anim

    anim = FuncAnimation(fig, animate, fargs=(dates, result,), interval=len(dates), repeat=False)

    plt.show()
