import handle_csv
from datetime import datetime

def sort_datetime(data):
    header = data[0]
    sorted_data = sorted(data, key=lambda x: x[2])
    return tuple(sorted_data)

def convert_to_datetime(date):
    min_datetime = datetime(int(date[0:4]), int(date[5:7]), int(date[8:10]), int(date[11:13]), int(date[14:16]), int(date[17:19]))
    print(min_datetime)
    return min_datetime

def time_till_due(data):
    sorted_list = sort_datetime(data)
    min_datetime = sorted_list[0][2]
    min_datetime = convert_to_datetime(min_datetime)
    current_time = datetime.now()
    time_difference = min_datetime - current_time
    minutes_difference = max(0, time_difference.total_seconds() // 60)

    return minutes_difference

def cat_pic(data):
    difference = time_till_due(data)
    if (difference < 60):
        return "shag.PNG"
    
    elif (difference < 180):
        return "scream.PNG"
    
    elif (difference < 300) :
        return "quake.PNG"
    
    elif (difference < 720) : 
        return "stare.PNG"
    
    elif (difference < 1440) :
        return "sweat.PNG"
    else:
        return "calm.PNG"

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

#date = "2024-01-01 20:00:00"
#print(date[0:4])
#convert_to_datetime("2024-01-01 20:00:00")


