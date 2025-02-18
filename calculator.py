import tkinter as tk

# Create a basic calculator
class Calculator:
    def __init__(self, master):
        self.master = master
        master.title("Calculator")
        master.configure(bg='#e6e6e6')
        
        # Create display
        self.display = tk.Entry(master, width=20, font=('Arial', 20), justify='right', bd=5)
        self.display.grid(row=0, column=0, columnspan=4, padx=5, pady=5, sticky='nsew')
        
        # Create buttons
        self.create_buttons()
        
        # Add flag to track if result is displayed
        self.result_shown = False
        
        # Configure grid
        for i in range(6):
            master.grid_rowconfigure(i, weight=1)
        for i in range(4):
            master.grid_columnconfigure(i, weight=1)

    def create_buttons(self):
        # Layout more like a numpad
        button_config = {
            '7': (1, 0), '8': (1, 1), '9': (1, 2), '/': (1, 3),
            '4': (2, 0), '5': (2, 1), '6': (2, 2), '*': (2, 3),
            '1': (3, 0), '2': (3, 1), '3': (3, 2), '-': (3, 3),
            '0': (4, 1), '.': (4, 0), '=': (4, 2), '+': (4, 3),
            'C': (5, 0, 4)  # Spans 4 columns
        }
        
        for (text, pos) in button_config.items():
            if len(pos) == 2:
                row, col = pos
                button = tk.Button(self.master, text=text, font=('Arial', 14),
                                 command=lambda t=text: self.button_click(t))
                button.grid(row=row, column=col, sticky='nsew', padx=2, pady=2)
            else:
                # Special case for Clear button spanning multiple columns
                row, col, span = pos
                button = tk.Button(self.master, text=text, font=('Arial', 14),
                                 command=lambda t=text: self.button_click(t))
                button.grid(row=row, column=col, columnspan=span, sticky='nsew', padx=2, pady=2)
    
    def button_click(self, value):
        if value == '=':
            try:
                result = eval(self.display.get())
                self.display.delete(0, tk.END)
                self.display.insert(tk.END, str(result))
                self.result_shown = True
            except:
                self.display.delete(0, tk.END)
                self.display.insert(tk.END, "Error")
        elif value == 'C':
            self.display.delete(0, tk.END)
            self.result_shown = False
        else:
            if self.result_shown:
                self.display.delete(0, tk.END)
                self.result_shown = False
            current = self.display.get()
            self.display.delete(0, tk.END)
            self.display.insert(tk.END, current + value)

# Create the main window
window = tk.Tk()
window.geometry("400x600")  # Made taller to accommodate the layout
calc = Calculator(window)
window.mainloop()