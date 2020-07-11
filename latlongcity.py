import pandas as pd
import requests
import json
import time

df = pd.read_csv('latlong.csv')

# create empty list to store lats + longs
locations =[]

# iterate over each row
for index, rows in df.iterrows():
    # Create list for the current row
    my_list =[rows.latitude, rows.longitude]

    # append the list to the final list
    locations.append(my_list)

# text for API request
front = "http://geocode.xyz/"
back = "?geoit=json"

# create empty list to record names associated with latlong values
region = []

for x in range(0,len(locations)):
    # isolate latitude and longitude values from each list
    lat = locations[x][0]
    long = locations[x][1]

    # combine the API request url with the specific latlong values into a string
    path = front + str(lat) + "," + str(long) + back

    # use requests package to call the API and store .json file into python dictionary
    r = requests.get(path)
    r_dict = r.json()

    # if statement to allow for default values and ignore entries without 'region'
    if r_dict['region'] is None:
        region.append(0)
    else:
        region.append(r_dict['region'])

    # avoid throttling the server
    time.sleep(1.5)
