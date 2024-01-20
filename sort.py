import handle_csv
from datetime import datetime

def sort_datetime(data):
    header = data[0]
    sorted_data = sorted(data, key=lambda x: x[2])
    return tuple(sorted_data)

def time_till_due(data):
    sorted_list = sort_datetime(data)
    min_datetime = sorted_list[0][2]
    current_time = datetime.now()
    time_difference = min_datetime - current_time
    minutes_difference = max(0, time_difference.total_seconds() // 60)

    return minutes_difference

def cat_pic(data):
    difference = time_till_due(data)
    if (difference < 1):
        print("stare")
        return "stare.png"
    
    elif (difference < 2):
        print("scream")
        return "scream.png"
    
    elif (difference < 3) :
        print("quake")
        return "quake.png"
    elif (difference < 4) :
        print("sweat")
        return "sweat.png"
    elif (difference < 5) :
        print("shag")
        return "shag.png"
    else:
        print("calm")
        return "calm.png"

# data = [
#     ("Item1", "Description1", datetime(2024, 1, 21, 5, 40, 0)),
#     ("Item2", "Description2", datetime(2024, 1, 21, 7, 30, 0)),
#     # ... more data ...
# ]

# print(cat_pic(data))

# remaining_time = time_till_due(data)
# print(remaining_time)
# Example Usage:
# csv_filename = 'tasks.csv'
# unsorted_tuples = handle_csv.read_csv(csv_filename)
# sorted_tuples = sort_datetime(unsorted_tuples)
# print(sorted_tuples)