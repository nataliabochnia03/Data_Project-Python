"""
This module is responsible for processing the data.  Each function in this module will take a list of records,
process it and return the desired result.
"""

"""
Task 16 - 20: Write suitable functions to process the data.

Each of the functions below should follow the pattern:
- Take a list of records (where each record is a list of data values) as a parameter.
- Process the list of records appropriately.  You may use the module 'tui' to retrieve any additional information 
required from the user to complete the processing.
- Return a suitable result

The required functions are as follows:
- Retrieve the total number of records that have been loaded.
- Retrieve a record with the serial number as specified by the user.
- Retrieve the records for the observation dates as specified by the user.
- Retrieve all of the records grouped by the country/region.
- Retrieve a summary of all of the records. This should include the following information for each country/region:
    - the total number of confirmed cases
    - the total number of deaths
    - the total number of recoveries

 
"""
from tui import *
from numpy import reciprocal

# TODO: Your code here
# functions
# 01
def get_total_number_of_records(list_of_records):
    return len(list_of_records)
# 02
def get_record_by_serial_number(list_of_records):
    sn = None
    while not sn:
        sn = serial_number()

    for record in list_of_records:
        if int(record[0]) == sn:
            break
        #print(record)
        return record
# 03
def get_records_by_observation_dates(list_of_records, date = None):
    #date = None
    result = []
    while not date:
        date = observation_dates()
    for record in list_of_records:
        if record[1].strip() in date:
            result.append(record)
    return result
# 4
# def key_fun
def get_records_grouped_by_country_region(list_of_records):
    return sorted(list_of_records, key=lambda l:l[3])


def get_summary_of_records(list_of_records):
    places_data = {}
    countries = []
    for data in list_of_records:
        if (data[2], data[3]) not in places_data.keys():
            places_data[(data[2], data[3])] = {'total_conf_cases': 0, 'total_deaths': 0, 'total_recoveries': 0}
        if data[3] not in countries:
            countries.append(data[3])
        places_data[(data[2], data[3])]['total_conf_cases'] = max(places_data[(data[2], data[3])]['total_conf_cases'],data[5])
        places_data[(data[2], data[3])]['total_deaths'] = max(places_data[(data[2], data[3])]['total_deaths'], data[6])
        places_data[(data[2], data[3])]['total_recoveries'] = max(places_data[(data[2], data[3])]['total_recoveries'],data[7])

    # print(places_data)
    result = {}
    # result.append(['','Total Confirm Cases','Total Deaths','Total Recoveries'])
    for k, v in places_data.items():
        if k[1] not in result.keys():
            result[k[1]] = {'total_conf_cases': 0, 'total_deaths': 0, 'total_recoveries': 0}
        result[k[1]]['total_conf_cases'] += v['total_conf_cases']
        result[k[1]]['total_deaths'] += v['total_deaths']
        result[k[1]]['total_recoveries'] += v['total_recoveries']

    ret = []
    for k, v in result.items():
        ret.append([k, v['total_conf_cases'], v['total_deaths'], v['total_recoveries']])
    return ret

#to get total number of conf death and recovery cases

def get_total_of_records(list_of_records):
    total_conf_cases = 0
    total_deaths = 0
    total_recoveries = 0

    for record in list_of_records:
        total_recoveries += int(record[-1])
        total_deaths += int(record[-2])
        total_conf_cases += int(record[-3])
    return (total_conf_cases,total_deaths,total_recoveries)

