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

# TODO: Your code here
def pi_chart_conf_cases(data):
    countries = []
    cases_count = []
    for i in data:
        countries.append(i[0])
        cases_count.append(i[1])
    #creating plot
    fig = plt.figure(figsize = (10,7))
    #autopct enables to display the percent value using Python string formatting.
    plt.pie(cases_count, lables = countries, autopct = "%1.1f%%")
    plt.title("Number of confirmed cases per country/region")
    plt.legend()
    #show plt
    plt.show()
