import tkinter as tk
import customtkinter as ctk
from ctypes import windll
from PIL import Image, ImageTk
import csv
import os
import handle_csv as parsecsv
from datetime import datetime
import sort as sortdates

ctk.set_appearance_mode("dark-blue")
other_window_open = False

if not os.path.exists('Tasks.csv'):
    # If file doesn't exist, create a new file and write data
    header = ['Title', 'Description', 'Deadline', 'Completion Status']
    with open('Tasks.csv', mode='w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=header)
        writer.writeheader()
    print(f"New file {'Tasks.csv'} initialised")


class AddWindow(ctk.CTkToplevel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.attributes("-topmost", True)
        self.title("Add Task")        
        self.config(highlightthickness=0, bg=root["bg"]) 

        # Title Label   
        self.nameLabel = ctk.CTkLabel(self,
                                text="Title", text_color="#D0D6D6", fg_color="#4C7273",
                                width=100, corner_radius=0)
        self.nameLabel.grid(row=0, column=0,
                            padx=20, pady=20,
                            sticky="ew")
         
        # Name Entry Field
        self.nameEntry = ctk.CTkEntry(self,
                          placeholder_text="", text_color="#000000", fg_color="#ffffff",
                          border_width=0, border_color="#000000", corner_radius=0)
        self.nameEntry.grid(row=0, column=1,
                            columnspan=3, padx=20,
                            pady=20, sticky="ew")
 
        # Deadline Label
        self.deadlineLabel = ctk.CTkLabel(self, text="Deadline", text_color="#D0D6D6", fg_color="#4C7273",
                                          width=100, corner_radius=0)
        self.deadlineLabel.grid(row=1, column=0,
                           padx=20, pady=20,
                           sticky="ew")
 
        # Deadline Field
        self.deadlineEntry = ctk.CTkEntry(self,
                            placeholder_text="DD-MM-YYYY HH:MM:SS", text_color="#000000", fg_color="#ffffff",
                            border_width=0, border_color="#000000", corner_radius=0)
        self.deadlineEntry.grid(row=1, column=1,
                           columnspan=3, padx=20,
                           pady=20, sticky="ew")
        
        # Remarks Label
        self.remarksLabel = ctk.CTkLabel(self, text="Description", text_color="#D0D6D6", fg_color="#4C7273",
                                         width=100, corner_radius=0)
        self.remarksLabel.grid(row=2, column=0,
                           padx=20, pady=20,
                           sticky="ew")
 
        # Remarks Field
        self.remarksEntry = ctk.CTkEntry(self,
                            placeholder_text="", width=500, text_color="#000000", fg_color="#ffffff",
                            border_width=0, border_color="#000000", corner_radius=0)
        self.remarksEntry.grid(row=2, column=1,
                           columnspan=5, padx=20,
                           pady=20, sticky="ew")

        self.submit_button = ctk.CTkButton(self, text="SUBMIT", command=self.addToCSV, corner_radius=0)
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
        update_table("Tasks.csv")
        self.withdraw()

class EditWindow(ctk.CTkToplevel):
    def __init__(self, edit_title, edit_date, edit_desc, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.attributes("-topmost", True)
        self.title("Edit Task")
        self.edit_title = edit_title
        self.config(highlightthickness=0, bg=root["bg"]) 
 
        # Title Label
        self.nameLabel = ctk.CTkLabel(self,
                                text="Title", text_color="#D0D6D6", fg_color="#4C7273",
                                width=100, corner_radius=0)
        self.nameLabel.grid(row=0, column=0,
                            padx=20, pady=20,
                            sticky="ew")
 
        # Name Entry Field
        self.nameEntry = ctk.CTkEntry(self,
                          placeholder_text=edit_title, text_color="#000000", fg_color="#ffffff",
                            border_width=0, border_color="#000000", corner_radius=0)
        self.nameEntry.grid(row=0, column=1,
                            columnspan=3, padx=20,
                            pady=20, sticky="ew")
 
        # Deadline Label
        self.deadlineLabel = ctk.CTkLabel(self, text="Deadline", text_color="#D0D6D6", fg_color="#4C7273",
                                width=100, corner_radius=0)
        self.deadlineLabel.grid(row=1, column=0,
                           padx=20, pady=20,
                           sticky="ew")
 
        # Deadline Field
        self.deadlineEntry = ctk.CTkEntry(self,
                            placeholder_text=edit_date, text_color="#000000", fg_color="#ffffff",
                            border_width=0, border_color="#000000", corner_radius=0)
        self.deadlineEntry.grid(row=1, column=1,
                           columnspan=3, padx=20,
                           pady=20, sticky="ew")
        
        # Remarks Label
        self.remarksLabel = ctk.CTkLabel(self, text="Description", text_color="#D0D6D6", fg_color="#4C7273",
                                width=100, corner_radius=0)
        self.remarksLabel.grid(row=2, column=0,
                           padx=20, pady=20,
                           sticky="ew")
 
        # Remarks Field
        self.remarksEntry = ctk.CTkEntry(self,
                            placeholder_text=edit_desc, width=500, text_color="#000000", fg_color="#ffffff",
                            border_width=0, border_color="#000000", corner_radius=0)
        self.remarksEntry.grid(row=2, column=1,
                           columnspan=5, padx=20,
                           pady=20, sticky="ew")

        self.submit_button = ctk.CTkButton(self, text="SUBMIT", command= self.editCSV, corner_radius=0)
        self.submit_button.grid(row=3, column=1,
                           columnspan=5, padx=20,
                           pady=20, sticky="ew")
        
    def editCSV(self):
        data = {
            'Title': self.nameEntry.get(),
            'Description': self.remarksEntry.get(),
            'Deadline': datetime.strptime(self.deadlineEntry.get(), '%d-%m-%Y %H:%M:%S'),  # Format: 01-01-2024 20:00:00
            'Completion Status': 'Incomplete'
        }
        print(data)

        parsecsv.edit_csv_entry('Tasks.csv', self.edit_title, data)
        update_table("Tasks.csv")
        self.withdraw()

class EntryFrame(ctk.CTkCanvas):
    def __init__(self, master, title, description, deadline, index):
        super().__init__(master)
        self.index = index
        self.title = title
        self.description = description
        self.deadline = str(deadline)
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=2)
        self._border_width = 1
        self.config(highlightbackground="#4C7273", highlightthickness=1, bg=root["bg"])

        self.check_var = ctk.StringVar(value="off")
        self.checkbox = ctk.CTkCheckBox(self, text="", variable=self.check_var, onvalue="on", offvalue="off", height=10)
        self.checkbox.grid(row=0, column=0, padx=3, sticky="s")

        # Title of Task
        self.task_title = ctk.CTkTextbox(master=self, text_color="#D0D6D6",height=3, width=200, fg_color="transparent", activate_scrollbars=False, border_width=0, border_color="#000000", corner_radius=0)
        self.task_title.grid(row=0, column=1,sticky="w")
        self.task_title.insert("0.0", title)
        self.task_title.configure(state="disabled")

        # Deadline
        self.task_deadline = ctk.CTkTextbox(master=self, text_color="#D0D6D6", height=3, width=200, fg_color="transparent", activate_scrollbars=False, border_width=0, border_color="#4C7273", corner_radius=0)
        self.task_deadline.grid(row=0, column=2, sticky="w")  # Set column to 2
        self.task_deadline.insert("0.0", deadline)
        self.task_deadline.configure(state="disabled")

        # Description
        self.task_description = ctk.CTkTextbox(master=self, text_color="#D0D6D6", height=3, width=200, fg_color="transparent", activate_scrollbars=False, border_width=0, border_color="#4C7273", corner_radius=0)
        self.task_description.grid(row=1, column=1, pady=(0,7), sticky="w", columnspan=2)  # Set columnspan to 2
        self.task_description.insert("0.0", description)
        self.task_description.configure(state="disabled")

        pencil = Image.open("./pencil.png").resize((20,20))
        self.edit_button = ctk.CTkButton(self, width= 2, height = 2, text="", corner_radius=8, command=self.edit, text_color="black", fg_color="transparent",image=ImageTk.PhotoImage(pencil))
        self.edit_button.grid(row=0, column=3, padx=0, pady=(10,0), sticky="s")

        bin = Image.open("./bin.png").resize((20,20))
        self.delete_button = ctk.CTkButton(self, width= 2, height = 2, text="", corner_radius=8, command=self.delete, text_color="black", fg_color="transparent",image=ImageTk.PhotoImage(bin))
        self.delete_button.grid(row=0, column=4, padx=3, pady=(10,0), sticky="s")

        
    def edit(self):
        new_toplevel = EditWindow(self.title, self.deadline, self.description)
    
    # DELETE FUNC DOES NOT WORK when getting to last 2-3 entries, dk why.
    def delete(self):
        other_window_open == True
        parsecsv.delete_csv_entry("Tasks.csv", self.title)
        update_table("Tasks.csv")
        print(other_window_open)


class NavBarFrame(ctk.CTkCanvas):
    def __init__(self, master):
        super().__init__(master)
        self.grid_rowconfigure(0, weight=1)  # configure grid system
        self.grid_columnconfigure(0, weight=1)
        self.config(highlightthickness=0, bg=root["bg"])
        self._corner_radius = 0

        logo = Image.open("./purrplanned.png").resize((100,100))

        # Create a Label widget to display the logo
        self.logo_label = ctk.CTkLabel(self, image=ImageTk.PhotoImage(logo))
        self.logo_label.grid(row=0, column=0, sticky="nw", padx=5, pady=5)
        self.logo_label.configure(text="")

        self.entry_text = ctk.CTkTextbox(master=self, text_color="#D0D6D6", height=3, width=200, fg_color="transparent",
                                         activate_scrollbars=False, border_width=0, border_color="#000000",
                                         corner_radius=0)
        self.entry_text.grid(row=0, column=1)
        self.entry_text.insert("0.0", "Planner!")
        self.entry_text.configure(state="disabled")

        add = Image.open("./add.png").resize((120,28))
        self.add_button = ctk.CTkButton(self, width= 2, height = 2, text="", corner_radius=0, command=self.add_window, text_color="black", fg_color="transparent",image=ImageTk.PhotoImage(add))
        self.add_button.grid(row=0, column=2, padx=23, pady=(3,0), sticky="e")

    def add_window(self):
        new_toplevel = AddWindow()

def maketransparent(w):
    colorkey = 0x00030201
    hwnd = w.winfo_id()
    wnd_exstyle = windll.user32.GetWindowLongA(hwnd, -20)  # GWL_EXSTYLE
    new_exstyle = wnd_exstyle | 0x00080000  # WS_EX_LAYERED
    windll.user32.SetWindowLongA(hwnd, -20, new_exstyle)  # GWL_EXSTYLE
    windll.user32.SetLayeredWindowAttributes(hwnd, colorkey, 255, 0x00000001)  # LWA_COLORKEY = 0x00000001


def get_cat():
    data = parsecsv.read_csv("Tasks.csv")
    filename = sortdates.cat_pic(data)
    return filename

def create_new_window(event):
    if (other_window_open == False):
        win = ctk.CTkToplevel(root)
        win.geometry('400x200')
        canvas = tk.Canvas(win, width=2000, height=2000, background='#000000')
        label = tk.Label(canvas,borderwidth=0,bg='#000000')
        label.pack()
        canvas.grid(row=0, column=0, sticky='nesw')
        win.wm_attributes('-transparentcolor','#000000')
        win.wm_attributes('-topmost', True)
        cvs_upper=tk.Canvas(win, background='#010203') # Don't use all black to prevent errors with black text on canvas
        cvs_upper.grid(row=0, column=0, sticky='nesw')
        canvas.create_window(0, 0, anchor=tk.NW, window=label)

        filename = get_cat()
        image1 = Image.open(filename)
        test = ImageTk.PhotoImage(image1)
        label1 = ctk.CTkLabel(cvs_upper, height = 500, width = 500, fg_color="transparent", image=test)
        label1.place(x=500, y=80)

        win.after(0, lambda:win.state('zoomed'))
        win.after(0, lambda:maketransparent(cvs_upper))
        win.mainloop()

root = ctk.CTk(fg_color="#041421") 
root.title("planner")
nav = NavBarFrame(root)
nav.place(relx=0.5, rely=0.05, anchor="center")


# Use a list to store EntryFrames dynamically
entry_frames = []

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
            entry_frame.place(relx=0.5, rely=0.05 + (index * 0.069), anchor="center")
    other_window_open = False


# Calculate the required width and height based on widget sizes
width = max(root.winfo_reqwidth(), sum(entry_frame.winfo_reqwidth() for entry_frame in entry_frames))
height = max(root.winfo_reqheight(), sum(entry_frame.winfo_reqheight() for entry_frame in entry_frames))

root.after(0, lambda:root.state('zoomed'))
root.minsize(800, 800)

# Update the window geometry
root.update_idletasks()
width = max(root.winfo_reqwidth(), sum(entry_frame.winfo_reqwidth() for entry_frame in entry_frames))
height = max(root.winfo_reqheight(), sum(entry_frame.winfo_reqheight() for entry_frame in entry_frames))

update_table("Tasks.csv")
root.bind("<Unmap>", create_new_window)
root.mainloop()