import customtkinter as ctk

class AddWindow(ctk.CTkToplevel):
     def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.attributes("-topmost", True)
 
        # Sets the title of the window to "App"
        self.title("GUI Application")   
        # Sets the dimensions of the window to 600x700
        #self.geometry(500, 500)    
 
        # Name Label
        self.nameLabel = ctk.CTkLabel(self,
                                text="Name")
        self.nameLabel.grid(row=0, column=0,
                            padx=20, pady=20,
                            sticky="ew")
 
        # Name Entry Field
        self.nameEntry = ctk.CTkEntry(self,
                          placeholder_text="Teja")
        self.nameEntry.grid(row=0, column=1,
                            columnspan=3, padx=20,
                            pady=20, sticky="ew")
 
        # Age Label
        self.ageLabel = ctk.CTkLabel(self, text="Age")
        self.ageLabel.grid(row=1, column=0,
                           padx=20, pady=20,
                           sticky="ew")
 
        # Age Entry Field
        self.ageEntry = ctk.CTkEntry(self,
                            placeholder_text="18")
        self.ageEntry.grid(row=1, column=1,
                           columnspan=3, padx=20,
                           pady=20, sticky="ew")
 
        # Gender Label
        self.genderLabel = ctk.CTkLabel(self,
                                  text="Gender")
        self.genderLabel.grid(row=2, column=0, 
                              padx=20, pady=20,
                              sticky="ew")
 
        # Gender Radio Buttons
        self.genderVar = ctk.StringVar(value="Prefer \
                                         not to say")
 
        self.maleRadioButton = ctk.CTkRadioButton(self,
                                   text="Male",
                                   variable=self.genderVar,
                                         value="He is")
        self.maleRadioButton.grid(row=2, column=1,
                                  padx=20, pady=20,
                                  sticky="ew")
 
        self.femaleRadioButton = ctk.CTkRadioButton(self,
                                     text="Female",
                                     variable=self.genderVar,
                                     value="She is")
        self.femaleRadioButton.grid(row=2, column=2,
                                    padx=20, pady=20,
                                    sticky="ew")
         
        self.noneRadioButton = ctk.CTkRadioButton(self,
                                    text="Prefer not to say",
                                    variable=self.genderVar,
                                    value="They are")
        self.noneRadioButton.grid(row=2, column=3, padx=20,
                                  pady=20, sticky="ew")
 
        # Choice Label
        self.choiceLabel = ctk.CTkLabel(self,
                                        text="Choice")
        self.choiceLabel.grid(row=3, column=0,
                              padx=20, pady=20,
                              sticky="ew")
 
        # Choice Check boxes
        self.checkboxVar = ctk.StringVar(value="Choice 1")
         
        self.choice1 = ctk.CTkCheckBox(self,
                             text="choice 1",
                             variable=self.checkboxVar,
                             onvalue="choice1", offvalue="c1")
        self.choice1.grid(row=3, column=1,
                          padx=20, pady=20,
                          sticky="ew")
 
        self.choice2 = ctk.CTkCheckBox(self,
                            text="choice 2",
                            variable=self.checkboxVar,
                            onvalue="choice2",
                            offvalue="c2")                               
        self.choice2.grid(row=3, column=2,
                          padx=20, pady=20,
                          sticky="ew")
 
        # Occupation Label
        self.occupationLabel = ctk.CTkLabel(self,
                                    text="Occupation")
        self.occupationLabel.grid(row=4, column=0,
                                  padx=20, pady=20,
                                  sticky="ew")
 
        # Occupation combo box
        self.occupationOptionMenu = ctk.CTkOptionMenu(self,
                                       values=["Student",
                                       "Working Professional"])
        self.occupationOptionMenu.grid(row=4, column=1,
                                       padx=20, pady=20,
                                       columnspan=2, sticky="ew")
 

 
        # Text Box
        self.displayBox = ctk.CTkTextbox(self,
                                         width=200,
                                         height=100)
        self.displayBox.grid(row=6, column=0,
                             columnspan=4, padx=20,
                             pady=20, sticky="nsew")
        


app = AddWindow()
app.mainloop()