
'''
This module is responsible for the overall program flow. It controls how the user interacts with the
program and how the program behaves. It uses the other modules to interact with the user, carry out
processing, and for visualising information.

Note:   any user input/output should be done using the appropriate functions in the module 'tui'
        any processing should be done using the appropriate functions in the module 'process'
        any visualisation should be done using the appropriate functions in the module 'visual'

'''

# Task 10: Import required modules
# TODO: Your code here

import csv
from tui import *
from process import *



# Task 11: Create an empty list named 'covid_records'.
# This will be used to store the data read from the source data file.
# TODO: Your code here
covid_records = []


def run():
    # Task 12: Call the function welcome of the module 'tui'.
    # This will display our welcome message when the program is executed.
    # TODO: Your code here
    tui.welcome()

    # Task 13: Load the data.
    # - Use the appropriate function in the module 'tui' to display a message to indicate that the data loading
    # operation has started.
    # - Load the data. Each line in the file should be a record in the list 'covid_records'.
    # You should appropriately handle the case where the file cannot be found or loaded.
    # - Use the appropriate functions in the module 'tui' to display a message to indicate how many records have
    # been loaded and that the data loading operation has completed.
    # TODO: Your code here
    progress("data", 0)
    file_name = "data//covid_19_data.csv"
    total_no_of_record = 0
    #try-except statemens. Used for exception handeling. If no errors are found in the try block, control flow moves to the statements after the except block.
    # If an error is found in the try block, the code moves on to the statements in the except block. Learned it on yt and W3schools and I really like this method as is very efficient.

    try:
        f = open(file_name)
        total_no_of_record = sum(1 for line in f) - 1 #titles removed!
        #print("Total Lines: ", total_no_of_record)
    except:
        #display "File Error, CSV File not Found"
        error("CSV File Not found")
        exit()
    #I used with statement because it close the file automaticly
    with open (file_name) as csv_file:
        #csv_reader = csv.reader(csv_file, end = ",")
        #csv_reader = csv.reader(csv_file.split(","))
        #Using delimiter ="," statement to parse the line as comma-delimited
        csv_reader = csv.reader(csv_file, delimiter=',')
        i = -1
        for row in csv_reader:
            # while True
            # while i > -1:
            # print(row)
            if i > -1:
            # print(row)
            # exit()
            covid_records.append(
                [int(row[0]), row[1], row[2], row[3], row[4], int(row[5]), int(row[6]), int(row[7])])
            progress('data loading', round((i / total_no_of_record) * 100, 2))
            # += operator, equivalent to: i = i + 1
            i += 1
            progress('data loading', 100)

            total_records(total_no_of_record)

        # print('l:',len(covid_records))
        # print(covid_records)
        # return

    while True:
        # Task 14: Using the appropriate function in the module 'tui', display a menu of options
        # for the different operations that can be performed on the data (menu variant 0).
        # Assign the selected option to a suitable local variable
        # TODO: Your code here
        menu0 = menu(0)

        # Task 15: Check if the user selected the option for processing data.  If so, then do the following:
        # - Use the appropriate function in the module tui to display a message to indicate that the data processing
        # operation has started.
        # - Process the data (see below).
        # - Use the appropriate function in the module tui to display a message to indicate that the data processing
        # operation has completed.
        #
        # To process the data, do the following:
        # - Use the appropriate function in the module 'tui' to display a menu of options for processing the data
        # (menu variant 1).
        # - Check what option has been selected
        #
        #   - If the user selected the option to retrieve an individual record by serial number then
        #       - Use the appropriate function in the module 'tui' to indicate that the record retrieval process
        #       has started.
        #       - Use the appropriate function in the module 'process' to retrieve the record and then appropriately
        #       display it.
        #       - Use the appropriate function in the module 'tui' to indicate that the record retrieval process has
        #       completed.
        #
        #   - If the user selected the option to retrieve (multiple) records by observation dates then
        #       - Use the appropriate function in the module 'tui' to indicate that the records retrieval
        #       process has started.
        #       - Use the appropriate function in the module 'process' to retrieve records with
        #       - Use the appropriate function in the module 'tui' to display the retrieved records.
        #       - Use the appropriate function in the module 'tui' to indicate that the records retrieval
        #       process has completed.
        #
        #   - If the user selected the option to group records by country/region then
        #       - Use the appropriate function in the module 'tui' to indicate that the grouping
        #       process has started.
        #       - Use the appropriate function in the module 'process' to group the records
        #       - Use the appropriate function in the module 'tui' to display the groupings.
        #       - Use the appropriate function in the module 'tui' to indicate that the grouping
        #       process has completed.
        #
        #   - If the user selected the option to summarise the records then
        #       - Use the appropriate function in the module 'tui' to indicate that the summary
        #       process has started.
        #       - Use the appropriate function in the module 'process' to summarise the records.
        #       - Use the appropriate function in the module 'tui' to display the summary
        #       - Use the appropriate function in the module 'tui' to indicate that the summary
        #       process has completed.
        # TODO: Your code here
        if menu0 == 1:
            # processing data :
            progress('Data Processing Operation', 0)
            menu1 = menu(1)
            # '[1] Record by Serial Number'
            if menu1 == 1:
                progress('record retrieval process', 0)
                # fun call for process.py
                display_record (get_record_by_serial_number(covid_records))
                progress('record retrieval process', 100)

            # '[2] Records by Observation Date'
            if menu1 == 2:
                progress('records retrieval process', 0)
                # fun call for process.py
                # fun call for tui.py
                display_records (get_records_by_observation_dates(covid_records))
                progress('records retrieval process', 100)

            # '[3] Group Records by Country/Region
            if menu1 == 3:
                progress('grouping process', 0)
                # fun call for process.py
                # fun call for tui.py
                display_records (get_records_grouped_by_country_region(covid_records))
                progress('grouping process', 100)

            # '[4] Summarise Records'
            if menu1 == 4:
                progress('summary process', 0)
                # fun call for process.py
                # fun call for tui.py
                display_records (get_summary_of_records(covid_records))
                progress('summary process', 100)

        # Task 21: Check if the user selected the option for visualising data.
        # If so, then do the following:
        # - Use the appropriate function in the module 'tui' to indicate that the data visualisation operation
        # has started.
        # - Visualise the data by doing the following:
        #   - call the appropriate function in the module 'tui' to determine what visualisation is to be done.
        #   - call the appropriate function in the module 'visual'
        # - Use the appropriate function in the module 'tui' to display a message to indicate that the
        # data visualisation operation has completed.
        # TODO: Your code here
        #if menu0 ==2:
        elif menu0 ==2:
            progress('data visualisation operation', 0)
            #fun call for tui.py
            #'[1] Country/Region Pie Chart', '[2] Observations Chart', '[3] Animated Summary'
            menu2 = menu(2)
            #fun call for visual.py
            if menu2 == 1:
                pi_chart_conf_cases(get_summary_of_records(covid_records))
            elif menu2 == 2:
                pi_chart_top_5_death_countries(get_summary_of_records(covid_records))
            elif menu == 3:
                menu3 = menu(3)
                #['[1]All Data', [2] Data for Specific Country/Region']

        
        # Task 25: Check if the user selected the option for exporting data.  If so, then do the following:
        # - Use the appropriate function in the module 'tui' to retrieve the type of data to be exported.
        # - Check what option has been selected
        #
        # - Use the appropriate function in the module 'tui' to indicate that the export operation has started.
        # - Export the data (see below)
        # - Use the appropriate function in the module 'tui' to indicate that the export operation has completed.
        #
        # To export the data, you should demonstrate the application of OOP principles including the concepts of
        # abstraction and inheritance.  You should create suitable classes with appropriate methods.
        # You should use these to write the records (either all or only those for a specific country/region) to a JSON file.
        # TODO: Your code here

        # Task 26: Check if the user selected the option for exiting the program.
        # If so, then break out of the loop
        # TODO: Your code here

        # Task 27: If the user selected an invalid option then use the appropriate function of the
        # module tui to display an error message
        # TODO: Your code here

        pass  # can remove


if __name__ == "__main__":
    run()
