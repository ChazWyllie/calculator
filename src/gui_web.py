"""Web-based GUI for the Advanced Calculator using Flask."""

import os
import sys
from pathlib import Path

try:
    from flask import Flask, render_template_string, request, jsonify
except ImportError:
    Flask = None
    print("Flask not installed. Install with: pip install flask")
    sys.exit(1)

from src.calculator import Calculator


class CalculatorWebGUI:
    """Web-based GUI for the calculator using Flask."""
    
    HTML_TEMPLATE = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Advanced Calculator</title>
        <style>
            * {
                margin: 0;
                padding: 0;
                box-sizing: border-box;
            }
            
            body {
                font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
                background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
                min-height: 100vh;
                display: flex;
                justify-content: center;
                align-items: center;
                padding: 20px;
            }
            
            .container {
                background: white;
                border-radius: 15px;
                box-shadow: 0 10px 40px rgba(0, 0, 0, 0.3);
                max-width: 600px;
                width: 100%;
                padding: 30px;
            }
            
            h1 {
                text-align: center;
                color: #333;
                margin-bottom: 30px;
                font-size: 28px;
            }
            
            .display {
                background: #2b2b2b;
                color: #00ff00;
                padding: 15px;
                border-radius: 8px;
                margin-bottom: 20px;
                font-family: 'Courier New', monospace;
                font-size: 16px;
                word-wrap: break-word;
                min-height: 40px;
                border: 2px solid #667eea;
            }
            
            .result-display {
                background: #f0f8f0;
                color: #00aa00;
                padding: 15px;
                border-radius: 8px;
                margin-bottom: 20px;
                font-family: 'Courier New', monospace;
                font-size: 18px;
                font-weight: bold;
                border: 2px solid #27ae60;
            }
            
            input[type="text"] {
                width: 100%;
                padding: 12px;
                border: 2px solid #ddd;
                border-radius: 8px;
                font-size: 14px;
                margin-bottom: 20px;
                transition: border-color 0.3s;
            }
            
            input[type="text"]:focus {
                outline: none;
                border-color: #667eea;
                box-shadow: 0 0 5px rgba(102, 126, 234, 0.3);
            }
            
            .button-grid {
                display: grid;
                grid-template-columns: repeat(4, 1fr);
                gap: 10px;
                margin-bottom: 20px;
            }
            
            .btn {
                padding: 12px;
                border: none;
                border-radius: 8px;
                font-size: 14px;
                font-weight: bold;
                cursor: pointer;
                transition: all 0.3s;
                color: white;
            }
            
            .btn-number {
                background: #34495e;
            }
            
            .btn-number:hover {
                background: #2c3e50;
                transform: translateY(-2px);
                box-shadow: 0 5px 15px rgba(0, 0, 0, 0.2);
            }
            
            .btn-operator {
                background: #e74c3c;
            }
            
            .btn-operator:hover {
                background: #c0392b;
                transform: translateY(-2px);
                box-shadow: 0 5px 15px rgba(231, 76, 60, 0.3);
            }
            
            .btn-equal {
                background: #27ae60;
                grid-column: span 2;
            }
            
            .btn-equal:hover {
                background: #229954;
                transform: translateY(-2px);
                box-shadow: 0 5px 15px rgba(39, 174, 96, 0.3);
            }
            
            .btn-clear {
                background: #f39c12;
                grid-column: span 2;
            }
            
            .btn-clear:hover {
                background: #d68910;
                transform: translateY(-2px);
                box-shadow: 0 5px 15px rgba(243, 156, 18, 0.3);
            }
            
            .functions-grid {
                display: grid;
                grid-template-columns: repeat(3, 1fr);
                gap: 10px;
                margin-bottom: 20px;
            }
            
            .btn-function {
                background: #3498db;
                padding: 10px;
                font-size: 12px;
            }
            
            .btn-function:hover {
                background: #2980b9;
                transform: translateY(-2px);
                box-shadow: 0 5px 15px rgba(52, 152, 219, 0.3);
            }
            
            .tabs {
                display: flex;
                gap: 10px;
                margin-bottom: 20px;
                border-bottom: 2px solid #ecf0f1;
            }
            
            .tab-btn {
                padding: 10px 20px;
                background: #ecf0f1;
                border: none;
                border-radius: 8px 8px 0 0;
                cursor: pointer;
                font-weight: bold;
                color: #666;
                transition: all 0.3s;
            }
            
            .tab-btn.active {
                background: #667eea;
                color: white;
            }
            
            .tab-content {
                display: none;
            }
            
            .tab-content.active {
                display: block;
            }
            
            .history {
                background: #f8f9fa;
                border: 2px solid #ecf0f1;
                border-radius: 8px;
                padding: 15px;
                max-height: 200px;
                overflow-y: auto;
                font-family: 'Courier New', monospace;
                font-size: 12px;
            }
            
            .history-item {
                padding: 8px;
                border-bottom: 1px solid #e0e0e0;
                color: #333;
            }
            
            .history-item:last-child {
                border-bottom: none;
            }
            
            .error {
                color: #e74c3c;
            }
            
            .success {
                color: #27ae60;
            }
            
            .constants-grid {
                display: grid;
                grid-template-columns: 1fr 1fr;
                gap: 10px;
                margin-bottom: 20px;
            }
            
            .const-btn {
                background: #9b59b6;
            }
            
            .const-btn:hover {
                background: #8e44ad;
                transform: translateY(-2px);
                box-shadow: 0 5px 15px rgba(155, 89, 182, 0.3);
            }
            
            .const-value {
                background: #ecf0f1;
                padding: 10px;
                border-radius: 8px;
                margin-bottom: 10px;
                font-size: 12px;
                color: #666;
            }
        </style>
    </head>
    <body>
        <div class="container">
            <h1>Advanced Calculator</h1>
            
            <div class="display" id="display">0</div>
            <div class="result-display" id="result"></div>
            
            <input type="text" id="input" placeholder="Enter expression..." />
            
            <div class="tabs">
                <button class="tab-btn active" onclick="switchTab('basic')">Basic</button>
                <button class="tab-btn" onclick="switchTab('functions')">Functions</button>
                <button class="tab-btn" onclick="switchTab('constants')">Constants</button>
                <button class="tab-btn" onclick="switchTab('history')">History</button>
            </div>
            
            <!-- Basic Tab -->
            <div id="basic" class="tab-content active">
                <div class="button-grid">
                    <button class="btn btn-number" onclick="addToInput('7')">7</button>
                    <button class="btn btn-number" onclick="addToInput('8')">8</button>
                    <button class="btn btn-number" onclick="addToInput('9')">9</button>
                    <button class="btn btn-operator" onclick="addToInput('/')">&divide;</button>
                    
                    <button class="btn btn-number" onclick="addToInput('4')">4</button>
                    <button class="btn btn-number" onclick="addToInput('5')">5</button>
                    <button class="btn btn-number" onclick="addToInput('6')">6</button>
                    <button class="btn btn-operator" onclick="addToInput('*')">&times;</button>
                    
                    <button class="btn btn-number" onclick="addToInput('1')">1</button>
                    <button class="btn btn-number" onclick="addToInput('2')">2</button>
                    <button class="btn btn-number" onclick="addToInput('3')">3</button>
                    <button class="btn btn-operator" onclick="addToInput('-')">-</button>
                    
                    <button class="btn btn-number" onclick="addToInput('0')">0</button>
                    <button class="btn btn-number" onclick="addToInput('.')">.</button>
                    <button class="btn btn-equal" onclick="calculate()">=</button>
                    
                    <button class="btn btn-operator" onclick="addToInput('+')">+</button>
                    <button class="btn btn-operator" onclick="addToInput('^')">^</button>
                    <button class="btn btn-operator" onclick="addToInput('%')">%</button>
                    <button class="btn btn-clear" onclick="clearInput()">Clear</button>
                </div>
            </div>
            
            <!-- Functions Tab -->
            <div id="functions" class="tab-content">
                <h3 style="margin-top: 0; margin-bottom: 10px;">Trigonometric</h3>
                <div class="functions-grid">
                    <button class="btn btn-function" onclick="addToInput('sin(')">sin</button>
                    <button class="btn btn-function" onclick="addToInput('cos(')">cos</button>
                    <button class="btn btn-function" onclick="addToInput('tan(')">tan</button>
                    <button class="btn btn-function" onclick="addToInput('asin(')">asin</button>
                    <button class="btn btn-function" onclick="addToInput('acos(')">acos</button>
                    <button class="btn btn-function" onclick="addToInput('atan(')">atan</button>
                </div>
                
                <h3 style="margin-top: 15px; margin-bottom: 10px;">Logarithmic & Utility</h3>
                <div class="functions-grid">
                    <button class="btn btn-function" onclick="addToInput('log(')">log</button>
                    <button class="btn btn-function" onclick="addToInput('ln(')">ln</button>
                    <button class="btn btn-function" onclick="addToInput('sqrt(')">sqrt</button>
                    <button class="btn btn-function" onclick="addToInput('abs(')">abs</button>
                    <button class="btn btn-function" onclick="addToInput('floor(')">floor</button>
                    <button class="btn btn-function" onclick="addToInput('ceil(')">ceil</button>
                </div>
            </div>
            
            <!-- Constants Tab -->
            <div id="constants" class="tab-content">
                <div class="const-value">
                    <button class="btn const-btn" style="width: 100%; margin-bottom: 10px;" onclick="addToInput('pi')">π (pi)</button>
                    <span>= 3.1415926536...</span>
                </div>
                <div class="const-value">
                    <button class="btn const-btn" style="width: 100%; margin-bottom: 10px;" onclick="addToInput('e')">e</button>
                    <span>= 2.7182818285...</span>
                </div>
                <div class="const-value">
                    <button class="btn const-btn" style="width: 100%; margin-bottom: 10px;" onclick="addToInput('phi')">φ (phi)</button>
                    <span>= 1.6180339887...</span>
                </div>
                <div class="const-value">
                    <button class="btn const-btn" style="width: 100%; margin-bottom: 10px;" onclick="addToInput('tau')">τ (tau)</button>
                    <span>= 6.2831853072...</span>
                </div>
            </div>
            
            <!-- History Tab -->
            <div id="history" class="tab-content">
                <div class="history" id="historyList"></div>
                <button class="btn btn-clear" style="width: 100%; margin-top: 10px;" onclick="clearHistory()">Clear History</button>
            </div>
        </div>
        
        <script>
            function addToInput(value) {
                const input = document.getElementById('input');
                input.value += value;
                updateDisplay();
            }
            
            function updateDisplay() {
                const input = document.getElementById('input');
                const display = document.getElementById('display');
                display.textContent = input.value || '0';
            }
            
            function clearInput() {
                document.getElementById('input').value = '';
                document.getElementById('result').textContent = '';
                updateDisplay();
            }
            
            function deleteLast() {
                const input = document.getElementById('input');
                input.value = input.value.slice(0, -1);
                updateDisplay();
            }
            
            function calculate() {
                const input = document.getElementById('input');
                const expression = input.value;
                
                if (!expression) return;
                
                fetch('/calculate', {
                    method: 'POST',
                    headers: {'Content-Type': 'application/json'},
                    body: JSON.stringify({expression: expression})
                })
                .then(response => response.json())
                .then(data => {
                    const resultDiv = document.getElementById('result');
                    if (data.error) {
                        resultDiv.textContent = data.error;
                        resultDiv.style.color = '#e74c3c';
                        addToHistory(expression, data.error, true);
                    } else {
                        resultDiv.textContent = data.result;
                        resultDiv.style.color = '#27ae60';
                        addToHistory(expression, data.result, false);
                        input.value = '';
                        updateDisplay();
                    }
                });
            }
            
            function addToHistory(expr, result, isError) {
                const historyList = document.getElementById('historyList');
                const item = document.createElement('div');
                item.className = 'history-item' + (isError ? ' error' : ' success');
                item.textContent = expr + ' = ' + result;
                historyList.appendChild(item);
                historyList.scrollTop = historyList.scrollHeight;
            }
            
            function clearHistory() {
                document.getElementById('historyList').innerHTML = '';
            }
            
            function switchTab(tabName) {
                // Hide all tabs
                document.querySelectorAll('.tab-content').forEach(tab => {
                    tab.classList.remove('active');
                });
                
                // Remove active class from all buttons
                document.querySelectorAll('.tab-btn').forEach(btn => {
                    btn.classList.remove('active');
                });
                
                // Show selected tab
                document.getElementById(tabName).classList.add('active');
                event.target.classList.add('active');
            }
            
            // Keyboard support
            document.addEventListener('keydown', function(e) {
                if (e.key === 'Enter') {
                    calculate();
                } else if (e.key === 'Escape') {
                    clearInput();
                } else if (e.key === 'Backspace') {
                    deleteLast();
                }
            });
            
            // Focus on input
            document.getElementById('input').focus();
        </script>
    </body>
    </html>
    """
    
    def __init__(self, port: int = 5000):
        """Initialize the web-based calculator."""
        self.app = Flask(__name__)
        self.calculator = Calculator(verbose=False)
        self.port = port
        self.setup_routes()
    
    def setup_routes(self):
        """Set up Flask routes."""
        
        @self.app.route("/")
        def index():
            return render_template_string(self.HTML_TEMPLATE)
        
        @self.app.route("/calculate", methods=["POST"])
        def calculate():
            data = request.json
            expression = data.get("expression", "").strip()
            
            if not expression:
                return jsonify({"error": "Empty expression"})
            
            result = self.calculator.calculate(expression)
            formatted_result = self.calculator.format_result(result)
            
            if isinstance(result, str) and "Error" in result:
                return jsonify({"error": formatted_result})
            
            return jsonify({"result": formatted_result})
    
    def run(self, debug: bool = False):
        """Run the Flask application."""
        print(f"\n🚀 Advanced Calculator Web Interface")
        print(f"📊 Open your browser and go to: http://localhost:{self.port}")
        print(f"Press Ctrl+C to stop the server\n")
        
        self.app.run(debug=debug, port=self.port, use_reloader=False)


def main():
    """Main entry point for web GUI."""
    try:
        gui = CalculatorWebGUI()
        gui.run(debug=False)
    except ImportError:
        print("Flask is required for the web GUI.")
        print("Install it with: pip install flask")
        sys.exit(1)


if __name__ == "__main__":
    main()
