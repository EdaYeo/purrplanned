import handle_csv
from datetime import datetime

def sort_datetime(data):
    header = data[0]
    sorted_data = sorted(data, key=lambda x: x[2])
    return tuple(sorted_data)

# Example Usage:
# csv_filename = 'tasks.csv'
# unsorted_tuples = handle_csv.read_csv(csv_filename)
# sorted_tuples = sort_datetime(unsorted_tuples)
# print(sorted_tuples)