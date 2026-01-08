
#Author: Gabriel Venegas
#Github:GVenegas1
#Jan/7/2026
#Discription:  This script defines a function that calculates similarity between
# a target string and a list of strings using fuzzy matching.

# Import fuzz module from fuzzywuzzy
from fuzzywuzzy import fuzz

def string_distance(string_list, target):
    """Takes a list of strings and a target string, and returns the distance
    Returns a dictionary where keys are strings from the list"""

    # Empty dictionary to store results
    similarity_list = {}

    # Loop through each string in the list
    for string in string_list:
        # Calculate similarity using fuzz.ratio()
        similarity = fuzz.ratio(string, target)
        # Add it to the dictionary
        similarity_list[string] = similarity

    return similarity_list

