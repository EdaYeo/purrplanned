import csv
import os
from datetime import datetime

def read_csv(csvfilename):
    rows = ()
    with open(csvfilename, 'r', newline='') as csvfile:
        file_reader = csv.reader(csvfile)
        for row in file_reader:
            rows += (tuple(row), )
    return rows

def write_to_csv(entry_data, filename):
    # Define the CSV header
    header = ['Title', 'Description', 'Deadline', 'Completion Status']

    # Check if the file already exists
    if os.path.exists(filename):
        # File exists, open in append mode and add data
        with open(filename, mode='a', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=header)
            
            # Check if the header needs to be written
            if os.stat(filename).st_size == 0:
                writer.writeheader()
            
            writer.writerow(entry_data)
        print(f"Data appended to {filename}")
    else:
        # File doesn't exist, create a new file and write data
        with open(filename, mode='w', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=header)
            writer.writeheader()
            entry_data['Deadline'] = entry_data['Deadline'].strftime('%D-%m-%Y %H:%M:%S') # Parse datetime object into string
            writer.writerow(entry_data)
        print(f"New file {filename} created with data")

def edit_csv_entry(filename, title_to_search, updated_data):
    # Check if the file exists
    if os.path.exists(filename):
        # Read the existing data
        with open(filename, mode='r', newline='') as file:
            reader = csv.DictReader(file)
            data = list(reader)

        if data:  # Check if data is not empty
            # Find the index of the entry with the matching title
            entry_index = next((index for index, entry in enumerate(data) if entry['Title'] == title_to_search), None)

            if entry_index is not None:
                # Update the entry with the new data
                data[entry_index].update(updated_data)

                # Write the updated data back to the file
                with open(filename, mode='w', newline='') as file:
                    writer = csv.DictWriter(file, fieldnames=data[0].keys())
                    writer.writeheader()
                    writer.writerows(data)

                print(f"Entry with title '{title_to_search}' updated in {filename}")
            else:
                print(f"Entry with title '{title_to_search}' not found in {filename}")
        else:
            print(f"File {filename} is empty")
    else:
        print(f"File {filename} not found")

def delete_csv_entry(filename, title_to_delete):
    # Check if the file exists
    if os.path.exists(filename):
        # Read the existing data
        with open(filename, mode='r', newline='') as file:
            reader = csv.DictReader(file)
            data = list(reader)

        if data:  # Check if data is not empty
            # Find the index of the entry with the matching title
            entry_index = next((index for index, entry in enumerate(data) if entry['Title'] == title_to_delete), None)

            if entry_index is not None:
                # Remove the entry from the data list
                del data[entry_index]

                # Write the updated data back to the file
                with open(filename, mode='w', newline='') as file:
                    if data:  # Check if there is remaining data
                        writer = csv.DictWriter(file, fieldnames=data[0].keys())
                        writer.writeheader()
                        writer.writerows(data)
                        print(f"Entry with title '{title_to_delete}' deleted from {filename}")
                    else:
                        # If no data left, you may choose to skip writing the header
                        print(f"Entry with title '{title_to_delete}' deleted from {filename}. No remaining data.")
            else:
                print(f"Entry with title '{title_to_delete}' not found in {filename}")
        else:
            print(f"File {filename} is empty")
    else:
        print(f"File {filename} not found")

# Example usage:
# entry_data_to_write = {
#     'Title': 'Task 1',
#     'Description': 'Complete assignment',
#     'Deadline': datetime.strptime('2024-01-31 18:00:00', '%d-%m-%Y %H:%M:%S'),  # Format: YYYY-MM-DD HH:MM:SS
#     'Completion Status': 'Incomplete'
# }

# # Specify the filename (change it as needed)
# csv_filename = 'tasks.csv'

# # Call the function with data and filename
# # write_to_csv(entry_data_to_write, csv_filename)

# # Example usage:
# csv_filename = 'tasks.csv'

# # Specify the title of the entry to edit
# title_to_edit = 'Updated Task'

# # Specify the updated data for the entry
# updated_entry_data = {
#     'Title': 'Updated Task',
#     'Description': 'Updated description',
#     'Deadline': datetime.strptime('2024-01-31 20:00:00', '%d-%m-%Y %H:%M:%S'),
#     'Completion Status': 'Complete'
# }

# # Call the function to edit the CSV entry by title
# # edit_csv_entry(csv_filename, title_to_edit, updated_entry_data)

# # Specify the filename (change it as needed)
# csv_filename = 'tasks.csv'

# # Specify the title of the entry to delete
# title_to_delete = 'Updated Task'

# # Call the function to delete the CSV entry by title
# # delete_csv_entry(csv_filename, title_to_delete)