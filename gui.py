import tkinter as tk
import customtkinter as ctk
from PIL import Image, ImageTk

ctk.set_appearance_mode("dark-blue")

class EntryFrame(ctk.CTkFrame):
    def __init__(self, master, title, description, deadline, index):
        super().__init__(master)

        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=2)
        self._border_width = 1
        self._border_color = "#4C7273"
        self._fg_color = "transparent"

        self.check_var = ctk.StringVar(value="on")
        self.checkbox = ctk.CTkCheckBox(self, text="", variable=self.check_var, onvalue="on", offvalue="off", height=10)
        self.checkbox.grid(row=0, column=0, sticky="s")

        # Title of Task
        self.entry_text = ctk.CTkTextbox(master=self, text_color="#D0D6D6",height=3, width=200, fg_color="transparent", activate_scrollbars=False, border_width=0, border_color="#000000", corner_radius=0)
        self.entry_text.grid(row=0, column=1,sticky="w")
        self.entry_text.insert("0.0", title)
        self.entry_text.configure(state="disabled")

        # Deadline
        self.deadline = ctk.CTkTextbox(master=self, text_color="#D0D6D6", height=3, width=200, fg_color="transparent", activate_scrollbars=False, border_width=0, border_color="#4C7273", corner_radius=0)
        self.deadline.grid(row=0, column=2, sticky="w")  # Set column to 2
        self.deadline.insert("0.0", deadline)
        self.deadline.configure(state="disabled")

        # Description
        self.entry_text = ctk.CTkTextbox(master=self, text_color="#D0D6D6", height=3, width=200, fg_color="transparent", activate_scrollbars=False, border_width=0, border_color="#4C7273", corner_radius=0)
        self.entry_text.grid(row=1, column=1, pady=(0,7), sticky="w", columnspan=2)  # Set columnspan to 2
        self.entry_text.insert("0.0", description)
        self.entry_text.configure(state="disabled")

        pencil = Image.open("./pencil.png").resize((20,20))
        self.add_button = ctk.CTkButton(self, width= 2, height = 2, text="", corner_radius=8, text_color="black", fg_color="transparent",image=ImageTk.PhotoImage(pencil))
        self.add_button.grid(row=0, column=3, padx=0, pady=(10,0), sticky="s")

        bin = Image.open("./bin.png").resize((20,20))
        self.delete_button = ctk.CTkButton(self, width= 2, height = 2, text="", corner_radius=8, text_color="black", fg_color="transparent",image=ImageTk.PhotoImage(bin))
        self.delete_button.grid(row=0, column=4, padx=3, pady=(10,0), sticky="s")
        
class NavBarFrame(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)
        self.grid_rowconfigure(0, weight=1)  # configure grid system
        self.grid_columnconfigure(0, weight=1)
        self._border_width = 1
        self._fg_color = "transparent"
        self._border_color = "transparent"
        self._corner_radius = 0

        self.entry_text = ctk.CTkTextbox(master=self, text_color="#D0D6D6", height=3, width=200, fg_color="transparent",
                                         activate_scrollbars=False, border_width=0, border_color="#000000",
                                         corner_radius=0)
        self.entry_text.grid(row=0, column=0, sticky="nw")
        self.entry_text.insert("0.0", "Planner!")
        self.entry_text.configure(state="disabled")

        add = Image.open("./add.png").resize((120,28))
        self.delete_button = ctk.CTkButton(self, width= 2, height = 2, text="", corner_radius=0, text_color="black", fg_color="transparent",image=ImageTk.PhotoImage(add))
        self.delete_button.grid(row=0, column=1, padx=23, pady=(3,0), sticky="e")
        #self.add_button = ctk.CTkButton(self, corner_radius=0, text_color="black",fg_color="transparent",image=ImageTk.PhotoImage(add))
        #self.add_button.grid(row=0, column=1, padx=221, pady=(3, 0), sticky="e")


root = ctk.CTk(fg_color="#041421") 
root.title("planner")
#root._fg_color("black")
nav = NavBarFrame(root)
#menu = MenuFrame(root)
nav.grid(row=0, column=1, padx=0, pady=5, sticky="nw", columnspan=2)
#menu.grid(row=0, column=1, padx=0, pady=0, sticky="nw", rowspan=4)

# Use a list to store EntryFrames dynamically
entry_frames = []
entry_frames.append(EntryFrame(root, "TESTING", "Testing Description", "10/10/20", 1))
entry_frames.append(EntryFrame(root, "TESTING2", "Testing2 Description", "1/1/23", 2))

# Use enumerate to get both index and entry_frame
for index, entry_frame in enumerate(entry_frames, start=1):
    if(index == 0):
        entry_frame.grid(row=index, column=1, padx=0, pady=(2,0), sticky="nw")
    else:
        entry_frame.grid(row=index, column=1, padx=0, pady=0, sticky="nw")

# Calculate the required width and height based on widget sizes
width = max(root.winfo_reqwidth(), sum(entry_frame.winfo_reqwidth() for entry_frame in entry_frames))
height = max(root.winfo_reqheight(), sum(entry_frame.winfo_reqheight() for entry_frame in entry_frames))

root.after(0, lambda:root.state('zoomed'))

# Update the window geometry
root.update_idletasks()
width = max(root.winfo_reqwidth(), sum(entry_frame.winfo_reqwidth() for entry_frame in entry_frames))
height = max(root.winfo_reqheight(), sum(entry_frame.winfo_reqheight() for entry_frame in entry_frames))

root.mainloop()