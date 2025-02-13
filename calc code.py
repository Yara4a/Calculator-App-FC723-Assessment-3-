import tkinter as tk  # Import tkinter using an alias

class CalculatorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculator")  # Set window title
        self.root.geometry("400x300")  # Set window size

        # Display text or images with labels
        self.label = tk.Label(self.root, text="WELCOME!", font=("Arial", 20))
        self.label.pack(pady=50)

        # Welcome button
        self.welcome_button = tk.Button(self.root, text="Click Here", command=self.clear_screen)
        self.welcome_button.pack()




    def clear_screen(self):
        # Destroy all widgets in the root window
        for widget in self.root.winfo_children():
            widget.destroy()

        # Create new content for page 2
        label = tk.Label(self.root, text="This is page 2 (We can change it)", font=("Arial", 20))
        label.pack(pady=50)




if __name__ == "__main__":
    root = tk.Tk()
    app = CalculatorApp(root)
    root.mainloop()
