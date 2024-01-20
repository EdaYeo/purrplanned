   self.canvas = Canvas(self, width=500, height=200, bd=0, highlightthickness=0)
    self.canvas.create_rectangle(245,50,345,150, fill='white')

    self.image = tk.PhotoImage(file='chess.png')
    self.image_id = self.canvas.create_image(50,50, image=self.image)

    self.canvas.move(self.image_id, 245, 100)