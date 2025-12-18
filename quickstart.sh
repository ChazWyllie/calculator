#!/bin/bash
# Quick start script for the Advanced Calculator

echo "🧮 Advanced Calculator - Quick Start"
echo "===================================="
echo ""

# Check if virtual environment exists
if [ ! -d "venv" ]; then
    echo "📦 Creating virtual environment..."
    python3 -m venv venv
fi

# Activate virtual environment
echo "✓ Activating virtual environment..."
source venv/bin/activate

# Install dependencies
echo "📥 Installing dependencies..."
pip install flask pytest -q

echo ""
echo "🚀 Choose how to run the calculator:"
echo ""
echo "1. Web GUI (Browser-based, recommended)"
echo "   python main.py web"
echo ""
echo "2. Interactive Menu"
echo "   python main.py"
echo ""
echo "3. Command-line"
echo "   python main.py \"2 + 3 * 4\""
echo ""
echo "4. Run tests"
echo "   pytest tests/"
echo ""
echo "👉 Tip: Visit http://localhost:5000 when running the web GUI"
