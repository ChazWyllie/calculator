"""Tkinter-based GUI for the Advanced Calculator."""

import tkinter as tk
from tkinter import ttk, scrolledtext, messagebox
from typing import Optional
import re

from src.calculator import Calculator
from src.enums import OperationType


class CalculatorGUI:
    """Modern GUI interface for the Advanced Calculator using Tkinter."""
    
    def __init__(self, root: tk.Tk):
        """
        Initialize the calculator GUI.
        
        Args:
            root: The root Tkinter window
        """
        self.root = root
        self.calculator = Calculator(verbose=False)
        self.setup_window()
        self.create_widgets()
        self.bind_shortcuts()
    
    def setup_window(self):
        """Configure the main window."""
        self.root.title("Advanced Calculator")
        self.root.geometry("600x700")
        self.root.resizable(True, True)
        
        # Set minimum window size
        self.root.minsize(500, 600)
        
        # Configure style
        self.root.configure(bg="#f0f0f0")
        style = ttk.Style()
        style.theme_use("clam")
        
        # Custom colors
        self.bg_color = "#f0f0f0"
        self.display_bg = "#2b2b2b"
        self.display_fg = "#00ff00"
        self.button_bg = "#404040"
        self.button_fg = "#ffffff"
    
    def create_widgets(self):
        """Create all GUI widgets."""
        # Main container
        main_frame = ttk.Frame(self.root, padding="10")
        main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        # Configure grid weights
        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(0, weight=1)
        main_frame.columnconfigure(0, weight=1)
        main_frame.rowconfigure(1, weight=1)
        
        # Create display and controls section
        self.create_display_section(main_frame)
        
        # Create calculator buttons section
        self.create_button_section(main_frame)
        
        # Create history section
        self.create_history_section(main_frame)
    
    def create_display_section(self, parent: ttk.Frame):
        """Create the display and input section."""
        display_frame = ttk.LabelFrame(parent, text="Display", padding="10")
        display_frame.grid(row=0, column=0, sticky=(tk.W, tk.E), pady=(0, 10))
        display_frame.columnconfigure(0, weight=1)
        
        # Expression display (read-only)
        ttk.Label(display_frame, text="Expression:").grid(row=0, column=0, sticky=tk.W)
        self.display_var = tk.StringVar(value="")
        display = ttk.Entry(
            display_frame,
            textvariable=self.display_var,
            font=("Courier", 14),
            state="readonly"
        )
        display.grid(row=0, column=1, sticky=(tk.W, tk.E), padx=(10, 0))
        display.configure(foreground="#0066cc")
        
        # Input field
        ttk.Label(display_frame, text="Input:").grid(row=1, column=0, sticky=tk.W, pady=(10, 0))
        self.input_var = tk.StringVar()
        self.input_field = ttk.Entry(
            display_frame,
            textvariable=self.input_var,
            font=("Courier", 12)
        )
        self.input_field.grid(row=1, column=1, sticky=(tk.W, tk.E), padx=(10, 0), pady=(10, 0))
        
        # Result display
        ttk.Label(display_frame, text="Result:").grid(row=2, column=0, sticky=tk.W, pady=(10, 0))
        self.result_var = tk.StringVar(value="")
        result_display = ttk.Entry(
            display_frame,
            textvariable=self.result_var,
            font=("Courier", 14, "bold"),
            state="readonly"
        )
        result_display.grid(row=2, column=1, sticky=(tk.W, tk.E), padx=(10, 0), pady=(10, 0))
        result_display.configure(foreground="#00aa00")
    
    def create_button_section(self, parent: ttk.Frame):
        """Create the calculator buttons section."""
        button_frame = ttk.LabelFrame(parent, text="Calculator", padding="10")
        button_frame.grid(row=1, column=0, sticky=(tk.W, tk.E, tk.N, tk.S), pady=(0, 10))
        
        # Create a notebook (tabs) for different button categories
        self.notebook = ttk.Notebook(button_frame)
        self.notebook.pack(fill=tk.BOTH, expand=True)
        
        # Basic arithmetic tab
        self.create_basic_tab()
        
        # Functions tab
        self.create_functions_tab()
        
        # Constants tab
        self.create_constants_tab()
        
        # Control buttons at bottom
        control_frame = ttk.Frame(button_frame)
        control_frame.pack(fill=tk.X, pady=(10, 0))
        
        ttk.Button(control_frame, text="Calculate", command=self.calculate).pack(side=tk.LEFT, padx=5)
        ttk.Button(control_frame, text="Clear", command=self.clear_input).pack(side=tk.LEFT, padx=5)
        ttk.Button(control_frame, text="Delete Last", command=self.delete_last).pack(side=tk.LEFT, padx=5)
        ttk.Button(control_frame, text="Clear History", command=self.clear_history).pack(side=tk.LEFT, padx=5)
    
    def create_basic_tab(self):
        """Create basic arithmetic buttons tab."""
        tab = ttk.Frame(self.notebook)
        self.notebook.add(tab, text="Basic")
        
        buttons = [
            [("7", "7"), ("8", "8"), ("9", "9"), ("÷", "/")],
            [("4", "4"), ("5", "5"), ("6", "6"), ("×", "*")],
            [("1", "1"), ("2", "2"), ("3", "3"), ("-", "-")],
            [("0", "0"), (".", "."), ("=", "calculate"), ("+", "+")],
            [("(", "("), (")", ")"), ("%", "%"), ("^", "^")],
        ]
        
        for row_idx, row in enumerate(buttons):
            for col_idx, (display, value) in enumerate(row):
                btn = ttk.Button(
                    tab,
                    text=display,
                    command=lambda v=value: self.button_click(v) if v != "calculate" else self.calculate()
                )
                btn.grid(row=row_idx, column=col_idx, sticky=(tk.W, tk.E, tk.N, tk.S), padx=2, pady=2)
        
        # Configure grid weights
        for i in range(5):
            tab.rowconfigure(i, weight=1)
            tab.columnconfigure(i % 4, weight=1)
    
    def create_functions_tab(self):
        """Create mathematical functions tab."""
        tab = ttk.Frame(self.notebook)
        self.notebook.add(tab, text="Functions")
        
        # Trigonometric
        trig_frame = ttk.LabelFrame(tab, text="Trigonometric", padding="5")
        trig_frame.pack(fill=tk.X, padx=5, pady=5)
        
        trig_buttons = ["sin", "cos", "tan", "asin", "acos", "atan"]
        for i, func in enumerate(trig_buttons):
            ttk.Button(
                trig_frame,
                text=func,
                command=lambda f=func: self.insert_function(f)
            ).grid(row=0, column=i, sticky=(tk.W, tk.E), padx=2, pady=2)
        
        # Hyperbolic
        hyp_frame = ttk.LabelFrame(tab, text="Hyperbolic", padding="5")
        hyp_frame.pack(fill=tk.X, padx=5, pady=5)
        
        hyp_buttons = ["sinh", "cosh", "tanh"]
        for i, func in enumerate(hyp_buttons):
            ttk.Button(
                hyp_frame,
                text=func,
                command=lambda f=func: self.insert_function(f)
            ).grid(row=0, column=i, sticky=(tk.W, tk.E), padx=2, pady=2)
        
        # Logarithmic
        log_frame = ttk.LabelFrame(tab, text="Logarithmic", padding="5")
        log_frame.pack(fill=tk.X, padx=5, pady=5)
        
        log_buttons = ["log", "log10", "ln", "exp"]
        for i, func in enumerate(log_buttons):
            ttk.Button(
                log_frame,
                text=func,
                command=lambda f=func: self.insert_function(f)
            ).grid(row=0, column=i, sticky=(tk.W, tk.E), padx=2, pady=2)
        
        # Utility
        util_frame = ttk.LabelFrame(tab, text="Utility", padding="5")
        util_frame.pack(fill=tk.X, padx=5, pady=5)
        
        util_buttons = ["sqrt", "abs", "floor", "ceil", "round", "factorial"]
        for i, func in enumerate(util_buttons):
            ttk.Button(
                util_frame,
                text=func,
                command=lambda f=func: self.insert_function(f)
            ).grid(row=0, column=i % 6, sticky=(tk.W, tk.E), padx=2, pady=2)
        
        # Angle conversion
        angle_frame = ttk.LabelFrame(tab, text="Angle Conversion", padding="5")
        angle_frame.pack(fill=tk.X, padx=5, pady=5)
        
        angle_buttons = ["degrees", "radians"]
        for i, func in enumerate(angle_buttons):
            ttk.Button(
                angle_frame,
                text=func,
                command=lambda f=func: self.insert_function(f)
            ).grid(row=0, column=i, sticky=(tk.W, tk.E), padx=2, pady=2)
    
    def create_constants_tab(self):
        """Create constants tab."""
        tab = ttk.Frame(self.notebook)
        self.notebook.add(tab, text="Constants")
        
        constants_frame = ttk.LabelFrame(tab, text="Mathematical Constants", padding="10")
        constants_frame.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)
        
        for const_name, const_value in sorted(Calculator.CONSTANTS.items()):
            frame = ttk.Frame(constants_frame)
            frame.pack(fill=tk.X, pady=5)
            
            ttk.Button(
                frame,
                text=const_name.upper(),
                command=lambda c=const_name: self.insert_constant(c),
                width=10
            ).pack(side=tk.LEFT, padx=5)
            
            ttk.Label(
                frame,
                text=f"= {const_value:.10f}",
                font=("Courier", 10)
            ).pack(side=tk.LEFT, padx=5)
    
    def create_history_section(self, parent: ttk.Frame):
        """Create the calculation history section."""
        history_frame = ttk.LabelFrame(parent, text="Calculation History", padding="10")
        history_frame.grid(row=2, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        history_frame.columnconfigure(0, weight=1)
        history_frame.rowconfigure(0, weight=1)
        
        # Create scrolled text widget
        self.history_text = scrolledtext.ScrolledText(
            history_frame,
            height=8,
            width=70,
            font=("Courier", 9),
            state="disabled"
        )
        self.history_text.pack(fill=tk.BOTH, expand=True)
        
        # Configure tags for styling
        self.history_text.tag_config("error", foreground="red")
        self.history_text.tag_config("success", foreground="green")
        self.history_text.tag_config("separator", foreground="gray")
    
    def bind_shortcuts(self):
        """Bind keyboard shortcuts."""
        self.root.bind("<Return>", lambda e: self.calculate())
        self.root.bind("<Escape>", lambda e: self.clear_input())
        self.root.bind("<BackSpace>", lambda e: self.delete_last())
        self.input_field.bind("<Return>", lambda e: self.calculate())
    
    def button_click(self, value: str):
        """Handle button clicks."""
        current = self.input_var.get()
        self.input_var.set(current + value)
        self.display_var.set(current + value)
    
    def insert_function(self, func: str):
        """Insert a function with opening parenthesis."""
        current = self.input_var.get()
        self.input_var.set(current + func + "(")
        self.display_var.set(current + func + "(")
    
    def insert_constant(self, const: str):
        """Insert a constant."""
        current = self.input_var.get()
        self.input_var.set(current + const)
        self.display_var.set(current + const)
    
    def calculate(self):
        """Calculate the current expression."""
        expression = self.input_var.get().strip()
        
        if not expression:
            messagebox.showwarning("Input Error", "Please enter an expression")
            return
        
        result = self.calculator.calculate(expression)
        formatted_result = self.calculator.format_result(result)
        
        # Update result display
        self.result_var.set(formatted_result)
        
        # Update history
        self.update_history(expression, result)
        
        # Clear input after successful calculation
        if not str(result).startswith("Error"):
            self.input_var.set("")
            self.display_var.set("")
    
    def update_history(self, expression: str, result):
        """Update the history display."""
        self.history_text.config(state="normal")
        
        # Format the result
        formatted_result = self.calculator.format_result(result)
        
        # Determine if it's an error
        is_error = isinstance(result, str) and "Error" in result
        
        # Add to history
        if is_error:
            self.history_text.insert(tk.END, f"{expression}\n", "error")
            self.history_text.insert(tk.END, f"  → {formatted_result}\n", "error")
        else:
            self.history_text.insert(tk.END, f"{expression}\n", "success")
            self.history_text.insert(tk.END, f"  → {formatted_result}\n", "success")
        
        self.history_text.insert(tk.END, "-" * 50 + "\n", "separator")
        
        # Auto-scroll to bottom
        self.history_text.see(tk.END)
        self.history_text.config(state="disabled")
    
    def clear_input(self):
        """Clear the input field."""
        self.input_var.set("")
        self.display_var.set("")
        self.result_var.set("")
    
    def delete_last(self):
        """Delete the last character from input."""
        current = self.input_var.get()
        self.input_var.set(current[:-1])
        self.display_var.set(current[:-1])
    
    def clear_history(self):
        """Clear the calculation history."""
        self.history_text.config(state="normal")
        self.history_text.delete(1.0, tk.END)
        self.history_text.config(state="disabled")
        self.calculator.clear_history()


def main():
    """Run the calculator GUI."""
    root = tk.Tk()
    gui = CalculatorGUI(root)
    root.mainloop()


if __name__ == "__main__":
    main()
