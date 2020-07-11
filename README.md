# Reverse Geocoding Using Geocode.xyz API

A small side project to assign region/county names to a list of unidentified latitudes and longitudes.

Given the a csv with two columns (latitude and longitude), this project converts the csv to a pandas dataframe to iterate through each row and convert them into the Geocoding API request format: https://geocode.xyz/location?outputformat.

The .JSON file is then parsed through and the 'region' feature is extracted and appended into a list for later conversion and use.
