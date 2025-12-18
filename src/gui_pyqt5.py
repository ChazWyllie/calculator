"""PyQt5-based GUI for the Advanced Calculator (modern, polished interface)."""

try:
    from PyQt5.QtWidgets import (
        QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout,
        QLineEdit, QPushButton, QLabel, QTextEdit, QTabWidget, QGridLayout,
        QGroupBox, QMessageBox, QScrollArea
    )
    from PyQt5.QtCore import Qt, QSize
    from PyQt5.QtGui import QFont, QIcon, QColor, QPalette
except ImportError:
    QApplication = None
    print("PyQt5 not installed. Install with: pip install PyQt5")

from src.calculator import Calculator


class CalculatorPyQT5:
    """Modern GUI interface for the Advanced Calculator using PyQt5."""
    
    def __init__(self):
        """Initialize the PyQt5 calculator."""
        if QApplication is None:
            raise ImportError("PyQt5 is not installed. Install with: pip install PyQt5")
        
        self.app = QApplication([])
        self.calculator = Calculator(verbose=False)
        self.setup_window()
    
    def setup_window(self):
        """Set up the main window."""
        self.window = QMainWindow()
        self.window.setWindowTitle("Advanced Calculator - PyQt5")
        self.window.setGeometry(100, 100, 800, 900)
        
        # Set modern stylesheet
        self.set_stylesheet()
        
        # Create central widget
        central_widget = QWidget()
        self.window.setCentralWidget(central_widget)
        
        # Create layout
        layout = QVBoxLayout(central_widget)
        layout.setSpacing(10)
        layout.setContentsMargins(15, 15, 15, 15)
        
        # Title
        title = QLabel("Advanced Calculator")
        title_font = QFont()
        title_font.setPointSize(20)
        title_font.setBold(True)
        title.setFont(title_font)
        layout.addWidget(title)
        
        # Input section
        layout.addWidget(self.create_input_section())
        
        # Calculator buttons
        layout.addWidget(self.create_calculator_section())
        
        # History
        layout.addWidget(self.create_history_section())
    
    def set_stylesheet(self):
        """Set a modern stylesheet."""
        stylesheet = """
        QMainWindow {
            background-color: #f5f5f5;
        }
        QLineEdit {
            padding: 8px;
            border: 2px solid #3498db;
            border-radius: 4px;
            font-size: 14px;
            background-color: #ffffff;
        }
        QPushButton {
            background-color: #3498db;
            color: white;
            border: none;
            padding: 8px 12px;
            border-radius: 4px;
            font-weight: bold;
            font-size: 11px;
        }
        QPushButton:hover {
            background-color: #2980b9;
        }
        QPushButton:pressed {
            background-color: #1f618d;
        }
        QPushButton#numberBtn {
            background-color: #34495e;
            font-size: 12px;
        }
        QPushButton#operatorBtn {
            background-color: #e74c3c;
        }
        QPushButton#operatorBtn:hover {
            background-color: #c0392b;
        }
        QPushButton#calcBtn {
            background-color: #27ae60;
            font-size: 13px;
        }
        QPushButton#calcBtn:hover {
            background-color: #229954;
        }
        QLabel {
            color: #2c3e50;
        }
        QTextEdit {
            background-color: #ffffff;
            border: 2px solid #bdc3c7;
            border-radius: 4px;
            padding: 5px;
            color: #2c3e50;
        }
        QTabWidget::pane {
            border: 2px solid #bdc3c7;
        }
        QTabBar::tab {
            background-color: #ecf0f1;
            padding: 6px 20px;
            margin-right: 2px;
        }
        QTabBar::tab:selected {
            background-color: #3498db;
            color: white;
        }
        QGroupBox {
            border: 2px solid #bdc3c7;
            border-radius: 4px;
            margin-top: 10px;
            padding-top: 10px;
            font-weight: bold;
        }
        QGroupBox::title {
            subcontrol-origin: margin;
            subcontrol-position: top left;
            padding: 0 3px;
        }
        """
        self.app.setStyleSheet(stylesheet)
    
    def create_input_section(self) -> QGroupBox:
        """Create the input display section."""
        group = QGroupBox("Display")
        layout = QVBoxLayout()
        
        # Expression label and display
        layout.addWidget(QLabel("Expression:"))
        self.expr_display = QLineEdit()
        self.expr_display.setReadOnly(True)
        self.expr_display.setFont(QFont("Courier", 11))
        layout.addWidget(self.expr_display)
        
        # Input field
        layout.addWidget(QLabel("Input:"))
        self.input_field = QLineEdit()
        self.input_field.setFont(QFont("Courier", 12))
        self.input_field.returnPressed.connect(self.calculate)
        layout.addWidget(self.input_field)
        
        # Result display
        layout.addWidget(QLabel("Result:"))
        self.result_display = QLineEdit()
        self.result_display.setReadOnly(True)
        result_font = QFont("Courier", 14)
        result_font.setBold(True)
        self.result_display.setFont(result_font)
        self.result_display.setStyleSheet("QLineEdit { color: #27ae60; background-color: #f0f8f0; }")
        layout.addWidget(self.result_display)
        
        group.setLayout(layout)
        return group
    
    def create_calculator_section(self) -> QTabWidget:
        """Create the calculator buttons section."""
        tabs = QTabWidget()
        
        # Basic arithmetic tab
        tabs.addTab(self.create_basic_tab(), "Basic")
        
        # Functions tab
        tabs.addTab(self.create_functions_tab(), "Functions")
        
        # Constants tab
        tabs.addTab(self.create_constants_tab(), "Constants")
        
        # Control buttons
        control_layout = QHBoxLayout()
        
        buttons_data = [
            ("Calculate", self.calculate, "#27ae60"),
            ("Clear", self.clear_input, "#e74c3c"),
            ("Delete Last", self.delete_last, "#f39c12"),
            ("Clear History", self.clear_history, "#95a5a6"),
        ]
        
        for text, callback, color in buttons_data:
            btn = QPushButton(text)
            btn.clicked.connect(callback)
            btn.setStyleSheet(f"QPushButton {{ background-color: {color}; }}")
            control_layout.addWidget(btn)
        
        # Add control buttons to tabs
        control_widget = QWidget()
        control_widget.setLayout(control_layout)
        tabs.addTab(control_widget, "Control")
        
        return tabs
    
    def create_basic_tab(self) -> QWidget:
        """Create basic arithmetic tab."""
        widget = QWidget()
        layout = QGridLayout()
        
        buttons = [
            [("7", "7"), ("8", "8"), ("9", "9"), ("÷", "/"), ("×", "*")],
            [("4", "4"), ("5", "5"), ("6", "6"), ("-", "-"), ("%", "%")],
            [("1", "1"), ("2", "2"), ("3", "3"), ("+", "+"), ("^", "^")],
            [("0", "0"), (".", "."), ("(", "("), (")", ")"), ("=", "=")],
        ]
        
        for row_idx, row in enumerate(buttons):
            for col_idx, (display, value) in enumerate(row):
                btn = QPushButton(display)
                btn.setObjectName("numberBtn")
                if value in ["/", "*", "-", "+", "%", "^"]:
                    btn.setObjectName("operatorBtn")
                elif value == "=":
                    btn.setObjectName("calcBtn")
                    btn.clicked.connect(self.calculate)
                else:
                    btn.clicked.connect(lambda checked, v=value: self.button_click(v))
                
                if value != "=":
                    btn.clicked.connect(lambda checked, v=value: self.button_click(v))
                
                btn.setMinimumHeight(50)
                layout.addWidget(btn, row_idx, col_idx)
        
        widget.setLayout(layout)
        return widget
    
    def create_functions_tab(self) -> QWidget:
        """Create functions tab."""
        widget = QWidget()
        main_layout = QVBoxLayout()
        
        # Trigonometric
        trig_layout = QGridLayout()
        trig_funcs = ["sin", "cos", "tan", "asin", "acos", "atan"]
        for i, func in enumerate(trig_funcs):
            btn = QPushButton(func)
            btn.clicked.connect(lambda checked, f=func: self.insert_function(f))
            btn.setMinimumHeight(40)
            trig_layout.addWidget(btn, 0, i)
        
        trig_group = QGroupBox("Trigonometric")
        trig_group.setLayout(trig_layout)
        main_layout.addWidget(trig_group)
        
        # Logarithmic
        log_layout = QGridLayout()
        log_funcs = ["log", "log10", "ln", "exp", "sqrt", "abs"]
        for i, func in enumerate(log_funcs):
            btn = QPushButton(func)
            btn.clicked.connect(lambda checked, f=func: self.insert_function(f))
            btn.setMinimumHeight(40)
            log_layout.addWidget(btn, 0, i)
        
        log_group = QGroupBox("Logarithmic & Utility")
        log_group.setLayout(log_layout)
        main_layout.addWidget(log_group)
        
        # Other functions
        other_layout = QGridLayout()
        other_funcs = ["floor", "ceil", "round", "factorial", "degrees", "radians"]
        for i, func in enumerate(other_funcs):
            btn = QPushButton(func)
            btn.clicked.connect(lambda checked, f=func: self.insert_function(f))
            btn.setMinimumHeight(40)
            other_layout.addWidget(btn, 0, i)
        
        other_group = QGroupBox("Advanced Functions")
        other_group.setLayout(other_layout)
        main_layout.addWidget(other_group)
        
        main_layout.addStretch()
        widget.setLayout(main_layout)
        return widget
    
    def create_constants_tab(self) -> QWidget:
        """Create constants tab."""
        widget = QWidget()
        layout = QVBoxLayout()
        
        for const_name, const_value in sorted(Calculator.CONSTANTS.items()):
            btn_layout = QHBoxLayout()
            
            btn = QPushButton(const_name.upper())
            btn.setMaximumWidth(100)
            btn.clicked.connect(lambda checked, c=const_name: self.insert_constant(c))
            btn_layout.addWidget(btn)
            
            label = QLabel(f"= {const_value:.10f}")
            label.setFont(QFont("Courier", 10))
            btn_layout.addWidget(label)
            
            btn_layout.addStretch()
            layout.addLayout(btn_layout)
        
        layout.addStretch()
        widget.setLayout(layout)
        return widget
    
    def create_history_section(self) -> QGroupBox:
        """Create history section."""
        group = QGroupBox("Calculation History")
        layout = QVBoxLayout()
        
        self.history_display = QTextEdit()
        self.history_display.setReadOnly(True)
        self.history_display.setFont(QFont("Courier", 9))
        self.history_display.setMaximumHeight(150)
        layout.addWidget(self.history_display)
        
        group.setLayout(layout)
        return group
    
    def button_click(self, value: str):
        """Handle button clicks."""
        current = self.input_field.text()
        self.input_field.setText(current + value)
        self.expr_display.setText(current + value)
    
    def insert_function(self, func: str):
        """Insert a function."""
        current = self.input_field.text()
        self.input_field.setText(current + func + "(")
        self.expr_display.setText(current + func + "(")
    
    def insert_constant(self, const: str):
        """Insert a constant."""
        current = self.input_field.text()
        self.input_field.setText(current + const)
        self.expr_display.setText(current + const)
    
    def calculate(self):
        """Calculate the expression."""
        expression = self.input_field.text().strip()
        
        if not expression:
            QMessageBox.showwarning(self.window, "Input Error", "Please enter an expression")
            return
        
        result = self.calculator.calculate(expression)
        formatted_result = self.calculator.format_result(result)
        
        # Update displays
        self.result_display.setText(formatted_result)
        
        # Update history
        self.update_history(expression, result)
        
        # Clear input
        if not str(result).startswith("Error"):
            self.input_field.clear()
            self.expr_display.clear()
    
    def update_history(self, expression: str, result):
        """Update history display."""
        formatted_result = self.calculator.format_result(result)
        current_history = self.history_display.toPlainText()
        
        new_entry = f"{expression} = {formatted_result}"
        self.history_display.setText(current_history + new_entry + "\n")
        
        # Scroll to bottom
        scrollbar = self.history_display.verticalScrollBar()
        scrollbar.setValue(scrollbar.maximum())
    
    def clear_input(self):
        """Clear input fields."""
        self.input_field.clear()
        self.expr_display.clear()
        self.result_display.clear()
    
    def delete_last(self):
        """Delete last character."""
        current = self.input_field.text()
        self.input_field.setText(current[:-1])
        self.expr_display.setText(current[:-1])
    
    def clear_history(self):
        """Clear history."""
        self.history_display.clear()
        self.calculator.clear_history()
    
    def run(self):
        """Run the application."""
        self.window.show()
        self.app.exec_()


def main():
    """Main entry point for PyQt5 GUI."""
    try:
        gui = CalculatorPyQT5()
        gui.run()
    except ImportError as e:
        print(f"Error: {e}")
        print("To use the PyQt5 GUI, install it with: pip install PyQt5")


if __name__ == "__main__":
    main()
