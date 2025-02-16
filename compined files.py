import tkinter as tk

class CalculatorApp:
    def __init__(self, root):
        # setting the window title and size 
        self.root = root
        self.root.title("Calculator")
        self.root.geometry("500x700")
        
        # displays the welcome message annd the welcome button 
        self.label = tk.Label(self.root, text="WELCOME!", font=("Times New Roman", 26))
        self.label.pack(pady=50)
        self.welcome_button = tk.Button(self.root, text="Click Here", command=self.clear_screen)
        self.welcome_button.pack()

        # Apply colors externally to initial screen
        self.root.configure(bg="#FAF6F7")
        self.label.configure(bg="#FFA2B9", fg="#FFD1DC")
        self.welcome_button.configure(bg="#FFA2B9", fg="#FFD1DC")
        
    def clear_screen(self):
            # this destroy the welcome page 
        for widget in self.root.winfo_children():
            widget.destroy()
                

            # Create the display
        display = self.create_display(self.root)

            # Define the buttons
        buttons = [
                'AC', 'x²', '√x', 'sin', 'arcsin',
                '7', '8', '9', 'cos', 'arccos',
                '4', '5', '6', 'tan', 'arctan',
                '1', '2', '3', '+', '-',
                'Exit', '0', '=', 'x', '÷',
            ]

            # Create and place the buttons
        self.create_buttons(self.root, buttons)

            # Configure the grid
        self.configure_grid(self.root)
        display.configure(bg="#FAF6F7", fg="#FFD1DC")
        for child in self.root.winfo_children():
            if isinstance(child, tk.Button):
                    child.configure(bg="#FFA2B9", fg="#FFD1DC")
          
    def create_display(self, root):
        #create and place the display entry widget.
        display = tk.Entry(root, font=('Times New Roman', 20), justify='right')
        display.grid(row=0, column=0, columnspan=5, sticky="nsew")
        return display
    
    def create_buttons(self, root, buttons):
        #create and place the buttons in the grid.
        row_val, col_val = 1, 0
        for button in buttons:
            btn = tk.Button(root, text=button, font=('Times New Roman', 20), padx=20, pady=20)
            btn.grid(row=row_val, column=col_val, sticky="nsew")
            col_val += 1
            if col_val > 4:
                col_val = 0
                row_val += 1
                
    def configure_grid(self, root):
        # configure the grid to expand properly.
        for i in range(5):
            root.grid_columnconfigure(i, weight=1)
        for i in range(6):
            root.grid_rowconfigure(i, weight=1)
            
            
if __name__ == "__main__":
    root = tk.Tk()
    app = CalculatorApp(root)
    root.mainloop()
            
            



       
        
      