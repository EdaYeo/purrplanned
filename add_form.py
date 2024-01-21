import customtkinter as ctk
from datetime import datetime
import handle_csv as parsecsv

class AddWindow(ctk.CTkToplevel):
    # I think mine doesnt work cause its catering to my system which is in light mode, we didnt
    # have styling for this
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.attributes("-topmost", True)
        self.title("Add Task")
 
        # Title Label
        self.nameLabel = ctk.CTkLabel(self,
                                text="Title")
        self.nameLabel.grid(row=0, column=0,
                            padx=20, pady=20,
                            sticky="ew")
 
        # Name Entry Field
        self.nameEntry = ctk.CTkEntry(self,
                          placeholder_text="")
        self.nameEntry.grid(row=0, column=1,
                            columnspan=3, padx=20,
                            pady=20, sticky="ew")
 
        # Deadline Label
        self.deadlineLabel = ctk.CTkLabel(self, text="Deadline")
        self.deadlineLabel.grid(row=1, column=0,
                           padx=20, pady=20,
                           sticky="ew")
 
        # Deadline Field
        self.deadlineEntry = ctk.CTkEntry(self,
                            placeholder_text="DD-MM-YYYY HH:MM:SS")
        self.deadlineEntry.grid(row=1, column=1,
                           columnspan=3, padx=20,
                           pady=20, sticky="ew")
        
        # Remarks Label
        self.remarksLabel = ctk.CTkLabel(self, text="Description")
        self.remarksLabel.grid(row=2, column=0,
                           padx=20, pady=20,
                           sticky="ew")
 
        # Remarks Field
        self.remarksEntry = ctk.CTkEntry(self,
                            placeholder_text="", width=500)
        self.remarksEntry.grid(row=2, column=1,
                           columnspan=5, padx=20,
                           pady=20, sticky="ew")

        self.submit_button = ctk.CTkButton(self, text="SUBMIT", command=self.addToCSV)
        self.submit_button.grid(row=3, column=1,
                           columnspan=5, padx=20,
                           pady=20, sticky="ew")
        
    
    def addToCSV(self):
        data = {
            'Title': self.nameEntry.get(),
            'Description': self.remarksEntry.get(),
            'Deadline': datetime.strptime(self.deadlineEntry.get(), '%d-%m-%Y %H:%M:%S'),  # Format: 01-01-2024 20:00:00
            'Completion Status': 'Incomplete'
        }

        parsecsv.write_to_csv(data, 'Tasks.csv')
        print(parsecsv.read_csv("Tasks.csv")[1][0])
        print(data)
        self.withdraw()

    def update_table(filename):
        global other_window_open 
        other_window_open = True
        for entry_frame in entry_frames:
            entry_frame.place_forget()
        entry_frames.clear()
        data = parsecsv.read_csv(filename)
        for i in range(1, len(data)):
            entry_frames.append(EntryFrame(root, data[i][0], data[i][1], data[i][2], i-1))
        for index, entry_frame in enumerate(entry_frames, start=1):
            if (index == 0):
                entry_frame.place(relx=0.5, rely=0.05 + (index * 0.1), anchor="center")
            else:
                # omg DED this is based on com resolution
                entry_frame.place(relx=0.5, rely=0.05 + (index * 0.069), anchor="center")
        other_window_open = False