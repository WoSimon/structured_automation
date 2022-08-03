#!/bin/zsh

# Open Structured.app
cd /Applications
open Structured.app

# Execute the Python script
cd /Users/SimonWosnitza/PycharmProjects/structured_automation/
python3 new_task.py

# Close Structured.app
osascript -e 'tell application "Structured" to quit'
