import tkinter as tk
from tkinter import messagebox
import math

class ScientificCalculator:
    def __init__(self, master):
        self.master = master
        master.title("Scientific Calculator")
        master.geometry("600x600")
        master.resizable(False, False)
        
        # This variable will hold the user's input/expression.
        self.expression = ""
        
        # Create the display entry widget.
        self.display = tk.Entry(master, font=("Arial", 20), bd=10, relief=tk.RIDGE, justify='right')
        self.display.grid(row=0, column=0, columnspan=6, pady=20, padx=20, ipady=10)
        
        # Define the buttons to be used on the calculator.
        # This includes digits, basic operators, parentheses, and scientific functions.
        button_texts = [
            '7', '8', '9', '/', 'C', '⌫',
            '4', '5', '6', '*', '(', ')',
            '1', '2', '3', '-', 'sin', 'cos',
            '0', '.', '=', '+', 'tan', 'log',
            'exp', 'sqrt', 'pi', 'e'
        ]
        
        # Dynamically create and place buttons in a grid layout.
        row = 1
        col = 0
        for text in button_texts:
            button = tk.Button(master, text=text, font=("Arial", 18), bd=5, relief=tk.RAISED,
                               width=4, height=2,
                               command=lambda t=text: self.on_button_click(t))
            button.grid(row=row, column=col, padx=5, pady=5)
            col += 1
            if col > 5:
                col = 0
                row += 1
                
    def on_button_click(self, char):
        """Handles button click events."""
        if char == 'C':
            self.clear()
        elif char == '⌫':
            self.backspace()
        elif char == '=':
            self.calculate()
        # For scientific functions, append the function name and an opening parenthesis.
        elif char in ('sin', 'cos', 'tan', 'log', 'exp', 'sqrt'):
            self.expression += char + '('
            self.update_display()
        # For math constants, insert their value.
        elif char in ('pi', 'e'):
            self.expression += str(math.pi) if char == 'pi' else str(math.e)
            self.update_display()
        else:
            self.expression += str(char)
            self.update_display()
            
    def update_display(self):
        """Updates the entry display with the current expression."""
        self.display.delete(0, tk.END)
        self.display.insert(tk.END, self.expression)
        
    def clear(self):
        """Clears the current expression."""
        self.expression = ""
        self.update_display()
        
    def backspace(self):
        """Removes the last character from the expression."""
        self.expression = self.expression[:-1]
        self.update_display()
        
    def calculate(self):
        """Evaluates the expression using a safe dictionary of math functions."""
        try:
            # The eval function is given a restricted dictionary to prevent unsafe code execution.
            result = eval(self.expression, {"__builtins__": None}, {
                'sin': math.sin,
                'cos': math.cos,
                'tan': math.tan,
                'log': math.log,
                'exp': math.exp,
                'sqrt': math.sqrt,
                'pi': math.pi,
                'e': math.e
            })
            self.expression = str(result)
            self.update_display()
        except Exception:
            messagebox.showerror("Error", "Invalid Expression")
            self.expression = ""
            self.update_display()

if __name__ == "__main__":
    root = tk.Tk()
    calculator = ScientificCalculator(root)
    root.mainloop()
