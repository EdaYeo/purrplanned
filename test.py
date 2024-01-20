import tkinter as tk
from PIL import Image, ImageTk

class ClickThroughWindow(tk.Tk):
    def __init__(self, image_path, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        self.overrideredirect(True)  # Remove window decorations
        self.wm_attributes("-transparentcolor", "black")  # Set black as the transparent color

        # Load and display the image
        image = Image.open(image_path)
        self.image = ImageTk.PhotoImage(image)
        label = tk.Label(self, image=self.image, bd=0)
        label.pack()

        # Bind events for dragging
        label.bind("<B1-Motion>", self.mouse_motion)
        label.bind("<Button-1>", self.mouse_press)

    def mouse_motion(self, event):
        x, y = event.x, event.y
        new_x = self.winfo_x() + x
        new_y = self.winfo_y() + y
        new_geometry = f"+{new_x}+{new_y}"
        self.geometry(new_geometry)

    def mouse_press(self, event):
        self.x, self.y = event.x, event.y

if __name__ == "__main__":
    image_path = "./hehe.jpg"  # Specify the path to your image file
    window = ClickThroughWindow(image_path)
    window.mainloop()
