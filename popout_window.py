import customtkinter

class ToplevelWindow(customtkinter.CTkToplevel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.attributes('-fullscreen', True)  # Make the window full-screen

        self.label = customtkinter.CTkLabel(self, text="ToplevelWindow")
        self.label.pack(padx=20, pady=20)

class App(customtkinter.CTk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.geometry("300x200")

        self.button_1 = customtkinter.CTkButton(self, text="open toplevel", command=self.open_toplevel)
        self.button_1.pack(side="top", padx=20, pady=20)

        self.toplevel_window = None

    def open_toplevel(self):
        if self.toplevel_window is None or not self.toplevel_window.winfo_exists():
            self.toplevel_window = ToplevelWindow(self)  # create window if its None or destroyed
            self.iconify()
        else:
            self.toplevel_window.focus()  # if window exists, focus it
            self.iconify()

def create_new_window(event):
    # Check if the new window is already created
    if not hasattr(app, '_new_window') or not app._new_window:
        new_window = customtkinter.CTkToplevel(app)
        new_window.title("New Window")
        new_window.attributes('-fullscreen', True)  # Make the window full-screen
        new_window.after(0, lambda:new_window.state('zoomed'))
        # new_window.geometry("{0}x{1}+0+0".format(new_window.winfo_screenwidth(), new_window.winfo_screenheight()))

        new_window.withdraw()  # Hide the window initially
        app._new_window = new_window  # Store a reference to the new window in the root

        # Show the window when needed
        new_window.deiconify()

def testing():
    print("HEY")

if __name__ == "__main__":
    app = App()
    app.bind("<Unmap>", create_new_window)
    app.mainloop()
