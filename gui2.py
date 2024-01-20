import tkinter as tk
import customtkinter as ctk
from ctypes import windll
from PIL import Image, ImageTk

import handle_csv as parsecsv
from datetime import datetime
import time

ctk.set_appearance_mode("dark-blue")
#index = 3
other_window_open = False


class AddWindow(ctk.CTkToplevel):
    # I think mine doesnt work cause its catering to my system which is in light mode, we didnt
    # have styling for this
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.attributes("-topmost", True)
        self.title("Add Task")
        #self.config(highlightthickness=0, bg=root["bg"])   
 
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
        #entry_frame = EntryFrame(root, self.nameEntry.get(), self.remarksEntry.get(), datetime.strptime(self.deadlineEntry.get(), '%d-%m-%Y %H:%M:%S'), 3)
        #entry_frames.append(entry_frame)
        update_table("Tasks.csv")
        self.withdraw()
        # index += 1

class EditWindow(ctk.CTkToplevel):
    def __init__(self, edit_title, edit_date, edit_desc, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.attributes("-topmost", True)
        self.title("Add Task")
        self.edit_title = edit_title   
 
        # Title Label
        self.nameLabel = ctk.CTkLabel(self,
                                text="Title")
        self.nameLabel.grid(row=0, column=0,
                            padx=20, pady=20,
                            sticky="ew")
 
        # Name Entry Field
        self.nameEntry = ctk.CTkEntry(self,
                          placeholder_text=edit_title)
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
                            placeholder_text=edit_date)
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
                            placeholder_text=edit_desc, width=500)
        self.remarksEntry.grid(row=2, column=1,
                           columnspan=5, padx=20,
                           pady=20, sticky="ew")

        self.submit_button = ctk.CTkButton(self, text="SUBMIT", command= self.editCSV)
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
    # TODOOOO
    def delete(self):
        other_window_open == True
        #print("CURR INDEX DELETING: " + str(self.index))
        parsecsv.delete_csv_entry("Tasks.csv", self.title)
        #print(len(entry_frames))
        # for i in range(self.index, len(entry_frames)):
        #     entry_frames[i].place_forget()
        update_table("Tasks.csv")
        print(other_window_open)


    # def add_window(self):
    #     if self.toplevel_window is None:
    #         self.toplevel_window = AddWindow(self)
    #     else:
    #         self.toplevel_window.focus()

class NavBarFrame(ctk.CTkCanvas):
    def __init__(self, master):
        super().__init__(master)
        self.grid_rowconfigure(0, weight=1)  # configure grid system
        self.grid_columnconfigure(0, weight=1)
        #self._border_width = 1
        #self._fg_color = "transparent"
        self.config(highlightthickness=0, bg=root["bg"])
        #self._border_color = "transparent"
        self._corner_radius = 0

        self.entry_text = ctk.CTkTextbox(master=self, text_color="#D0D6D6", height=3, width=200, fg_color="transparent",
                                         activate_scrollbars=False, border_width=0, border_color="#000000",
                                         corner_radius=0)
        self.entry_text.grid(row=0, column=0, sticky="nw")
        self.entry_text.insert("0.0", "Planner!")
        self.entry_text.configure(state="disabled")

        add = Image.open("./add.png").resize((120,28))
        self.add_button = ctk.CTkButton(self, width= 2, height = 2, text="", corner_radius=0, command=self.add_window, text_color="black", fg_color="transparent",image=ImageTk.PhotoImage(add))
        self.add_button.grid(row=0, column=1, padx=23, pady=(3,0), sticky="e")
        #self.add_button = ctk.CTkButton(self, corner_radius=0, text_color="black",fg_color="transparent",image=ImageTk.PhotoImage(add))
        #self.add_button.grid(row=0, column=1, padx=221, pady=(3, 0), sticky="e")

        
        #self.toplevel_window = None

    def add_window(self):
        new_toplevel = AddWindow()

def maketransparent(w):
    # the translated windll part...
    # a COLORREF structure is a reverse RGB order int!
    # see https://www.pinvoke.net/search.aspx?search=COLORREF&namespace=[All]
    # here we chose nearly black so real black (#000000) still shows up
    colorkey = 0x00030201
    hwnd = w.winfo_id()
    wnd_exstyle = windll.user32.GetWindowLongA(hwnd, -20)  # GWL_EXSTYLE
    new_exstyle = wnd_exstyle | 0x00080000  # WS_EX_LAYERED
    windll.user32.SetWindowLongA(hwnd, -20, new_exstyle)  # GWL_EXSTYLE
    windll.user32.SetLayeredWindowAttributes(hwnd, colorkey, 255, 0x00000001)  # LWA_COLORKEY = 0x00000001

def create_new_window(event):
    if (other_window_open == False):
        win = ctk.CTkToplevel(root)
        win.geometry('400x200')
        #win.title("New Window")
        #win.attributes('-fullscreen', True)  # Make the window full-screen
        #win.after(0, lambda: win.state('zoomed'))
        canvas = tk.Canvas(win, width=2000, height=2000, background='#000000')
        label = tk.Label(canvas,borderwidth=0,bg='#000000')
        label.pack()
        #button = tk.Button(canvas, text="HAI")
        canvas.grid(row=0, column=0, sticky='nesw')
        #canvas.pack()
        #window.overrideredirect(True)
        win.wm_attributes('-transparentcolor','#000000')
        win.wm_attributes('-topmost', True)
        cvs_upper=tk.Canvas(win, background='#010203') #dont use all black, screws up any black trext on your canvas...
        #cvs_upper.create_rectangle(325, 25, 375, 175, fill='red')
        cvs_upper.grid(row=0, column=0, sticky='nesw')
        #cvs_upper.place(x=10, y=10)
        canvas.create_window(0, 0, anchor=tk.NW, window=label)

        image1 = Image.open("actual_kalm_cat.PNG")
        test = ImageTk.PhotoImage(image1)
        label1 = ctk.CTkLabel(cvs_upper, height = 500, width = 500, fg_color="transparent", image=test)
        #label1.image = test
        label1.place(x=550, y=100)

        win.after(0, lambda:win.state('zoomed'))
        win.after(0, lambda:maketransparent(cvs_upper))
        win.mainloop()

root = ctk.CTk(fg_color="#041421") 
root.title("planner")
nav = NavBarFrame(root)
nav.place(relx=0.5, rely=0.05, anchor="center")


# Use a list to store EntryFrames dynamically
entry_frames = []

# new update_table based on csv functions
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