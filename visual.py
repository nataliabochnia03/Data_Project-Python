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

def pi_chart_top_5_death_countries(data):
    #reverse method doesen't return any value and it updates the existing list!
    #lambda is anonymous function(that is defined without a name) and can take any number of arguments, but can only have one expression!
    data = sorted(data, key =lambda l:l[3], reverse=True)
    countries = []
    cases_count = []
    c = 0
    for i in data:
        countries.append(i[0])
        cases_count.append(i[3])
        c+=1
        if c == 5:
            break
        #creating plot
        plt.figure(figsize = (10,7))
        #plt.legend()
        plt.pie(cases_count, lables = countries, autopct = "%1.1f%%")
        #plt.axis("equal")
        #show plt
        plt.show()

    def visualization(data, name = None):
        if name == None:
            pass
    #     else:
    #         fig = plt.figure(figsize = (7,5))
    #         axes = fig.add_subplot(1,1,1)
    #         axes.set_ylim(0, 300)
    #         palette = ["blue", "red", "green", "darkorange", "maroon", "black"]
    #         y1, y2, y3, y4, y5, y6 = [], [], [], [], [], []
    #
    #         plt.title("Bar Chart Animation")
    #         animation = FuncAnimation(fig, animation_function, interval = 50)
    #         plt.show()
    #
    # def animation_function(i):
    #     y1 = i
    #     y2 = 5 *i
    #     y3 = 3* i
    #     y4 = 2 *i
    #     y5 = 6 * i
    #     y6 = 3 * i
    #
    #     plt.xlabel("Country")
    #     plt.ylable("GDP of Country")
    #
    #     plt.bar(["India", "China", "Germany", "USA", "Canada", "UK"], [y1, y2, y3, y4, y5, y6], color = palette)

