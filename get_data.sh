#!/bin/zsh

# Open Structured.app
cd /Applications
open Structured.app

# Execute the Python script to create a Backup
cd /Users/SimonWosnitza/PycharmProjects/structured_automation/
python3 get_backup.py

# Close Structured.app
osascript -e 'tell application "Structured" to quit'

# Execute the Python script to extract Tasks from the Backup
cd /Users/SimonWosnitza/PycharmProjects/structured_automation/
python3 get_tasks.py

