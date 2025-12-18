"""Launch script for GUI applications."""

import sys
from pathlib import Path


def main():
    """Main launcher for GUI."""
    if len(sys.argv) > 1:
        gui_type = sys.argv[1].lower()
        
        if gui_type == "web":
            from src.gui_web import main as web_main
            web_main()
        
        elif gui_type == "tkinter":
            from src.gui_tkinter import main as tkinter_main
            tkinter_main()
        
        elif gui_type == "pyqt5":
            from src.gui_pyqt5 import main as pyqt5_main
            pyqt5_main()
        
        else:
            print(f"Unknown GUI type: {gui_type}")
            print("Usage: python gui.py [web|tkinter|pyqt5]")
            sys.exit(1)
    else:
        # Default to web GUI
        from src.gui_web import main as web_main
        web_main()


if __name__ == "__main__":
    main()
